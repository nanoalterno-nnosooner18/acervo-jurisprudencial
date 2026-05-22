# -*- coding: utf-8 -*-
"""
Scraper semanal del Semanario Judicial de la Federación (SJF).
Diseñado para correr en GitHub Actions cada viernes.

Usa Playwright (Chromium headless) para renderizar la SPA Angular del SJF,
busca tesis recientes en los temas del acervo, extrae las que se publicaron
en los últimos 8 días, y las agrega al dataset si no existen ya.

Después regenera index.html / HTML / DOCX / XLSX llamando a los generadores.

NO inventa datos: solo guarda registros reales extraídos del SJF.
"""
import re
import sys
import datetime
import importlib.util
from pathlib import Path

# Playwright se instala en el workflow
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
DATASET_PATH = SCRIPT_DIR / "acervo_dataset.py"

# Temas a vigilar cada semana (término de búsqueda -> metadata por defecto)
TEMAS = [
    ("usucapión prescripción", "Civil", "Usucapión / Prescripción positiva"),
    ("juicio hipotecario", "Civil", "Juicio hipotecario"),
    ("arrendamiento", "Civil", "Arrendamiento"),
    ("fideicomiso", "Civil-Mercantil", "Fideicomisos"),
    ("extinción de dominio", "Civil-Penal", "Extinción de dominio"),
    ("derecho humano agua", "Administrativo", "Agua y servicios públicos"),
    ("condominio", "Civil — Condominio", "Régimen de propiedad en condominio"),
    ("juicio ejecutivo mercantil", "Mercantil", "Juicio ejecutivo mercantil"),
    ("pagaré título de crédito", "Mercantil", "Títulos de crédito"),
    ("concurso mercantil", "Mercantil", "Concursos mercantiles"),
    ("velo corporativo", "Mercantil", "Sociedades mercantiles"),
    ("prisión preventiva oficiosa", "Penal", "Prisión preventiva oficiosa"),
    ("prueba ilícita", "Penal", "Prueba ilícita"),
    ("cadena de custodia", "Penal", "Cadena de custodia"),
    ("tortura", "Penal", "Tortura"),
    ("reparación del daño", "Penal", "Reparación del daño"),
    ("caducidad facultades comprobación", "Fiscal", "Caducidad de facultades del fisco"),
    ("devolución saldo a favor", "Fiscal", "Devolución de saldos a favor"),
    ("operaciones inexistentes 69-B", "Fiscal", "Comprobantes fiscales (CFDI)"),
    ("despido carga probatoria", "Laboral", "Despido injustificado"),
    ("subcontratación REPSE", "Laboral", "Subcontratación / Outsourcing"),
    ("responsabilidad administrativa", "Administrativo", "Responsabilidad administrativa de servidores públicos"),
    ("interés legítimo amparo", "Amparo", "Procedencia del amparo"),
    ("suspensión apariencia buen derecho", "Amparo", "Suspensión"),
    ("perspectiva de género", "Constitucional / DDHH", "Perspectiva de género"),
    ("identidad de género", "Constitucional / DDHH", "Identidad de género"),
    ("derecho a la salud", "Administrativo / Salud", "Derecho humano a la salud"),
    ("medio ambiente sano", "Constitucional / Ambiental", "Medio ambiente sano"),
]

INSTANCIA_JERARQUIA = {
    "Pleno": (1, "Pleno SCJN"),
    "Primera Sala": (2, "Primera Sala SCJN"),
    "Segunda Sala": (2, "Segunda Sala SCJN"),
    "Plenos Regionales": (3, "Plenos Regionales"),
    "TCC": (4, "Tribunales Colegiados de Circuito"),
}


