# -*- coding: utf-8 -*-
"""Genera el archivo HTML interactivo del acervo."""
import json, html, re
from pathlib import Path
from acervo_dataset import ACERVO


def materia_canonica(m: str) -> str:
    m = m.lower()
    if "amparo" in m:
        return "Amparo"
    if "condominio" in m:
        return "Civil — Condominio"
    if m.startswith("civil"):
        return "Civil"
    if "mercantil" in m:
        return "Mercantil"
    if "penal" in m:
        return "Penal"
    if "fiscal" in m:
        return "Fiscal"
    if "laboral" in m:
        return "Laboral"
    if "administrativo" in m:
        return "Administrativo"
    if "constitucional" in m:
        return "Constitucional / DDHH"
    return m.title()


def instancia_corta(i: str) -> str:
    if "Pleno SCJN" in i:
        return "Pleno SCJN"
    if "Primera Sala" in i:
        return "1ª Sala SCJN"
    if "Segunda Sala" in i:
        return "2ª Sala SCJN"
    if "Plenos Regionales" in i or "Plenos de Circuito" in i:
        return "Plenos Regionales"
    if "Tribunales Colegiados" in i:
        return "Tribunales Colegiados"
    if "TSJ" in i:
        return "TSJ Local"
    return i


def construir_entradas_normalizadas():
    out = []
    for e in ACERVO["entradas"]:
        ec = dict(e)
        ec["materia_principal"] = materia_canonica(e["materia"])
        ec["instancia_corta"] = instancia_corta(e["instancia"])
        out.append(ec)
    return out


def render_html():
    entradas = construir_entradas_normalizadas()
    entradas.sort(key=lambda x: (x["jerarquia"], x["materia_principal"], x["tema"]))
    md = ACERVO["metadata"]
    data_json = json.dumps(entradas, ensure_ascii=False)

    # listas únicas para los filtros
    materias = sorted({e["materia_principal"] for e in entradas})
    instancias = sorted({e["instancia_corta"] for e in entradas})
    epocas = sorted({e["epoca"] for e in entradas})
    tipos = sorted({e["tipo"] for e in entradas})
    temas = sorted({e["tema"] for e in entradas})

    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>{html.escape(md['titulo'])} — Acervo Jurisprudencial</title>
