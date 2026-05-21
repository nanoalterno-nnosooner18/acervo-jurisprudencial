# Acervo Jurisprudencial NaNo — Guía de uso

## Qué recibiste

Tres archivos paralelos con los mismos 51 criterios curados (jurisprudencias, tesis aisladas y sentencias hito) compilados con tu plan de trabajo:

| Archivo | Para qué sirve | Cómo se abre |
|---|---|---|
| `Acervo_Jurisprudencial.html` | Buscador real con filtros — el formato más útil para consulta diaria | Doble clic; se abre en navegador |
| `Acervo_Jurisprudencial.docx` | Lectura corrida, impresión, archivo del foro | Word, Pages, LibreOffice |
| `Acervo_Jurisprudencial.xlsx` | Mini base de datos con autofiltros por columna | Excel, Numbers, LibreOffice Calc |

## Estructura jerárquica

Conforme a los arts. 215–230 de la Ley de Amparo y al Acuerdo General 1/2021 del Pleno SCJN, el acervo se ordena en cinco niveles descendentes:

1. Pleno de la SCJN
2. Salas de la SCJN (Primera y Segunda)
3. Plenos Regionales (antes Plenos de Circuito)
4. Tribunales Colegiados de Circuito
5. Tribunales Superiores de Justicia locales (CDMX, Edomex)

Reforma 2021: los precedentes obligatorios del Pleno (≥8 votos) y de las Salas (≥4 votos) ya no requieren reiteración.

## Cómo usar el HTML (recomendado)

- **Buscador**: escribe cualquier palabra clave (rubro, registro, etiqueta, concepto). Se buscan TODOS los términos en TODOS los campos.
- **Filtros**: combinables — materia, tema, instancia, época, tipo. Limpia con el botón "Limpiar".
- **Marcado dinámico**: las coincidencias se resaltan en amarillo dentro del rubro y de la explicación.
- **Imprimir**: botón flotante abajo a la derecha. Genera PDF imprimible respetando saltos de página por entrada.
- **Conserva privacidad**: el HTML no envía nada a internet; funciona offline.

## Cómo usar el Excel

- **Hoja "Índice"**: portada con estadística por materia y por jerarquía.
- **Hoja "Acervo (maestra)"**: las 51 entradas con autofiltros (flechas en cada encabezado). Filtra por cualquier columna. Las dos primeras columnas (ID y Nivel) están congeladas.
- **Hojas por materia**: subconjuntos pre-filtrados por materia para impresión por área.
- **Registros marcados [VERIFICAR EN SJF2]**: aparecen en rojo. Son los que requieren validar el número exacto antes de cita formal.

## Cómo usar el Word

- Portada + Índice jerárquico navegable + cuerpo completo.
- Cada entrada está en una tabla autocontenida para que no se parta entre páginas.
- Apto para imprimir y archivar como referencia del despacho.

## Materias y temas incluidos (versión 1.0)

- **Civil**: usucapión/prescripción positiva, juicio hipotecario, contratos civiles (teoría general), arrendamiento, fideicomisos, urbanización y desarrollo urbano, extinción de dominio, agua y servicios públicos
- **Civil — Condominio**: cuotas condominales, asambleas
- **Mercantil**: juicio ejecutivo, títulos de crédito, concursos, sociedades, contratos
- **Penal**: sistema acusatorio, prisión preventiva oficiosa (post-CIDH), prueba ilícita, cadena de custodia
- **Fiscal**: caducidad, devolución de saldos, art. 69-B CFF (operaciones inexistentes)
- **Laboral**: reforma 2019 (Tribunales Laborales), despido injustificado, subcontratación reforma 2021 (REPSE)
- **Administrativo**: nulidad por falta de fundamentación, responsabilidad administrativa (LGRA)
- **Amparo**: interés legítimo, suspensión y apariencia del buen derecho, precedentes obligatorios reforma 2021
- **Sentencias hito SCJN**: Radilla (control difuso de convencionalidad), matrimonio igualitario, cannabis lúdico, despenalización del aborto, PPO y CIDH, compensación por trabajo doméstico, consulta indígena

## Cómo seguir ampliando el acervo

Esta es la **versión 1.0**. Para crecerla:

1. Dime: "agrega 10 jurisprudencias más de [materia/tema]" — yo edito el archivo `acervo_dataset.py` y regenero los tres formatos automáticamente.
2. Si traes una jurisprudencia específica que quieras incorporar (rubro o registro), también la integro.
3. Cuando habilites egreso a `sjf2.scjn.gob.mx` en Cowork → Settings → Capabilities, podemos validar masivamente los registros marcados [VERIFICAR EN SJF2].

## Integración con NotebookLM (opcional)

Si quieres una **capa conversacional semántica** encima del acervo:

1. Ve a [notebooklm.google.com](https://notebooklm.google.com) (necesita cuenta Google).
2. Crea un nuevo notebook.
3. Sube como fuente el archivo **`Acervo_Jurisprudencial.docx`** (NotebookLM digiere mejor los .docx que los HTML).
4. Podrás hacer preguntas tipo "¿qué jurisprudencias hay sobre tácita reconducción?" o "compara las defensas en juicio ejecutivo mercantil vs. especial hipotecario" y NotebookLM responde citando las entradas exactas del acervo.

No necesitas cuenta nueva ni configuración especial. Es complementario al buscador del HTML, no lo sustituye.

## Salvaguardas profesionales

- Las explicaciones prácticas son apoyo de trabajo; toda cita formal debe verificarse en el SJF2 antes de presentarse en juicio.
- Los registros marcados `[VERIFICAR EN SJF2]` son rubros que conozco con certeza pero cuyo número de registro digital exacto debe confirmarse en el portal oficial. Esta es la práctica que se exige en cualquier despacho serio.
- Esta compilación NO sustituye lectura íntegra del precedente cuando se cita en un escrito formal — la "razón fundante" del precedente importa más que el rubro.

## Próximas sesiones — sugerencias

Para ir denso por materia, lo recomendable es:

- Sesión 2: profundizar materia civil (usucapión + arrendamiento + contratos: pasar de 14 a 40 entradas)
- Sesión 3: profundizar penal (PPO post-CIDH, sistema acusatorio, garantías) y amparo
- Sesión 4: completar fiscal (CFF, LFPCA, jurisprudencias de la 2ª Sala) y laboral (juicios orales, Tribunales Laborales)
- Sesión 5: amparo procesal (suspensión, ejecución, recursos)

Dime cuándo quieres avanzar con cada uno.

—

**Acervo Jurisprudencial NaNo** · Compilado por NanoLawyer (asistente jurídico mexicano) · Versión 1.0 · 2026-05-18