def cargar_dataset():
    spec = importlib.util.spec_from_file_location("acervo_dataset", DATASET_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ACERVO


def registros_existentes(acervo):
    regs = set()
    for e in acervo["entradas"]:
        rd = str(e.get("registro_digital", ""))
        m = re.search(r"\b(\d{6,7})\b", rd)
        if m:
            regs.add(m.group(1))
    return regs


def parse_resultado(bloque):
    """Extrae registro, rubro, instancia, época y fecha de un bloque de resultado."""
    reg = re.search(r"Registro digital:\s*(\d{6,7})", bloque)
    if not reg:
        return None
    registro = reg.group(1)
    # rubro: la línea siguiente al registro, en mayúsculas
    lineas = [l.strip() for l in bloque.split("\n") if l.strip()]
    rubro = ""
    for i, l in enumerate(lineas):
        if "Registro digital" in l and i + 1 < len(lineas):
            rubro = lineas[i + 1]
            break
    # instancia, época, fecha de la línea con ';'
    instancia = "Tribunales Colegiados de Circuito"
    epoca = "Duodécima Época"
    fecha = ""
    meta = re.search(r"(SCJN|TCC|Plenos Regionales);\s*(\d+a\.?)\s*Época[^;]*;[^;]*;([^;]*);?\s*Publicaci[oó]n:\s*([^\n]+)", bloque)
    if meta:
        org = meta.group(1)
        ep = meta.group(2)
        fecha = meta.group(4).strip()
        if org == "SCJN":
            instancia = "Primera Sala SCJN" if "1a." in bloque else ("Segunda Sala SCJN" if "2a." in bloque else "Pleno SCJN")
        elif org == "Plenos Regionales":
            instancia = "Plenos Regionales"
        else:
            instancia = "Tribunales Colegiados de Circuito"
        epoca_map = {"12a.": "Duodécima Época", "11a.": "Undécima Época", "10a.": "Décima Época", "9a.": "Novena Época"}
        epoca = epoca_map.get(ep, epoca)
    return {"registro": registro, "rubro": rubro, "instancia": instancia, "epoca": epoca, "fecha": fecha}


def es_de_esta_semana(fecha_str):
    """Devuelve True si la fecha de publicación es de los últimos 8 días."""
    if not fecha_str:
        return False
    meses = {"enero":1,"febrero":2,"marzo":3,"abril":4,"mayo":5,"junio":6,
             "julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}
    m = re.search(r"(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", fecha_str.lower())
    if not m:
        return False
    try:
        dia = int(m.group(1)); mes = meses.get(m.group(2)); anio = int(m.group(3))
        if not mes:
            return False
        fpub = datetime.date(anio, mes, dia)
        return (datetime.date.today() - fpub).days <= 8
    except Exception:
        return False


def jerarquia_de(instancia):
    if "Pleno SCJN" in instancia:
        return 1
    if "Sala SCJN" in instancia:
        return 2
    if "Plenos Regionales" in instancia:
        return 3
    return 4


def buscar_tema(page, termino):
    page.goto("https://sjf2.scjn.gob.mx/busqueda-principal-tesis", wait_until="networkidle")
    page.wait_for_timeout(2500)
    inp = page.query_selector("input[type=text]")
    if not inp:
        return ""
    inp.fill(termino)
    page.wait_for_timeout(400)
    botones = page.query_selector_all("button")
    for b in botones:
        if (b.inner_text() or "").strip() == "Buscar":
            b.click()
            break
    page.wait_for_timeout(5000)
    return page.inner_text("body")


def main():
    acervo = cargar_dataset()
    existentes = registros_existentes(acervo)
    nuevas = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(30000)
        for termino, materia, tema in TEMAS:
            try:
                texto = buscar_tema(page, termino)
            except Exception as ex:
                print(f"[WARN] fallo búsqueda '{termino}': {ex}")
                continue
            bloques = re.findall(r"Registro digital:\s*\d{6,7}[\s\S]{0,400}", texto)
            for bloque in bloques[:5]:
                info = parse_resultado(bloque)
                if not info:
                    continue
                if info["registro"] in existentes:
                    continue
                if not es_de_esta_semana(info["fecha"]):
                    continue
                existentes.add(info["registro"])
                nuevas.append({
                    "id": f"auto-{info['registro']}",
                    "tipo": "jurisprudencia" if "J/" in bloque or "/J." in bloque else "tesis aislada",
                    "instancia": info["instancia"],
                    "jerarquia": jerarquia_de(info["instancia"]),
                    "epoca": info["epoca"],
                    "vigencia": "vigente",
                    "materia": materia,
                    "tema": tema,
                    "subtema": "Actualización automática semanal",
                    "ambito": "Federal",
                    "rubro": info["rubro"],
                    "texto_resumen": "Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.",
                    "registro_digital": info["registro"],
                    "url_sjf": f"https://sjf2.scjn.gob.mx/detalle/tesis/{info['registro']}",
                    "fecha_publicacion": info["fecha"],
                    "fuente_publicacion": "Semanario Judicial de la Federación — captura automática",
                    "trascendencia": "Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.",
                    "explicacion": "Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.",
                    "etiquetas": [tema, "actualización automática"],
                })
        browser.close()

    if not nuevas:
        print("SIN_NOVEDADES")
        return 0

    # Reescribir el dataset agregando las nuevas entradas antes del cierre del array
    contenido = DATASET_PATH.read_text(encoding="utf-8")
    bloque_nuevo = ""
    for e in nuevas:
        bloque_nuevo += "        " + repr(e) + ",\n"
    idx = contenido.rfind("    ],")
    if idx == -1:
        print("ERROR: no se encontró el cierre del array")
        return 1
    contenido = contenido[:idx] + bloque_nuevo + contenido[idx:]
    DATASET_PATH.write_text(contenido, encoding="utf-8")
    print(f"AGREGADAS:{len(nuevas)}")
    for e in nuevas:
        print(f"  + {e['registro_digital']} | {e['rubro'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