<style>
  :root {{
    --tinta: #1a1a1a;
    --tinta-suave: #444;
    --crema: #faf8f4;
    --beige: #efeae0;
    --acento: #6b1818;
    --acento-suave: #8a2424;
    --linea: #d8d2c4;
    --hit: #fff7d6;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: "Georgia", "Iowan Old Style", "Cambria", serif;
    background: radial-gradient(ellipse at top, #f7f1e3 0%, #efeae0 50%, #d8d2c4 100%);
    background-attachment: fixed;
    color: var(--tinta);
    margin: 0;
    padding: 0;
    line-height: 1.55;
    perspective: 2000px;
  }}
  main {{ transform-style: preserve-3d; }}
  header {{
    background: linear-gradient(135deg, #6b1818 0%, #8a2424 50%, #6b1818 100%);
    color: #fff;
    padding: 36px 40px 30px;
    border-bottom: 4px double #fff4;
    box-shadow: 0 10px 30px rgba(107,24,24,0.3), inset 0 -3px 6px rgba(0,0,0,0.2);
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    position: relative;
  }}
  header::after {{
    content: "";
    position: absolute;
    bottom: -8px;
    left: 0;
    right: 0;
    height: 8px;
    background: linear-gradient(to bottom, rgba(0,0,0,0.15), transparent);
    pointer-events: none;
  }}
  header h1 {{
    margin: 0 0 4px;
    font-size: 34px;
    letter-spacing: 0.5px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.4), 0 0 1px #fff;
  }}
  header p.sub {{
    margin: 0;
    color: #f6ddd2;
    font-size: 14px;
    font-style: italic;
  }}
  header p.meta {{
    margin: 10px 0 0;
    color: #f6ddd2;
    font-size: 12px;
  }}
  .controles {{
    background: var(--beige);
    padding: 18px 40px;
    border-bottom: 1px solid var(--linea);
    position: sticky;
    top: 0;
    z-index: 50;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  }}
  .fila {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
  }}
  #buscador {{
    flex: 1 1 320px;
    min-width: 260px;
    padding: 11px 14px;
    font-size: 15px;
    font-family: inherit;
    border: 1px solid var(--linea);
    border-radius: 4px;
    background: #fff;
    color: var(--tinta);
  }}
  #buscador:focus {{
    outline: 2px solid var(--acento);
    outline-offset: -1px;
  }}
  select {{
    padding: 10px 12px;
    font-size: 13px;
    font-family: inherit;
    border: 1px solid var(--linea);
    border-radius: 4px;
    background: #fff;
    color: var(--tinta);
    cursor: pointer;
    min-width: 130px;
  }}
  .contador {{
    color: var(--acento);
    font-size: 13px;
    font-weight: bold;
    margin-left: auto;
    padding: 0 8px;
  }}
  .reset {{
    padding: 10px 14px;
    background: #fff;
    border: 1px solid var(--linea);
    border-radius: 4px;
    cursor: pointer;
    font-family: inherit;
    font-size: 13px;
    color: var(--tinta-suave);
  }}
  .reset:hover {{ background: var(--beige); color: var(--acento); }}
  main {{ padding: 30px 40px 80px; max-width: 1200px; margin: 0 auto; }}
  .leyenda {{
    background: #fff;
    border-left: 3px solid var(--acento);
    padding: 14px 20px;
    margin-bottom: 28px;
    font-size: 13px;
    color: var(--tinta-suave);
    line-height: 1.6;
  }}
  .leyenda strong {{ color: var(--acento); }}
  h2.seccion {{
    font-size: 26px;
    color: var(--acento);
    border-bottom: 2px solid var(--linea);
    padding-bottom: 8px;
    margin: 40px 0 22px;
    letter-spacing: 0.3px;
    text-shadow: 1px 1px 0 #fff, 2px 2px 4px rgba(0,0,0,0.1);
    background: linear-gradient(180deg, #6b1818, #8a2424);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  h3.sub-seccion {{
    font-size: 17px;
    color: var(--tinta);
    margin: 24px 0 10px;
    border-left: 3px solid var(--acento-suave);
    padding-left: 10px;
  }}
  article.entrada {{
    background: linear-gradient(180deg, #ffffff 0%, #fdfaf3 100%);
    border: 1px solid var(--linea);
    border-radius: 10px;
    padding: 22px 26px;
    margin-bottom: 20px;
    box-shadow:
      0 1px 2px rgba(0,0,0,0.04),
      0 6px 16px rgba(0,0,0,0.06),
      0 24px 40px -20px rgba(0,0,0,0.1),
      inset 0 1px 0 #ffffff;
    transition: transform .25s cubic-bezier(.2,.7,.3,1), box-shadow .25s;
    transform-style: preserve-3d;
    will-change: transform;
  }}
  article.entrada:hover {{
    transform: translateY(-3px) rotateX(0.4deg);
    box-shadow:
      0 4px 8px rgba(0,0,0,0.05),
      0 12px 26px rgba(0,0,0,0.1),
      0 40px 60px -25px rgba(0,0,0,0.18),
      inset 0 1px 0 #ffffff;
  }}
  article.entrada.oculta {{ display: none; }}
  article.entrada.sentencia-hito {{
    background: linear-gradient(to right, #fff8e1 0%, #ffffff 30%);
    border-left: 5px solid #b8860b;
    box-shadow: 0 2px 8px rgba(184,134,11,0.15);
  }}
  article.entrada.sentencia-hito::before {{
    content: "⚖️  SENTENCIA HITO";
    display: inline-block;
    background: #b8860b;
    color: #fff;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 11px;
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 10px;
    letter-spacing: 1px;
  }}
  .btn-sjf {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--acento);
    color: #fff !important;
    padding: 10px 18px;
    border-radius: 6px;
    text-decoration: none !important;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 13px;
    font-weight: bold;
    margin: 12px 8px 4px 0;
    transition: background .15s;
    box-shadow: 0 2px 4px rgba(107,24,24,0.2);
  }}
  .btn-sjf:hover {{ background: var(--acento-suave); }}
  .btn-sjf::before {{ content: "🔗"; }}
  .btn-pdf {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #b8860b;
    color: #fff !important;
    padding: 10px 18px;
    border-radius: 6px;
    text-decoration: none !important;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 13px;
    font-weight: bold;
    margin: 12px 8px 4px 0;
    transition: background .15s;
    box-shadow: 0 2px 4px rgba(184,134,11,0.25);
  }}
  .btn-pdf:hover {{ background: #966a08; }}
  .btn-pdf::before {{ content: "📄"; }}
  .links-fila {{
    display: flex;
    flex-wrap: wrap;
    margin-top: 6px;
    padding-top: 10px;
    border-top: 1px dashed var(--linea);
  }}
  .chip-tipo {{
    background: #fff;
    color: var(--tinta-suave);
    border: 1.5px solid var(--linea);
    padding: 8px 14px;
    border-radius: 18px;
    cursor: pointer;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.3px;
    transition: all .15s;
  }}
  .chip-tipo:hover {{ border-color: var(--acento); color: var(--acento); }}
  .chip-tipo.activo {{
    background: var(--acento);
    color: #fff;
    border-color: var(--acento);
    box-shadow: 0 3px 8px rgba(107,24,24,0.25);
  }}
  .chip-tipo.sentencias-chip.activo {{
    background: #b8860b;
    border-color: #b8860b;
    box-shadow: 0 3px 8px rgba(184,134,11,0.3);
  }}
  .badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 8px;
  }}
  .badge {{
    display: inline-block;
    padding: 2px 9px;
    font-size: 11px;
    border-radius: 11px;
    background: var(--beige);
    color: var(--tinta-suave);
    border: 1px solid var(--linea);
    font-family: "Inter", -apple-system, sans-serif;
    letter-spacing: 0.2px;
  }}
  .badge.materia {{ background: #e8d5d5; color: #5a1212; border-color: #d5b8b8; }}
  .badge.jerarquia {{ background: #d8e2d5; color: #2d4a23; border-color: #b8c8b3; }}
  .badge.tipo {{ background: #d5dce8; color: #1f3358; border-color: #b3bdd5; }}
  .badge.vigencia {{ background: #f0e6d5; color: #6b4818; border-color: #d8c8a8; }}
  .badge.vigencia.alerta {{ background: #f8e0e0; color: #8b1818; border-color: #d8a8a8; }}
  .rubro {{
    font-size: 15px;
    font-weight: bold;
    margin: 6px 0 10px;
    line-height: 1.45;
    color: var(--tinta);
  }}
  .meta-loc {{
    font-size: 12px;
    color: var(--tinta-suave);
    margin-bottom: 12px;
    font-style: italic;
    border-bottom: 1px dashed var(--linea);
    padding-bottom: 8px;
  }}
  .meta-loc strong {{ font-style: normal; color: var(--tinta); }}
  .seccion-texto {{
    margin: 10px 0;
  }}
  .seccion-texto .label {{
    font-size: 11px;
    font-weight: bold;
    color: var(--acento);
    text-transform: uppercase;
    letter-spacing: 1px;
    display: block;
    margin-bottom: 3px;
    font-family: "Inter", -apple-system, sans-serif;
  }}
  .seccion-texto p {{
    margin: 0 0 8px;
    font-size: 14px;
    color: var(--tinta);
    text-align: justify;
  }}
  .etiquetas {{
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px dashed var(--linea);
  }}
  .etiquetas .tag {{
    display: inline-block;
    padding: 1px 7px;
    margin: 2px 3px 2px 0;
    font-size: 10px;
    background: var(--beige);
    color: var(--tinta-suave);
    border-radius: 3px;
    font-family: "Inter", -apple-system, sans-serif;
  }}
  mark.hit {{ background: var(--hit); padding: 0 2px; }}
  .vacio {{
    text-align: center;
    padding: 60px 20px;
    color: var(--tinta-suave);
    font-style: italic;
  }}
  footer {{
    background: var(--tinta);
    color: #aaa;
    padding: 22px 40px;
    font-size: 11px;
    text-align: center;
  }}
  footer a {{ color: #f6ddd2; text-decoration: none; }}
  .imprimir-btn {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: var(--acento);
    color: #fff;
    border: none;
    padding: 12px 18px;
    border-radius: 30px;
    cursor: pointer;
    font-family: inherit;
    font-size: 13px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    z-index: 100;
  }}
  .imprimir-btn:hover {{ background: var(--acento-suave); }}
  @media print {{
    .controles, .imprimir-btn, footer {{ display: none; }}
    article.entrada {{ break-inside: avoid; page-break-inside: avoid; box-shadow: none; }}
    header {{ background: #fff; color: #000; border-bottom: 2px solid #000; }}
    header h1, header p {{ color: #000; }}
    body {{ background: #fff; }}
  }}
</style>
</head>
<body>
<header>
  <h1>{html.escape(md['titulo'])}</h1>
  <p class="sub">{html.escape(md['subtitulo'])}</p>
  <p class="meta">Compilado: {html.escape(md['fecha_compilacion'])} · Versión {html.escape(md['version'])} · Fuente: {html.escape(md['fuente'])}</p>
</header>

<div class="controles">
  <div class="fila">
    <input id="buscador" type="search" placeholder="Buscar por texto libre: rubro, registro, palabra clave, etiqueta…" autocomplete="off">
    <span class="contador" id="contador">{len(entradas)} entradas</span>
  </div>
  <div class="fila" style="margin-top: 10px;">
    <select id="f-materia"><option value="">Todas las materias</option>{''.join(f'<option value="{html.escape(m)}">{html.escape(m)}</option>' for m in materias)}</select>
    <select id="f-tema"><option value="">Todos los temas</option>{''.join(f'<option value="{html.escape(t)}">{html.escape(t)}</option>' for t in temas)}</select>
    <select id="f-instancia"><option value="">Toda instancia</option>{''.join(f'<option value="{html.escape(i)}">{html.escape(i)}</option>' for i in instancias)}</select>
    <select id="f-epoca"><option value="">Toda época</option>{''.join(f'<option value="{html.escape(ep)}">{html.escape(ep)}</option>' for ep in epocas)}</select>
    <select id="f-tipo"><option value="">Todo tipo</option>{''.join(f'<option value="{html.escape(tp)}">{html.escape(tp)}</option>' for tp in tipos)}</select>
    <button class="reset" id="reset">Limpiar</button>
  </div>
  <div class="fila" style="margin-top: 10px;">
    <span style="font-size:12px;color:var(--tinta-suave);font-family:Inter,-apple-system,sans-serif;letter-spacing:.3px;">Filtro rápido:</span>
    <button class="chip-tipo" data-tipo="">📚 Todas</button>
    <button class="chip-tipo" data-tipo="jurisprudencia">📖 Solo jurisprudencias</button>
    <button class="chip-tipo" data-tipo="tesis aislada">📝 Solo tesis aisladas</button>
    <button class="chip-tipo sentencias-chip" data-tipo="sentencia hito">⚖️ Solo sentencias hito</button>
  </div>
</div>

<main>
  <div class="leyenda">
    <strong>Acervo curado conforme a Ley de Amparo arts. 215-230 y AG 1/2021.</strong>
    Orden jerárquico: <strong>Pleno SCJN → Salas SCJN → Plenos Regionales → Tribunales Colegiados → TSJ locales</strong>.
    Reforma 2021: los precedentes obligatorios del Pleno (8 votos) y de las Salas (4 votos) ya no requieren reiteración.
    Los registros marcados <strong>[VERIFICAR EN SJF2]</strong> requieren validación previa a cita formal en
    <a href="https://sjf2.scjn.gob.mx" target="_blank" rel="noopener">sjf2.scjn.gob.mx</a>.
    Esta compilación es apoyo de trabajo, no sustituye consulta directa al Semanario Judicial.
  </div>
  <div id="contenedor"></div>
  <div id="vacio" class="vacio" style="display:none;">Ningún criterio coincide con los filtros aplicados.</div>
</main>

<button class="imprimir-btn" onclick="window.print()">Imprimir / Guardar PDF</button>

<footer>
  Acervo Jurisprudencial NaNo · Generado por NanoLawyer (asistente jurídico mexicano) ·
  Fuente oficial: <a href="https://sjf2.scjn.gob.mx" target="_blank" rel="noopener">Semanario Judicial de la Federación</a>
</footer>

<script>
const ENTRADAS = {data_json};
const JERARQUIA_NOMBRES = {{
  1: "1. Pleno de la SCJN",
  2: "2. Salas de la SCJN",
  3: "3. Plenos Regionales",
  4: "4. Tribunales Colegiados de Circuito",
  5: "5. Tribunales Superiores de Justicia locales"
}};

const contenedor = document.getElementById("contenedor");
const buscador   = document.getElementById("buscador");
const fMateria   = document.getElementById("f-materia");
const fTema      = document.getElementById("f-tema");
const fInstancia = document.getElementById("f-instancia");
const fEpoca     = document.getElementById("f-epoca");
const fTipo      = document.getElementById("f-tipo");
const contador   = document.getElementById("contador");
const vacio      = document.getElementById("vacio");

function escape(s) {{
  if (s == null) return "";
  return String(s).replace(/[&<>"']/g, c => ({{ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;" }}[c]));
}}

function resaltar(texto, q) {{
  if (!q) return escape(texto);
  const partes = q.trim().split(/\\s+/).filter(p => p.length > 1);
  if (!partes.length) return escape(texto);
  let out = escape(texto);
  for (const p of partes) {{
    const re = new RegExp("(" + p.replace(/[.*+?^${{}}()|[\\\\]\\\\]/g, "\\\\$&") + ")", "gi");
    out = out.replace(re, "<mark class='hit'>$1</mark>");
  }}
  return out;
}}

function vigenciaBadge(v) {{
  const map = {{
    "vigente": ["vigente", "Vigente"],
    "vigente_con_matiz": ["vigente alerta", "Vigente c/ matiz"],
    "sustituida": ["vigencia alerta", "Sustituida"],
    "abandonada": ["vigencia alerta", "Abandonada"],
    "interrumpida": ["vigencia alerta", "Interrumpida"]
  }};
  const [cls, label] = map[v] || ["vigencia", v];
  return `<span class="badge ${{cls}}">${{label}}</span>`;
}}

function renderEntrada(e, q) {{
  const verifReg = e.registro_digital && e.registro_digital.includes("VERIFICAR");
  const esHito = e.tipo && e.tipo.toLowerCase().includes("sentencia");
  return `
    <article class="entrada${{esHito ? ' sentencia-hito' : ''}}" data-id="${{e.id}}">
      <div class="badges">
        <span class="badge jerarquia">${{escape(e.instancia_corta)}}</span>
        <span class="badge materia">${{escape(e.materia_principal)}}</span>
        <span class="badge tipo">${{escape(e.tipo)}}</span>
        <span class="badge">${{escape(e.epoca || "")}}</span>
        ${{vigenciaBadge(e.vigencia)}}
      </div>
      <div class="rubro">${{resaltar(e.rubro, q)}}</div>
      <div class="meta-loc">
        <strong>Tema:</strong> ${{escape(e.tema)}}${{e.subtema ? " · <strong>Subtema:</strong> " + escape(e.subtema) : ""}}<br>
        <strong>Instancia:</strong> ${{escape(e.instancia)}} ·
        <strong>Ámbito:</strong> ${{escape(e.ambito || "")}}<br>
        <strong>Registro:</strong> <span style="${{verifReg ? 'color:#8b1818;font-weight:bold;' : ''}}">${{escape(e.registro_digital)}}</span>
        ${{e.tesis_clave ? " · <strong>Tesis:</strong> " + escape(e.tesis_clave) : ""}}
        ${{e.fecha_publicacion ? " · <strong>Fecha:</strong> " + escape(e.fecha_publicacion) : ""}}
        ${{e.fuente_publicacion ? "<br><strong>Fuente:</strong> " + escape(e.fuente_publicacion) : ""}}
        ${{e.tipo_resolucion ? "<br><strong>Resolución:</strong> " + escape(e.tipo_resolucion) : ""}}
        ${{e.votacion ? " · <strong>Votación:</strong> " + escape(e.votacion) : ""}}
      </div>
      <div class="seccion-texto">
        <span class="label">Texto</span>
        <p>${{resaltar(e.texto_resumen || "", q)}}</p>
      </div>
      ${{e.trascendencia ? `<div class="seccion-texto"><span class="label">Trascendencia</span><p>${{resaltar(e.trascendencia, q)}}</p></div>` : ""}}
      ${{e.explicacion ? `<div class="seccion-texto"><span class="label">Explicación práctica</span><p>${{resaltar(e.explicacion, q)}}</p></div>` : ""}}
      <div class="links-fila">
        ${{e.url_sjf ? `<a class="btn-sjf" href="${{escape(e.url_sjf)}}" target="_blank" rel="noopener">Abrir esta tesis en el SJF</a>` : `<a class="btn-sjf" href="https://sjf2.scjn.gob.mx/busqueda-principal-tesis" target="_blank" rel="noopener">Buscar esta tesis en SJF</a>`}}
        ${{e.url_pdf_sentencia ? `<a class="btn-pdf" href="${{escape(e.url_pdf_sentencia)}}" target="_blank" rel="noopener">Descargar sentencia completa (PDF)</a>` : ""}}
      </div>
      ${{e.etiquetas && e.etiquetas.length ? `<div class="etiquetas">${{e.etiquetas.map(t => `<span class="tag">#${{escape(t)}}</span>`).join("")}}</div>` : ""}}
    </article>`;
}}

function coincide(e, q) {{
  if (!q) return true;
  const partes = q.toLowerCase().trim().split(/\\s+/).filter(p => p.length > 1);
  if (!partes.length) return true;
  const blob = [
    e.rubro, e.texto_resumen, e.trascendencia, e.explicacion,
    e.tema, e.subtema, e.materia, e.materia_principal, e.instancia,
    e.registro_digital, e.fuente_publicacion, e.tipo_resolucion,
    (e.etiquetas || []).join(" ")
  ].filter(Boolean).join(" ").toLowerCase();
  return partes.every(p => blob.includes(p));
}}

let chipTipoActivo = "";  // "" | "jurisprudencia" | "tesis aislada" | "sentencia hito"

function tipoIncluye(eTipo, target) {{
  if (!target) return true;
  if (!eTipo) return false;
  return eTipo.toLowerCase().includes(target.toLowerCase());
}}

function render() {{
  const q = buscador.value.trim();
  const fm = fMateria.value;
  const ft = fTema.value;
  const fi = fInstancia.value;
  const fe = fEpoca.value;
  const ftp = fTipo.value;

  const filtradas = ENTRADAS.filter(e =>
    coincide(e, q) &&
    (!fm || e.materia_principal === fm) &&
    (!ft || e.tema === ft) &&
    (!fi || e.instancia_corta === fi) &&
    (!fe || e.epoca === fe) &&
    (!ftp || e.tipo === ftp) &&
    tipoIncluye(e.tipo, chipTipoActivo)
  );

  // agrupar por jerarquía
  const grupos = {{}};
  for (const e of filtradas) {{
    if (!grupos[e.jerarquia]) grupos[e.jerarquia] = {{}};
    if (!grupos[e.jerarquia][e.materia_principal]) grupos[e.jerarquia][e.materia_principal] = [];
    grupos[e.jerarquia][e.materia_principal].push(e);
  }}

  let html = "";
  const niveles = Object.keys(grupos).map(Number).sort((a,b) => a-b);
  for (const n of niveles) {{
    html += `<h2 class="seccion">${{JERARQUIA_NOMBRES[n] || ("Nivel " + n)}}</h2>`;
    const mats = Object.keys(grupos[n]).sort();
    for (const m of mats) {{
      html += `<h3 class="sub-seccion">${{escape(m)}}</h3>`;
      for (const e of grupos[n][m]) {{
        html += renderEntrada(e, q);
      }}
    }}
  }}

  contenedor.innerHTML = html;
  contador.textContent = `${{filtradas.length}} de ${{ENTRADAS.length}} entradas`;
  vacio.style.display = filtradas.length === 0 ? "block" : "none";
}}

[buscador, fMateria, fTema, fInstancia, fEpoca, fTipo].forEach(el => {{
  el.addEventListener("input", render);
  el.addEventListener("change", render);
}});

function actualizarChips() {{
  document.querySelectorAll(".chip-tipo").forEach(btn => {{
    if (btn.dataset.tipo === chipTipoActivo) btn.classList.add("activo");
    else btn.classList.remove("activo");
  }});
}}

document.getElementById("reset").addEventListener("click", () => {{
  buscador.value = "";
  fMateria.value = "";
  fTema.value = "";
  fInstancia.value = "";
  fEpoca.value = "";
  fTipo.value = "";
  chipTipoActivo = "";
  actualizarChips();
  render();
}});

document.querySelectorAll(".chip-tipo").forEach(btn => {{
  btn.addEventListener("click", () => {{
    chipTipoActivo = btn.dataset.tipo;
    actualizarChips();
    render();
  }});
}});

// Estado inicial: "Todas" activo
chipTipoActivo = "";
actualizarChips();
document.querySelector('.chip-tipo[data-tipo=""]').classList.add("activo");

render();
</script>
</body>
</html>
"""
    return html_doc


if __name__ == "__main__":
    html_content = render_html()
    out = Path("/sessions/brave-bold-goodall/mnt/outputs/acervo/Acervo_Jurisprudencial.html")
    out.write_text(html_content, encoding="utf-8")
    print(f"HTML generado: {out} ({out.stat().st_size:,} bytes)")
    # index.html para GitHub Pages
    idx = Path("/sessions/brave-bold-goodall/mnt/outputs/acervo/index.html")
    idx.write_text(html_content, encoding="utf-8")
    print(f"index.html generado: {idx}")
