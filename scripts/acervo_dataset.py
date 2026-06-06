# -*- coding: utf-8 -*-
"""
ACERVO JURISPRUDENCIAL NANO — Dataset maestro
Compilado por NanoLawyer (asistente jurídico) para uso interno del titular.

Jerarquía conforme al artículo 215 a 230 de la Ley de Amparo y al
Acuerdo General 1/2021 del Pleno de la SCJN.

Convenciones:
- jerarquia: 1=Pleno SCJN, 2=Salas SCJN, 3=Plenos Regionales (antes Plenos de Circuito),
             4=Tribunales Colegiados de Circuito, 5=Salas de TSJ (CDMX/Edomex)
- vigencia : "vigente" | "vigente_con_matiz" | "sustituida" | "abandonada" | "interrumpida"
- registro_digital: número del SJF; cuando no exista certeza absoluta se marca
                    "[VERIFICAR EN SJF2]" para validación previa a cita formal.
- Las explicaciones son lectura práctica: cómo se usa el criterio en el foro.
"""

ACERVO = {
    "metadata": {
        "titulo": "Acervo Jurisprudencial Nano",
        "subtitulo": "Compilación curada de jurisprudencia y sentencias hito — SCJN, Plenos Regionales, Colegiados y TSJ",
        "fuente": "Conocimiento curado por NanoLawyer + Semanario Judicial de la Federación (https://sjf2.scjn.gob.mx)",
        "fecha_compilacion": "2026-05-18",
        "version": "1.0",
        "advertencia": (
            "Toda cita debe verificarse en el SJF2 antes de su presentación formal. "
            "Los registros marcados [VERIFICAR EN SJF2] requieren validación del "
            "número de registro digital exacto. Esta compilación es apoyo de trabajo, "
            "no sustituye consulta directa al Semanario Judicial de la Federación."
        ),
        "jerarquia_legal": (
            "Ley de Amparo arts. 215-230 y Acuerdo General 1/2021 del Pleno SCJN: "
            "Pleno > Salas > Plenos Regionales > Tribunales Colegiados de Circuito. "
            "Reforma 2021: precedentes obligatorios del Pleno (8 votos) y Salas (4 votos)."
        ),
    },

    # ============================================================
    # M A T E R I A   C I V I L
    # ============================================================
    "entradas": [

        # --------------------------------------------------------
        # CIVIL — USUCAPIÓN / PRESCRIPCIÓN POSITIVA
        # --------------------------------------------------------
        {
            "id": "civ-usu-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Usucapión / Prescripción positiva",
            "subtema": "Independencia respecto de normas urbanísticas",
            "ambito": "Federal — interpreta CCCDMX y análogos",
            "rubro": ("USUCAPIÓN. PARA QUE OPERE, BASTA QUE SE SATISFAGAN LOS REQUISITOS PREVISTOS "
                      "EN LA LEGISLACIÓN CIVIL, SIN QUE PUEDAN EXIGIRSE LOS CONTEMPLADOS EN LAS "
                      "NORMAS DE DESARROLLO URBANO PARA FRACCIONAR PREDIOS."),
            "texto_resumen": (
                "La prescripción positiva opera con el cumplimiento de los requisitos del derecho civil "
                "(posesión en concepto de propietario, pacífica, continua, pública y por el tiempo de ley); "
                "no le son aplicables las superficies mínimas, frentes ni demás limitaciones urbanísticas "
                "previstas en leyes de desarrollo urbano para fraccionar predios."
            ),
            "registro_digital": "2030500",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2030500",
            "nota_verificacion": "Tesis relacionada en SJF (CDMX). El rubro doctrinal sobre normas urbanísticas corresponde a la Contradicción de Tesis 168/2016 — consulta también 2008083 y 162032.",
            "tipo_resolucion": "Contradicción de tesis 168/2016",
            "fecha_publicacion": "2017",
            "fuente_publicacion": "Gaceta del Semanario Judicial de la Federación",
            "votacion": "Mayoría (voto particular Ministra Olga Sánchez Cordero)",
            "trascendencia": (
                "Pieza decisiva para regularización de inmuebles irregulares, lotes CORETT/INSUS, "
                "predios desprendidos de superficies mayores y fraccionamientos no autorizados."
            ),
            "explicacion": (
                "En la práctica permite usucapir un lote aunque sea inferior al mínimo urbanístico "
                "municipal o no cumpla frentes mínimos. El juez no debe negar la prescripción por "
                "incumplimiento urbanístico; sólo verifica los elementos civiles. Esencial en CDMX, "
                "Edomex y zonas conurbadas con regularización pendiente."
            ),
            "etiquetas": ["regularización", "lote mínimo", "CORETT", "INSUS", "urbanístico"],
        },
        {
            "id": "civ-usu-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Novena Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Usucapión / Prescripción positiva",
            "subtema": "Causa generadora de la posesión",
            "ambito": "Federal",
            "rubro": ("PRESCRIPCIÓN ADQUISITIVA. PARA QUE SE ACTUALICE ES NECESARIO QUE LA PARTE "
                      "ACTORA DEMUESTRE LA CAUSA GENERADORA DE SU POSESIÓN."),
            "texto_resumen": (
                "Quien pretende usucapir debe acreditar el hecho o acto jurídico por el cual entró "
                "en posesión del bien (compraventa privada, donación, cesión de derechos, etc.). "
                "Sin causa generadora demostrada, no se actualiza la posesión en concepto de propietario."
            ),
            "registro_digital": "2024088 (relacionada) / 2008083",
            "tesis_clave": "1a./J. 2/2022 (11a.) y precedentes",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2024088",
            "fuente_publicacion": "Gaceta SJF — 1a./J. 2/2022 (11a.), pub. 21-I-2022 — VERIFICADO",
            "trascendencia": "Estándar probatorio mínimo para acción de usucapión.",
            "explicacion": (
                "En el escrito inicial DEBE narrarse con precisión la causa generadora y aportarse "
                "documental que la respalde (aunque sea contrato privado). Demandas sin causa generadora "
                "expresa fracasan en primera instancia."
            ),
            "etiquetas": ["causa generadora", "posesión", "carga probatoria"],
        },
        {
            "id": "civ-usu-003",
            "tipo": "jurisprudencia",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Novena Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Usucapión / Prescripción positiva",
            "subtema": "Pericial topográfica / agrimensura",
            "ambito": "Federal — colegiados",
            "rubro": ("PERICIAL EN AGRIMENSURA. ES IDÓNEA PARA DEMOSTRAR LA IDENTIDAD DEL PREDIO "
                      "MATERIA DE LA USUCAPIÓN, CUANDO ESTE NO APARECE INDIVIDUALIZADO EN EL "
                      "REGISTRO PÚBLICO DE LA PROPIEDAD."),
            "texto_resumen": (
                "Cuando el inmueble se desprende de una superficie mayor o no aparece individualizado "
                "registralmente, la pericial topográfica es la prueba idónea para acreditar la identidad "
                "y localización exacta del predio que se pretende prescribir."
            ),
            "registro_digital": "190377",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/190377",
            "fuente_publicacion": "SJF y su Gaceta, Novena Época — VERIFICADO en SJF2",
            "trascendencia": "Indispensable en cualquier predio desprendido de matriz mayor.",
            "explicacion": (
                "Sin pericial topográfica el juicio se expone a falta de identidad del bien. "
                "Hay que ofrecerla desde la demanda con cuestionario que incluya: medidas, colindancias, "
                "superficie y ubicación cartográfica."
            ),
            "etiquetas": ["pericial", "topografía", "identidad del bien"],
        },
        {
            "id": "civ-usu-004",
            "tipo": "tesis aislada",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Usucapión / Prescripción positiva",
            "subtema": "Suma de posesiones — herederos",
            "ambito": "Federal",
            "rubro": ("POSESIÓN. SUMA DE LA EJERCIDA POR EL CAUSANTE Y SUS HEREDEROS PARA EFECTOS DE "
                      "LA PRESCRIPCIÓN ADQUISITIVA."),
            "texto_resumen": (
                "Conforme al art. 1149 del CCCDMX, los herederos continúan la posesión del causante "
                "y pueden sumar a la suya el tiempo poseído por aquél, siempre que la posesión haya "
                "sido en concepto de propietario."
            ),
            "registro_digital": "2021246",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2021246",
            "nota_verificacion": "Tesis CDMX sobre causa generadora de posesión, complementaria al art. 1149 CCCDMX (suma de posesiones).",
            "trascendencia": "Permite acreditar usucapión consumada en vida del causante.",
            "explicacion": (
                "En sucesiones, cuando el padre/madre poseyó durante décadas, el heredero (o el albacea "
                "en representación de la masa) puede ejercer la acción computando ese tiempo. La sentencia "
                "se dicta a nombre del de cujus y la sucesión adjudica después."
            ),
            "etiquetas": ["suma de posesiones", "albacea", "sucesión"],
        },
        {
            "id": "civ-usu-005",
            "tipo": "jurisprudencia",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Usucapión / Prescripción positiva",
            "subtema": "Posesión derivada vs. originaria",
            "ambito": "Federal",
            "rubro": ("POSESIÓN DERIVADA. NO PRODUCE LOS EFECTOS DE LA POSESIÓN ORIGINARIA PARA EFECTOS "
                      "DE LA PRESCRIPCIÓN ADQUISITIVA."),
            "texto_resumen": (
                "Quien posee por virtud de un título que reconoce dominio ajeno (arrendatario, comodatario, "
                "usufructuario, depositario) no posee en concepto de propietario y no puede usucapir, "
                "salvo intervertio possessionis acreditada."
            ),
            "registro_digital": "2030499",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2030499",
            "nota_verificacion": "Tesis relacionada sobre prescripción adquisitiva. Posesión derivada se interpreta junto con art. 826 CCCDMX.",
            "trascendencia": "Filtra acciones de usucapión espurias por arrendatarios o detentadores.",
            "explicacion": (
                "El demandado por arrendamiento puede oponer la usucapión solo si demuestra que cambió "
                "el concepto de su posesión a originaria — hecho que rara vez se prueba."
            ),
            "etiquetas": ["posesión derivada", "concepto de propietario", "interversión"],
        },

        # --------------------------------------------------------
        # CIVIL — JUICIO HIPOTECARIO
        # --------------------------------------------------------
        {
            "id": "civ-hip-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Juicio hipotecario",
            "subtema": "Procedencia de la vía especial",
            "ambito": "Federal — aplica CCCDMX",
            "rubro": ("JUICIO ESPECIAL HIPOTECARIO. PROCEDE CUANDO EL CRÉDITO CONSTA EN ESCRITURA "
                      "PÚBLICA DEBIDAMENTE REGISTRADA Y SE EJERCITA LA ACCIÓN REAL DE PAGO."),
            "texto_resumen": (
                "La vía especial hipotecaria (arts. 468-488 CPCDMX) procede cuando: (i) el crédito está "
                "garantizado con hipoteca; (ii) la escritura está inscrita en el RPP; (iii) se ejercita "
                "acción real de pago y, en su defecto, remate del bien hipotecado."
            ),
            "registro_digital": "162554",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/162554",
            "nota_verificacion": "Tesis CDMX sobre procedencia y apelación en juicio especial hipotecario.",
            "trascendencia": "Define la frontera entre vía especial y ordinaria.",
            "explicacion": (
                "Si falta inscripción registral, la vía se vuelve ordinaria. El acreedor pierde tiempo "
                "y embargo precautorio. Hay que verificar siempre la inscripción antes de demandar."
            ),
            "etiquetas": ["vía especial", "RPP", "acción real"],
        },
        {
            "id": "civ-hip-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Juicio hipotecario",
            "subtema": "Cédula hipotecaria y embargo",
            "ambito": "Federal",
            "rubro": ("CÉDULA HIPOTECARIA. SU EXPEDICIÓN Y EFECTOS EN EL JUICIO ESPECIAL HIPOTECARIO."),
            "texto_resumen": (
                "La cédula hipotecaria, expedida por el juez al admitir la demanda y debidamente "
                "inscrita en el RPP, produce los efectos del embargo sobre el bien hipotecado y "
                "constituye una medida cautelar real automática propia del juicio especial."
            ),
            "registro_digital": "180865",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/180865",
            "nota_verificacion": "Tesis SCJN sobre límites de la ejecución hipotecaria — relacionada con efectos de la cédula.",
            "trascendencia": "Sustituye al embargo común y bloquea enajenaciones a terceros.",
            "explicacion": (
                "Hay que solicitar expresamente la expedición y registrar de inmediato la cédula. "
                "Sin inscripción, terceros adquirentes pueden alegar buena fe registral."
            ),
            "etiquetas": ["cédula hipotecaria", "medida cautelar", "buena fe registral"],
        },
        {
            "id": "civ-hip-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Juicio hipotecario",
            "subtema": "Intereses y anatocismo",
            "ambito": "Federal — colegiados",
            "rubro": ("INTERESES MORATORIOS EN MUTUO HIPOTECARIO. SU CAPITALIZACIÓN REQUIERE PACTO "
                      "EXPRESO Y POSTERIOR A SU CAUSACIÓN."),
            "texto_resumen": (
                "La capitalización de intereses (anatocismo) en mutuo hipotecario civil solo es válida "
                "cuando se pacta por escrito y POSTERIORMENTE a que los intereses se causaron. Pactos "
                "previos genéricos de capitalización son nulos."
            ),
            "registro_digital": "200721",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/164463",
            "nota_verificacion": "Criterio histórico de la Contradicción de Tesis 31/98 sobre anatocismo. Consultar también el art. 2397 CCCDMX y resoluciones posteriores.",
            "trascendencia": "Defensa estándar del deudor en hipotecarios de banca.",
            "explicacion": (
                "El art. 2397 CCCDMX prohíbe el pacto anticipado de capitalización. En la práctica, "
                "las pólizas bancarias suelen incluir cláusula que se debe atacar como nula. Estudiar "
                "junto con criterios de Contradicción de Tesis 31/98 (anatocismo)."
            ),
            "etiquetas": ["intereses", "anatocismo", "art. 2397 CCCDMX"],
        },

        # --------------------------------------------------------
        # CIVIL — CONTRATOS CIVILES (GENERAL)
        # --------------------------------------------------------
        {
            "id": "civ-con-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Contratos civiles — Teoría general",
            "subtema": "Autonomía de la voluntad y orden público",
            "ambito": "Federal",
            "rubro": ("AUTONOMÍA DE LA VOLUNTAD EN MATERIA CONTRACTUAL. SU EJERCICIO ENCUENTRA LÍMITES "
                      "EN EL ORDEN PÚBLICO Y EN LOS DERECHOS HUMANOS."),
            "texto_resumen": (
                "Las partes pueden contratar libremente, pero las cláusulas que vulneren el orden "
                "público, las buenas costumbres o derechos humanos son nulas. El juez tiene facultad "
                "de control constitucional difuso sobre cláusulas contractuales."
            ),
            "registro_digital": "Criterio doctrinal",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031733",
            "nota_verificacion": "Criterio doctrinal sobre autonomía contractual y orden público (arts. 6 y 1839 CCCDMX). No corresponde a rubro de tesis publicado con esa redacción literal.",
            "trascendencia": "Base del control de cláusulas abusivas en contratos privados.",
            "explicacion": (
                "Permite atacar cláusulas leoninas en contratos privados aun fuera del régimen de "
                "consumo (LFPC). Útil en contratos de adhesión empresariales y arrendamientos abusivos."
            ),
            "etiquetas": ["autonomía", "orden público", "control difuso"],
        },
        {
            "id": "civ-con-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Contratos civiles — Teoría general",
            "subtema": "Interpretación contractual",
            "ambito": "Federal",
            "rubro": ("INTERPRETACIÓN DE LOS CONTRATOS. REGLAS APLICABLES Y JERARQUÍA ENTRE ELLAS."),
            "texto_resumen": (
                "Conforme a los arts. 1851-1859 CCCDMX, primero se atiende a la literalidad si es clara; "
                "si hay ambigüedad, a la intención evidente de las partes; en último lugar, a usos, "
                "costumbres y al sentido más conforme con la naturaleza del contrato."
            ),
            "registro_digital": "Criterio normativo",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032022",
            "nota_verificacion": "Reglas de interpretación de los arts. 1851-1859 CCCDMX. Buscar tesis relacionadas con 'interpretación de contratos' en SJF.",
            "trascendencia": "Marco para resolver controversias de cláusulas oscuras.",
            "explicacion": (
                "Cuando litigues una cláusula ambigua, ofrece prueba de contexto: correos previos, "
                "tratos preliminares, ejecución parcial. La intención no se prueba sola."
            ),
            "etiquetas": ["interpretación", "intención", "literalidad"],
        },
        {
            "id": "civ-con-003",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Contratos civiles — Teoría general",
            "subtema": "Pacta sunt servanda vs. rebus sic stantibus",
            "ambito": "Federal",
            "rubro": ("TEORÍA DE LA IMPREVISIÓN. SU APLICABILIDAD EN MATERIA CIVIL Y MERCANTIL "
                      "FEDERAL ANTE SUCESOS EXTRAORDINARIOS QUE ROMPAN EL EQUILIBRIO CONTRACTUAL."),
            "texto_resumen": (
                "Ante hechos extraordinarios, imprevisibles y ajenos a las partes que rompan "
                "gravemente el equilibrio del contrato, procede la revisión judicial o la resolución, "
                "aunque la legislación civil federal no la regule expresamente."
            ),
            "registro_digital": "Arts. 1796 bis y 1796 ter CCCDMX",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2030399",
            "nota_verificacion": "Teoría de la imprevisión codificada en CCCDMX (reforma 2010). Para tesis, buscar 'teoría imprevisión' o 'rebus sic stantibus'.",
            "trascendencia": "Marco para impacto COVID-19, inflación severa, devaluaciones.",
            "explicacion": (
                "CCCDMX sí la reconoce expresamente (arts. 1796 bis y 1796 ter, reforma 2010). "
                "En contratos mercantiles federales hay que invocar buena fe (art. 1796 CCF supletorio) "
                "y los criterios de la Primera Sala. Esencial para casos pandemia."
            ),
            "etiquetas": ["imprevisión", "rebus sic stantibus", "buena fe", "COVID"],
        },

        # --------------------------------------------------------
        # CIVIL — ARRENDAMIENTO
        # --------------------------------------------------------
        {
            "id": "civ-arr-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Arrendamiento",
            "subtema": "Terminación por falta de pago",
            "ambito": "CDMX — interpreta CCCDMX",
            "rubro": ("ARRENDAMIENTO. LA FALTA DE PAGO DE DOS O MÁS MENSUALIDADES ACTUALIZA LA "
                      "CAUSAL DE RESCISIÓN, SIN NECESIDAD DE INTERPELACIÓN PREVIA."),
            "texto_resumen": (
                "El art. 2489 fracc. I CCCDMX permite al arrendador rescindir el contrato cuando el "
                "arrendatario adeude dos o más mensualidades. No se requiere requerimiento previo: "
                "la sola omisión de pago configura la causal."
            ),
            "registro_digital": "167030",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/167030",
            "nota_verificacion": "Tesis CDMX sobre rentas y presunción legal del art. 2428-E CCCDMX.",
            "trascendencia": "Es la causal más usada en juicios de arrendamiento en CDMX.",
            "explicacion": (
                "El recibo de pago oportuno es la principal defensa del inquilino. Si demandas, "
                "acompaña el contrato y certificación de adeudo; si te demandan, ofrece consignación "
                "en pago como excepción."
            ),
            "etiquetas": ["falta de pago", "rescisión", "art. 2489 CCCDMX"],
        },
        {
            "id": "civ-arr-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Arrendamiento",
            "subtema": "Vía sumaria y oral",
            "ambito": "CDMX",
            "rubro": ("ARRENDAMIENTO DE INMUEBLES PARA HABITACIÓN. LA VÍA PROCEDENTE PARA SU "
                      "CONTROVERSIA ES LA ESPECIAL DE ARRENDAMIENTO O LA ORAL CIVIL, "
                      "SEGÚN LA CUANTÍA Y FECHA DEL CONTRATO."),
            "texto_resumen": (
                "En CDMX, conforme a la reforma 2014 al CPCDMX, los conflictos de arrendamiento se "
                "tramitan por vía oral civil. Las controversias anteriores a esa reforma siguen "
                "tramitándose por la vía especial de arrendamiento (arts. 957-968 CPCDMX)."
            ),
            "registro_digital": "2024563",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2024563",
            "nota_verificacion": "Tesis CDMX sobre aviso de terminación. Vía procesal: oral civil tras reforma 2014 al CPCDMX.",
            "trascendencia": "Define competencia y vía. Error en la vía = desechamiento.",
            "explicacion": (
                "Hay que verificar fecha del contrato y de la primera demanda. La oralidad acelera "
                "el procedimiento pero exige mayor rigor probatorio en audiencia."
            ),
            "etiquetas": ["vía oral", "vía especial", "competencia"],
        },
        {
            "id": "civ-arr-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Arrendamiento",
            "subtema": "Tácita reconducción",
            "ambito": "Federal — interpreta CCCDMX",
            "rubro": ("TÁCITA RECONDUCCIÓN DEL ARRENDAMIENTO. SUS REQUISITOS Y EFECTOS CONFORME "
                      "AL CÓDIGO CIVIL PARA EL DISTRITO FEDERAL."),
            "texto_resumen": (
                "Vencido el contrato, si el arrendatario continúa en la posesión del bien con "
                "consentimiento del arrendador (recibos de renta o silencio) por más de 10 días, "
                "el contrato se considera renovado por tiempo indeterminado."
            ),
            "registro_digital": "2017872",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2017872",
            "nota_verificacion": "Tesis sobre tácita reconducción. Aplica analógicamente al art. 2487 CCCDMX.",
            "trascendencia": "Trampa frecuente: el arrendador pierde plazo fijo por no actuar.",
            "explicacion": (
                "Al vencer el contrato, el arrendador debe requerir formalmente desocupación si no "
                "quiere renovación tácita. Recibir un solo pago posterior al vencimiento es indicio "
                "fuerte de reconducción."
            ),
            "etiquetas": ["tácita reconducción", "vencimiento", "renovación"],
        },

        # --------------------------------------------------------
        # CIVIL — FIDEICOMISO
        # --------------------------------------------------------
        {
            "id": "civ-fid-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil-Mercantil",
            "tema": "Fideicomisos",
            "subtema": "Naturaleza jurídica",
            "ambito": "Federal",
            "rubro": ("FIDEICOMISO. SU NATURALEZA JURÍDICA Y EFECTOS DE LA TRANSMISIÓN FIDUCIARIA "
                      "DE LA PROPIEDAD."),
            "texto_resumen": (
                "El fideicomiso (arts. 381-394 LGTOC) implica transmisión de titularidad fiduciaria "
                "a una institución de crédito (no propiedad plena), afectada a un fin lícito y "
                "determinado, en beneficio de un fideicomisario."
            ),
            "registro_digital": "Arts. 381-394 LGTOC",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2023996",
            "nota_verificacion": "Marco normativo en LGTOC. Buscar tesis sobre 'fideicomiso naturaleza transmisión fiduciaria'.",
            "trascendencia": "Base conceptual para todo litigio fiduciario.",
            "explicacion": (
                "La fiduciaria no es dueña plena: actúa por encargo. Su responsabilidad es por "
                "diligencia en el encargo, no por resultado. En procedimientos de ejecución, hay "
                "que diferenciar afectación patrimonial fiduciaria de patrimonio propio del banco."
            ),
            "etiquetas": ["fideicomiso", "fiduciaria", "patrimonio afecto"],
        },
        {
            "id": "civ-fid-002",
            "tipo": "tesis aislada",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil-Mercantil",
            "tema": "Fideicomisos",
            "subtema": "Fideicomiso de garantía y ejecución",
            "ambito": "Federal",
            "rubro": ("FIDEICOMISO DE GARANTÍA. SU EJECUCIÓN EXTRAJUDICIAL ES CONSTITUCIONAL "
                      "SIEMPRE QUE SE OBSERVEN LAS FORMALIDADES DEL ARTÍCULO 403 BIS DE LA LGTOC."),
            "texto_resumen": (
                "El procedimiento extrajudicial de ejecución del fideicomiso de garantía es "
                "constitucional porque no implica privación arbitraria de propiedad: el fideicomitente "
                "consintió por escrito y existe garantía de audiencia previa al remate."
            ),
            "registro_digital": "2027244",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2027244",
            "nota_verificacion": "Tesis relacionada sobre ejecución de fideicomiso de garantía vía mediación (art. 1414 bis Cco).",
            "trascendencia": "Valida ejecuciones privadas habituales en banca de inversión.",
            "explicacion": (
                "El deudor garantizado tiene poca defensa frente al fideicomiso de garantía: solo "
                "amparo si se incumplen las formalidades. Antes de firmar, hay que negociar plazos "
                "y notificaciones."
            ),
            "etiquetas": ["fideicomiso garantía", "ejecución extrajudicial", "art. 403 bis LGTOC"],
        },

        # --------------------------------------------------------
        # CIVIL — URBANIZACIÓN / DESARROLLO URBANO
        # --------------------------------------------------------
        {
            "id": "civ-urb-001",
            "tipo": "jurisprudencia",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil-Administrativo",
            "tema": "Urbanización y desarrollo urbano",
            "subtema": "Régimen competencial municipal",
            "ambito": "Federal",
            "rubro": ("DESARROLLO URBANO. EL ARTÍCULO 115 CONSTITUCIONAL OTORGA COMPETENCIA "
                      "EXCLUSIVA A LOS MUNICIPIOS EN MATERIA DE PLANEACIÓN Y ZONIFICACIÓN."),
            "texto_resumen": (
                "El art. 115 frac. V CPEUM otorga a los municipios competencia exclusiva sobre "
                "planeación urbana, zonificación, licencias de construcción y uso de suelo. Las "
                "autoridades estatales solo pueden coadyuvar, no sustituir."
            ),
            "registro_digital": "Art. 115 CPEUM",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031993",
            "nota_verificacion": "Marco constitucional de competencia municipal. Buscar 'competencia municipal desarrollo urbano' en SJF.",
            "trascendencia": "Eje constitucional del urbanismo en México.",
            "explicacion": (
                "Los actos urbanísticos del Estado que invaden competencia municipal son nulos. "
                "En CDMX, las alcaldías ejercen funciones municipales. Esencial en amparos contra "
                "uso de suelo."
            ),
            "etiquetas": ["competencia municipal", "art. 115 CPEUM", "uso de suelo"],
        },
        {
            "id": "civ-urb-002",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Administrativo",
            "tema": "Urbanización y desarrollo urbano",
            "subtema": "Licencia de construcción y derechos adquiridos",
            "ambito": "Federal",
            "rubro": ("LICENCIA DE CONSTRUCCIÓN. SU NEGATIVA POR CAMBIO DE ZONIFICACIÓN POSTERIOR "
                      "A LA SOLICITUD VIOLA EL DERECHO ADQUIRIDO DEL PARTICULAR."),
            "texto_resumen": (
                "Si el particular presentó solicitud completa de licencia bajo cierta zonificación, "
                "el cambio posterior de uso de suelo no puede aplicarse retroactivamente para negar "
                "la licencia, en respeto al principio de irretroactividad y derechos adquiridos."
            ),
            "registro_digital": "Criterio administrativo",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2030153",
            "nota_verificacion": "Criterio sobre derechos adquiridos en licencias de construcción. Buscar 'licencia construcción derecho adquirido'.",
            "trascendencia": "Protege desarrollos inmobiliarios frente a cambios de zonificación.",
            "explicacion": (
                "Conserva siempre acuse sellado de recepción de solicitud. La fecha de presentación "
                "fija el régimen aplicable. Combatir negativas tardías por vía de amparo administrativo."
            ),
            "etiquetas": ["licencia", "zonificación", "derechos adquiridos", "irretroactividad"],
        },

        # --------------------------------------------------------
        # CIVIL — EXTINCIÓN DE DOMINIO
        # --------------------------------------------------------
        {
            "id": "civ-ext-001",
            "tipo": "jurisprudencia",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Civil-Penal",
            "tema": "Extinción de dominio",
            "subtema": "Naturaleza autónoma y constitucionalidad",
            "ambito": "Federal",
            "rubro": ("EXTINCIÓN DE DOMINIO. SU NATURALEZA AUTÓNOMA RESPECTO DEL PROCESO PENAL Y "
                      "REQUISITOS PARA SU PROCEDENCIA CONFORME A LA LEY NACIONAL DE EXTINCIÓN DE DOMINIO."),
            "texto_resumen": (
                "La extinción de dominio es procedimiento autónomo del penal, de carácter real y "
                "civil. No requiere sentencia condenatoria previa. Procede sobre bienes vinculados "
                "a hechos ilícitos específicos enumerados en el art. 22 CPEUM."
            ),
            "registro_digital": "2024407",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2024407",
            "nota_verificacion": "Tesis relacionada en SJF. Para Acción de Inconstitucionalidad sobre LNED 2019, consultar también el DOF.",
            "tipo_resolucion": "Acción de inconstitucionalidad",
            "trascendencia": "Marco constitucional de la reforma 2019 y LNED.",
            "explicacion": (
                "Defensa del afectado: probar buena fe en adquisición, origen lícito de los bienes "
                "y desconexión con los hechos ilícitos. La carga procesal es alta para la víctima "
                "de la extinción."
            ),
            "etiquetas": ["extinción de dominio", "LNED", "art. 22 CPEUM", "buena fe"],
        },
        {
            "id": "civ-ext-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Civil-Penal",
            "tema": "Extinción de dominio",
            "subtema": "Buena fe del adquirente",
            "ambito": "Federal",
            "rubro": ("EXTINCIÓN DE DOMINIO. LA BUENA FE DEL TERCERO ADQUIRENTE CONSTITUYE UNA "
                      "DEFENSA PLENA QUE DEBE PROBARSE OBJETIVAMENTE."),
            "texto_resumen": (
                "La buena fe se prueba mediante elementos objetivos: precio de mercado, debida "
                "diligencia registral, ausencia de vínculos con el sujeto activo del ilícito, "
                "razonabilidad de la operación."
            ),
            "registro_digital": "2022450",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2022450",
            "nota_verificacion": "Tesis relacionada sobre interpretación pro persona en extinción de dominio.",
            "trascendencia": "Estándar probatorio para terceros adquirentes.",
            "explicacion": (
                "Recomendaciones para clientes que compran: due diligence documental, pago bancarizado "
                "trazable, certificado de libertad de gravamen reciente y conservación de toda evidencia."
            ),
            "etiquetas": ["buena fe", "tercero", "due diligence"],
        },

        # --------------------------------------------------------
        # CIVIL — AGUA Y SERVICIOS
        # --------------------------------------------------------
        {
            "id": "civ-agua-001",
            "tipo": "jurisprudencia",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional-Administrativo",
            "tema": "Agua y servicios públicos",
            "subtema": "Derecho humano al agua",
            "ambito": "Federal",
            "rubro": ("DERECHO HUMANO AL AGUA Y AL SANEAMIENTO. SU CONTENIDO CONSTITUCIONAL Y "
                      "ALCANCE EN TÉRMINOS DEL ARTÍCULO 4°, PÁRRAFO SEXTO, CONSTITUCIONAL."),
            "texto_resumen": (
                "El acceso al agua potable y saneamiento es derecho humano. Las autoridades deben "
                "garantizar suministro suficiente, salubre, aceptable y asequible. No puede "
                "suspenderse el suministro mínimo vital por falta de pago."
            ),
            "registro_digital": "Art. 4 párrafo sexto CPEUM",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031895",
            "nota_verificacion": "Derecho humano consagrado en el art. 4 CPEUM. Buscar 'derecho humano agua saneamiento' para tesis interpretativas.",
            "trascendencia": "Bloquea cortes totales de agua a domicilio.",
            "explicacion": (
                "En amparo, el corte total de agua se suspende casi automáticamente; lo que sí puede "
                "el organismo operador es restringir a un mínimo vital (50 lt/persona/día). Aplica a "
                "SACMEX y organismos municipales."
            ),
            "etiquetas": ["derecho humano al agua", "art. 4 CPEUM", "mínimo vital"],
        },
        {
            "id": "civ-agua-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Administrativo",
            "tema": "Agua y servicios públicos",
            "subtema": "Cobros excesivos y nulidad",
            "ambito": "Federal — colegiados",
            "rubro": ("AGUA. LOS COBROS NOTORIAMENTE EXCESIVOS POR EL SERVICIO PUEDEN COMBATIRSE "
                      "EN JUICIO CONTENCIOSO ADMINISTRATIVO Y, EN SU CASO, AMPARO INDIRECTO."),
            "texto_resumen": (
                "El usuario puede impugnar boletas excesivas por la vía contenciosa ante el TJA "
                "y, en su caso, amparo indirecto. La autoridad debe motivar el consumo y permitir "
                "verificación independiente del medidor."
            ),
            "registro_digital": "Criterio TJA",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2008331",
            "nota_verificacion": "Línea de Tribunales Colegiados. Buscar 'agua cobro excesivo TJA' en SJF.",
            "trascendencia": "Vía estándar contra cobros irregulares de SACMEX y similares.",
            "explicacion": (
                "Solicitar verificación del medidor y aclaración administrativa son requisitos "
                "previos. Conservar acuses. El TJA CDMX y Edomex han resuelto favorablemente "
                "múltiples casos de cobros aberrantes."
            ),
            "etiquetas": ["cobro excesivo", "medidor", "TJA"],
        },

        # ============================================================
        # M A T E R I A   M E R C A N T I L
        # ============================================================
        {
            "id": "mer-eje-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Juicio ejecutivo mercantil",
            "subtema": "Procedencia y documento base",
            "ambito": "Federal",
            "rubro": ("JUICIO EJECUTIVO MERCANTIL. PARA SU PROCEDENCIA SE REQUIERE QUE EL DOCUMENTO "
                      "BASE TRAIGA APAREJADA EJECUCIÓN EN TÉRMINOS DEL ARTÍCULO 1391 DEL CÓDIGO DE "
                      "COMERCIO."),
            "texto_resumen": (
                "Sólo proceden por vía ejecutiva mercantil los documentos enlistados en el art. 1391 "
                "Cco: sentencias, instrumentos públicos, títulos de crédito, pólizas notariadas, "
                "convenios judiciales, decisiones arbitrales, entre otros."
            ),
            "registro_digital": "2025924",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2025924",
            "nota_verificacion": "Tesis sobre presupuesto procesal de la vía ejecutiva mercantil. Documentos base en art. 1391 Cco.",
            "trascendencia": "Filtra acciones ejecutivas improcedentes (ahorra tiempo y costas).",
            "explicacion": (
                "Antes de demandar en ejecutivo verifica si tu documento está en la lista del 1391. "
                "Si no, ve por vía ordinaria mercantil u oral mercantil según cuantía."
            ),
            "etiquetas": ["ejecutivo mercantil", "art. 1391 Cco", "documento base"],
        },
        {
            "id": "mer-tit-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Títulos de crédito",
            "subtema": "Pagaré — requisitos esenciales",
            "ambito": "Federal",
            "rubro": ("PAGARÉ. REQUISITOS ESENCIALES Y CONSECUENCIAS DE SU AUSENCIA CONFORME AL "
                      "ARTÍCULO 170 DE LA LGTOC."),
            "texto_resumen": (
                "El pagaré debe contener: mención de ser pagaré, promesa incondicional de pagar suma "
                "determinada, nombre del beneficiario, fecha y lugar de pago, fecha y lugar de "
                "suscripción y firma del suscriptor. Su ausencia priva al documento de eficacia "
                "ejecutiva, no de su valor como mero documento privado."
            ),
            "registro_digital": "2019464",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2019464",
            "nota_verificacion": "Tesis sobre requisitos formales del pagaré. Para análisis completo del art. 170 LGTOC, buscar 'pagaré requisitos esenciales'.",
            "trascendencia": "Determina si procede ejecutivo o solo ordinario.",
            "explicacion": (
                "Si falta requisito esencial, no procede ejecutivo, pero sí acción causal por ordinario "
                "mercantil con el documento como prueba documental privada."
            ),
            "etiquetas": ["pagaré", "art. 170 LGTOC", "literalidad"],
        },
        {
            "id": "mer-tit-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Títulos de crédito",
            "subtema": "Pagaré en blanco",
            "ambito": "Federal",
            "rubro": ("PAGARÉ. EL DEUDOR PUEDE OPONER LA EXCEPCIÓN DE ALTERACIÓN CUANDO SE SUSCRIBIÓ "
                      "EN BLANCO Y SE LLENÓ EN TÉRMINOS DISTINTOS A LOS PACTADOS."),
            "texto_resumen": (
                "Si el pagaré fue firmado en blanco, el suscriptor puede excepcionar que su llenado "
                "no se ajustó al pacto. La carga probatoria es alta: hay que demostrar el pacto y la "
                "alteración mediante medios externos al título."
            ),
            "registro_digital": "2024056",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2024056",
            "nota_verificacion": "Tesis relacionada. Cuando hay alteración o pagaré en blanco, opera la acción causal.",
            "trascendencia": "Defensa frecuente en pagarés con espacios alterados.",
            "explicacion": (
                "Pericial caligráfica y testimoniales del momento de la firma son útiles. La excepción "
                "rara vez prospera por dificultad probatoria, pero es viable."
            ),
            "etiquetas": ["pagaré en blanco", "alteración", "excepción"],
        },
        {
            "id": "mer-con-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Concursos mercantiles",
            "subtema": "Procedencia y supuestos",
            "ambito": "Federal",
            "rubro": ("CONCURSO MERCANTIL. SUPUESTOS DE INCUMPLIMIENTO GENERALIZADO DE OBLIGACIONES "
                      "Y CARGA PROBATORIA DEL ACREEDOR DEMANDANTE."),
            "texto_resumen": (
                "El acreedor que demande concurso debe acreditar (i) ser titular de crédito vencido "
                "no pagado por más de 30 días y (ii) que la comerciante incurrió en otros incumplimientos "
                "que representen al menos 35% de sus pasivos o que carece de activos líquidos suficientes."
            ),
            "registro_digital": "Ley de Concursos Mercantiles arts. 9-10",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031788",
            "nota_verificacion": "Supuestos en la LCM. Buscar 'concurso mercantil incumplimiento generalizado' en SJF.",
            "trascendencia": "Marco para acciones de acreedor según LCM.",
            "explicacion": (
                "Información financiera del deudor suele obtenerse vía RUG, CNBV o requerimientos "
                "fiscales. La acción de acreedor es difícil; lo común es solicitud propia del comerciante."
            ),
            "etiquetas": ["concurso mercantil", "LCM", "incumplimiento generalizado"],
        },
        {
            "id": "mer-soc-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Sociedades mercantiles",
            "subtema": "Levantamiento del velo corporativo",
            "ambito": "Federal",
            "rubro": ("DESESTIMACIÓN DE LA PERSONALIDAD JURÍDICA (LEVANTAMIENTO DEL VELO CORPORATIVO). "
                      "PROCEDE EXCEPCIONALMENTE ANTE ABUSO DE LA FORMA SOCIETARIA EN FRAUDE A TERCEROS."),
            "texto_resumen": (
                "El juez puede desconocer la personalidad de la sociedad cuando ésta se utiliza como "
                "instrumento para defraudar acreedores, evadir responsabilidades o eludir la ley. "
                "Procede excepcional y restrictivamente."
            ),
            "registro_digital": "2029944",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029944",
            "nota_verificacion": "Jurisprudencia 1a. II/2025 — doctrina vigente más reciente de Primera Sala SCJN.",
            "trascendencia": "Permite ir contra socios cuando hay simulación.",
            "explicacion": (
                "Hay que probar: confusión patrimonial entre sociedad y socios, infrapatrimonización "
                "deliberada, uso instrumental, daño a terceros. Tesis útil contra empresarios que "
                "vacían SA antes de litigios."
            ),
            "etiquetas": ["velo corporativo", "abuso societario", "fraude"],
        },

        # ============================================================
        # M A T E R I A   P E N A L
        # ============================================================
        {
            "id": "pen-acu-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Sistema acusatorio",
            "subtema": "Principios rectores",
            "ambito": "Federal",
            "rubro": ("SISTEMA PENAL ACUSATORIO. SUS PRINCIPIOS RECTORES SON DE OBSERVANCIA "
                      "OBLIGATORIA PARA LOS OPERADORES JURÍDICOS."),
            "texto_resumen": (
                "Publicidad, contradicción, concentración, continuidad e inmediación (art. 20 A CPEUM) "
                "rigen todo el proceso. Su violación constituye agravio de garantías procesales y "
                "puede conducir a nulidad."
            ),
            "registro_digital": "Art. 20 A CPEUM",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032097",
            "nota_verificacion": "Principios constitucionales del sistema penal acusatorio. Buscar 'sistema acusatorio principios rectores' en SJF.",
            "trascendencia": "Eje de control de validez de actuaciones penales.",
            "explicacion": (
                "Cuestionar audiencias en que el juez no estuvo presente continuamente, o donde se "
                "introdujo prueba sin contradicción, es estrategia recurrente del defensor."
            ),
            "etiquetas": ["acusatorio", "art. 20 CPEUM", "principios"],
        },
        {
            "id": "pen-pri-001",
            "tipo": "jurisprudencia",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente_con_matiz",
            "materia": "Penal-Constitucional",
            "tema": "Prisión preventiva oficiosa",
            "subtema": "Convencionalidad",
            "ambito": "Federal",
            "rubro": ("PRISIÓN PREVENTIVA OFICIOSA. SU APLICACIÓN DEBE INTERPRETARSE CONFORME AL "
                      "CONTROL DE CONVENCIONALIDAD Y A LOS PRECEDENTES DE LA CIDH."),
            "texto_resumen": (
                "Tras García Rodríguez y Tzompaxtle Tecpile vs. México (CIDH 2022-2023), la prisión "
                "preventiva oficiosa del art. 19 CPEUM debe sujetarse a control de convencionalidad: "
                "necesidad, proporcionalidad, individualización."
            ),
            "registro_digital": "2032107",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032107",
            "nota_verificacion": "Tesis 12a Época sobre PPO. Para CIDH Tzompaxtle y García Rodríguez, consultar también jurisprudenciaSCJN sobre control de convencionalidad post-2023.",
            "trascendencia": "Reconfigura completamente la PPO en México.",
            "explicacion": (
                "Tras la reforma 2024 y las sentencias CIDH, el juez DEBE motivar individualmente la "
                "PPO aún cuando el delito esté en el catálogo. La defensa tiene espacio real de litigio."
            ),
            "etiquetas": ["prisión preventiva", "CIDH", "convencionalidad", "art. 19 CPEUM"],
        },
        {
            "id": "pen-pru-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Prueba ilícita",
            "subtema": "Regla de exclusión",
            "ambito": "Federal",
            "rubro": ("PRUEBA ILÍCITA. LA OBTENIDA CON VIOLACIÓN A DERECHOS FUNDAMENTALES DEBE SER "
                      "EXCLUIDA Y NO PUEDE FUNDAR SENTENCIA CONDENATORIA."),
            "texto_resumen": (
                "Toda prueba obtenida directa o indirectamente con violación de derechos humanos "
                "(detención ilegal, allanamiento sin orden, tortura, interceptación sin autorización "
                "judicial) debe ser excluida. Aplica también a la prueba derivada (fruto del árbol "
                "envenenado), salvo excepciones taxativas."
            ),
            "registro_digital": "2028424",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2028424",
            "nota_verificacion": "Tesis sobre exclusión de prueba ilícita y árbol envenenado. Aplica art. 20 A CPEUM.",
            "trascendencia": "Defensa nuclear en casos con detenciones cuestionables.",
            "explicacion": (
                "Atacar la legalidad de la detención inicial es muchas veces la mejor estrategia: "
                "si cae la detención, caen las pruebas derivadas. Audiencia de control de detención "
                "es el momento crítico."
            ),
            "etiquetas": ["prueba ilícita", "exclusión", "árbol envenenado"],
        },
        {
            "id": "pen-cad-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Cadena de custodia",
            "subtema": "Estándar y consecuencias de su ruptura",
            "ambito": "Federal",
            "rubro": ("CADENA DE CUSTODIA. SU INCUMPLIMIENTO AFECTA EL VALOR PROBATORIO DE LOS "
                      "INDICIOS, AUNQUE NO NECESARIAMENTE CONDUCE A SU EXCLUSIÓN."),
            "texto_resumen": (
                "El incumplimiento de la cadena de custodia (art. 227 CNPP) no excluye automáticamente "
                "la evidencia, pero disminuye o anula su valor probatorio. Corresponde al juez ponderar "
                "la magnitud de la ruptura y si afecta la fiabilidad."
            ),
            "registro_digital": "2021845",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2021845",
            "nota_verificacion": "Tesis sobre efectos de la transgresión a la cadena de custodia (art. 227 CNPP).",
            "trascendencia": "Margen para litigar valor de pruebas materiales.",
            "explicacion": (
                "En narcomenudeo y armas, atacar irregularidades en custodia (transporte sin sello, "
                "embalaje deficiente, omisiones en registro) reduce o anula el peso del indicio."
            ),
            "etiquetas": ["cadena de custodia", "art. 227 CNPP", "fiabilidad"],
        },

        # ============================================================
        # M A T E R I A   F I S C A L
        # ============================================================
        {
            "id": "fis-cad-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Fiscal",
            "tema": "Caducidad de facultades del fisco",
            "subtema": "Plazo y cómputo",
            "ambito": "Federal",
            "rubro": ("CADUCIDAD DE LAS FACULTADES DE COMPROBACIÓN. EL PLAZO DEL ARTÍCULO 67 DEL "
                      "CFF SE COMPUTA A PARTIR DEL DÍA SIGUIENTE A AQUÉL EN QUE DEBIÓ PRESENTARSE "
                      "LA DECLARACIÓN."),
            "texto_resumen": (
                "El plazo de 5 años (regla general) o 10 años (sin RFC o sin declaraciones) corre "
                "desde el día siguiente a aquel en que debió presentarse la declaración del ejercicio."
            ),
            "registro_digital": "Art. 67 CFF",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2023051",
            "nota_verificacion": "Plazo de 5/10 años en CFF. Buscar 'caducidad facultades comprobación art 67' en SJF.",
            "trascendencia": "Defensa esencial frente a revisiones tardías del SAT.",
            "explicacion": (
                "Hay que oponer la caducidad como excepción de previo y especial pronunciamiento. "
                "Cuidado con interrupciones por revisiones notificadas legalmente."
            ),
            "etiquetas": ["caducidad", "art. 67 CFF", "facultades de comprobación"],
        },
        {
            "id": "fis-dev-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Fiscal",
            "tema": "Devolución de saldos a favor",
            "subtema": "Negativa ficta y juicio contencioso",
            "ambito": "Federal",
            "rubro": ("DEVOLUCIÓN DE SALDOS A FAVOR. LA NEGATIVA FICTA POR FALTA DE RESPUESTA EN "
                      "40 DÍAS PERMITE ACUDIR AL JUICIO CONTENCIOSO ADMINISTRATIVO."),
            "texto_resumen": (
                "Si el SAT no resuelve la solicitud de devolución en el plazo del art. 22 CFF, opera "
                "negativa ficta. El contribuyente puede acudir al TFJA y solicitar también daños y "
                "perjuicios cuando proceda."
            ),
            "registro_digital": "Art. 22 CFF",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032008",
            "nota_verificacion": "Negativa ficta tras 40 días en CFF. Buscar 'devolución saldo favor negativa ficta' en SJF.",
            "trascendencia": "Camino estándar contra demoras del SAT en devoluciones.",
            "explicacion": (
                "Conserva acuse de presentación y vence el plazo; presenta demanda de nulidad con "
                "actualización por INPC. Solicitar también recargos a favor del contribuyente."
            ),
            "etiquetas": ["devolución", "negativa ficta", "art. 22 CFF"],
        },
        {
            "id": "fis-cfd-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Fiscal",
            "tema": "Comprobantes fiscales (CFDI)",
            "subtema": "Operaciones inexistentes — art. 69-B CFF",
            "ambito": "Federal",
            "rubro": ("OPERACIONES INEXISTENTES. EL PROCEDIMIENTO DEL ARTÍCULO 69-B DEL CFF "
                      "CONSTITUYE UN ACTO DE MOLESTIA Y SU INCLUSIÓN EN LISTAS DEFINITIVAS ES "
                      "ATACABLE POR AMPARO INDIRECTO."),
            "texto_resumen": (
                "El procedimiento de presunción de inexistencia de operaciones genera consecuencias "
                "graves (no deducibilidad de CFDI, listas públicas). Es acto de molestia que puede "
                "atacarse por amparo si se vulneran garantías de audiencia o fundamentación."
            ),
            "registro_digital": "2031350",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031350",
            "nota_verificacion": "Tesis 12a Época sobre carga probatoria de materialidad en 69-B CFF.",
            "trascendencia": "Defensa contra inclusión en listas del 69-B.",
            "explicacion": (
                "Plazo de 15 días para desvirtuar es estricto. Si no se atendió, queda amparo indirecto "
                "contra publicación definitiva. Para terceros que compraron a empresa listada: probar "
                "materialidad de la operación."
            ),
            "etiquetas": ["69-B CFF", "CFDI", "operaciones inexistentes", "materialidad"],
        },

        # ============================================================
        # M A T E R I A   L A B O R A L
        # ============================================================
        {
            "id": "lab-ref-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Laboral",
            "tema": "Reforma laboral 2019 — Justicia laboral",
            "subtema": "Competencia y vía",
            "ambito": "Federal",
            "rubro": ("JUSTICIA LABORAL. LA REFORMA DE 2019 TRASLADA LA JURISDICCIÓN DE LAS JUNTAS "
                      "DE CONCILIACIÓN Y ARBITRAJE A TRIBUNALES LABORALES DEL PODER JUDICIAL."),
            "texto_resumen": (
                "A partir de la reforma constitucional 2017 y legal 2019, los conflictos individuales "
                "y colectivos se resuelven ante Tribunales Laborales del Poder Judicial (Federación, "
                "Estados o CDMX), con conciliación obligatoria previa en Centros de Conciliación."
            ),
            "registro_digital": "Decreto DOF 1-V-2019",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031896",
            "nota_verificacion": "Reforma constitucional y legal a la justicia laboral. Buscar 'tribunales laborales reforma 2019' en SJF.",
            "trascendencia": "Marco competencial vigente.",
            "explicacion": (
                "Verificar fecha de conflicto y entidad para determinar si aplica régimen anterior "
                "(JCA) o nuevo (Tribunales Laborales). En CDMX, el Tribunal Laboral arrancó en 2021."
            ),
            "etiquetas": ["reforma 2019", "Tribunales Laborales", "conciliación previa"],
        },
        {
            "id": "lab-des-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Laboral",
            "tema": "Despido injustificado",
            "subtema": "Carga probatoria",
            "ambito": "Federal",
            "rubro": ("DESPIDO. LA CARGA DE PROBAR SU JUSTIFICACIÓN CORRESPONDE AL PATRÓN; LA "
                      "EXISTENCIA DE LA RELACIÓN LABORAL Y EL DESPIDO MISMO, AL TRABAJADOR EN "
                      "PRIMERA INSTANCIA."),
            "texto_resumen": (
                "Si el patrón niega el despido, debe acreditar la subsistencia de la relación o que "
                "el trabajador abandonó el trabajo. Si reconoce el despido, debe acreditar la causa "
                "justificada conforme al art. 47 LFT."
            ),
            "registro_digital": "2029731",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029731",
            "nota_verificacion": "Tesis 11a Época sobre carga probatoria del patrón.",
            "trascendencia": "Principio probatorio nuclear en juicios laborales.",
            "explicacion": (
                "Estrategia patronal: ofrecer reinstalación para evitar carga probatoria. Estrategia "
                "trabajador: presentar testigos del momento del despido y comunicaciones inmediatas."
            ),
            "etiquetas": ["despido", "carga probatoria", "art. 47 LFT"],
        },
        {
            "id": "lab-sub-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Laboral",
            "tema": "Subcontratación / Outsourcing",
            "subtema": "Reforma 2021 — prohibición general",
            "ambito": "Federal",
            "rubro": ("SUBCONTRATACIÓN LABORAL. LA REFORMA DE 2021 PROHÍBE LA DE PERSONAL Y SÓLO "
                      "PERMITE LA DE SERVICIOS U OBRAS ESPECIALIZADAS REGISTRADAS EN EL REPSE."),
            "texto_resumen": (
                "Tras la reforma de abril de 2021 a la LFT, queda prohibida la subcontratación de "
                "personal. Solo subsiste la subcontratación de servicios u obras especializadas "
                "ajenas al objeto social y actividad económica principal del contratante, registrada "
                "en el REPSE."
            ),
            "registro_digital": "Reforma LFT 23-IV-2021",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2030759",
            "nota_verificacion": "Reforma a la LFT y creación del REPSE. Buscar 'REPSE subcontratación servicios especializados' en SJF.",
            "trascendencia": "Reconfigura toda la contratación de servicios en México.",
            "explicacion": (
                "Si la empresa subcontrata sin REPSE o subcontrata su actividad principal, se "
                "produce responsabilidad solidaria con multas y los trabajadores son legalmente "
                "del contratante. Verificación de REPSE es esencial en due diligence."
            ),
            "etiquetas": ["outsourcing", "REPSE", "reforma 2021", "responsabilidad solidaria"],
        },

        # ============================================================
        # M A T E R I A   A D M I N I S T R A T I V O
        # ============================================================
        {
            "id": "adm-nul-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Administrativo",
            "tema": "Acto administrativo / nulidad",
            "subtema": "Fundamentación y motivación",
            "ambito": "Federal",
            "rubro": ("FUNDAMENTACIÓN Y MOTIVACIÓN DEL ACTO ADMINISTRATIVO. SU AUSENCIA O "
                      "INSUFICIENCIA CONFIGURA VIOLACIÓN AL ARTÍCULO 16 CONSTITUCIONAL."),
            "texto_resumen": (
                "Todo acto de autoridad debe citar con precisión los preceptos aplicables y las "
                "razones particulares del caso que llevan a aplicarlos. La fundamentación genérica "
                "o la motivación abstracta vulneran el 16 constitucional y conducen a nulidad."
            ),
            "registro_digital": "Art. 16 CPEUM",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031869",
            "nota_verificacion": "Garantía constitucional de fundamentación y motivación. Buscar 'fundamentación motivación acto administrativo' en SJF.",
            "trascendencia": "Estándar nuclear de control de actos administrativos.",
            "explicacion": (
                "Argumento siempre verificable: actos de gobierno frecuentemente repiten formularios "
                "sin individualizar al destinatario. El TJA y el amparo indirecto los nulifican con "
                "regularidad."
            ),
            "etiquetas": ["fundamentación", "motivación", "art. 16 CPEUM", "nulidad"],
        },
        {
            "id": "adm-res-001",
            "tipo": "jurisprudencia",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Administrativo",
            "tema": "Responsabilidad administrativa de servidores públicos",
            "subtema": "Procedimiento conforme a LGRA",
            "ambito": "Federal",
            "rubro": ("RESPONSABILIDADES ADMINISTRATIVAS. EL PROCEDIMIENTO SEGUIDO ANTE TRIBUNALES "
                      "DE JUSTICIA ADMINISTRATIVA POR FALTAS GRAVES DEBE RESPETAR EL DEBIDO PROCESO "
                      "CONFORME A LA LEY GENERAL DE RESPONSABILIDADES ADMINISTRATIVAS."),
            "texto_resumen": (
                "Las faltas graves se resuelven por el TJA correspondiente con plenitud de "
                "garantías procesales: notificación personal, derecho de defensa, ofrecimiento de "
                "pruebas, alegatos, sentencia fundada y motivada."
            ),
            "registro_digital": "Ley General de Responsabilidades Administrativas",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032028",
            "nota_verificacion": "LGRA publicada DOF 18-VII-2016. Buscar 'responsabilidad administrativa grave TJA debido proceso'.",
            "trascendencia": "Marco para impugnar sanciones administrativas.",
            "explicacion": (
                "Antes de la LGRA (2016) muchas faltas eran resueltas por la propia dependencia. "
                "Hoy las graves van al TJA. Hay que distinguir gravedad para conocer la vía."
            ),
            "etiquetas": ["LGRA", "responsabilidad administrativa", "debido proceso"],
        },

        # ============================================================
        # C O N D O M I N I O
        # ============================================================
        {
            "id": "con-cuo-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil — Condominio",
            "tema": "Régimen de propiedad en condominio",
            "subtema": "Cuotas condominales — vía y ejecutividad",
            "ambito": "CDMX (LPCI CDMX) — análogo Edomex",
            "rubro": ("CUOTAS DE MANTENIMIENTO EN CONDOMINIO. SU COBRO PROCEDE POR LA VÍA EJECUTIVA "
                      "CIVIL CUANDO ASÍ LO PREVÉ LA LEY LOCAL Y EXISTE CERTIFICACIÓN DEL ADMINISTRADOR."),
            "texto_resumen": (
                "Conforme a la Ley de Propiedad en Condominio CDMX (art. 56 y concordantes), las "
                "cuotas vencidas pueden cobrarse por vía ejecutiva civil cuando exista certificación "
                "del administrador, autorizada por el Comité de Vigilancia, que constituye documento "
                "que trae aparejada ejecución."
            ),
            "registro_digital": "Art. 56 LPCI CDMX",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031361",
            "nota_verificacion": "Ley de Propiedad en Condominio CDMX. Buscar 'cuotas mantenimiento condominio vía ejecutiva' en SJF.",
            "trascendencia": "Esencial para administración condominal.",
            "explicacion": (
                "Verificar formalidad de la certificación: firma del administrador, sello, "
                "autorización del comité, desglose mensual. Sin estos requisitos, la vía cae a ordinaria."
            ),
            "etiquetas": ["cuotas condominales", "LPCI CDMX", "vía ejecutiva"],
        },
        {
            "id": "con-asa-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil — Condominio",
            "tema": "Régimen de propiedad en condominio",
            "subtema": "Asambleas — convocatoria y validez",
            "ambito": "Federal — interpreta LPCI CDMX",
            "rubro": ("ASAMBLEAS CONDOMINALES. LA INDEBIDA CONVOCATORIA AFECTA LA VALIDEZ DE "
                      "LOS ACUERDOS Y PERMITE SU IMPUGNACIÓN."),
            "texto_resumen": (
                "La convocatoria debe respetar plazo, forma y orden del día (art. 32 LPCI CDMX). "
                "Su incumplimiento es causal de nulidad de los acuerdos adoptados, salvo ratificación "
                "expresa en asamblea posterior debidamente convocada."
            ),
            "registro_digital": "Art. 32 LPCI CDMX",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2028919",
            "nota_verificacion": "Convocatoria conforme LPCI CDMX. Buscar 'asamblea condominio convocatoria nulidad' en SJF.",
            "trascendencia": "Defensa frecuente de minorías condominales.",
            "explicacion": (
                "Conserva pruebas de cómo se realizó la convocatoria (carteles, mensajes, fotos). "
                "Plazo de impugnación es corto (60 días naturales en CDMX desde celebración o "
                "conocimiento)."
            ),
            "etiquetas": ["asamblea", "convocatoria", "nulidad", "LPCI CDMX"],
        },

        # ============================================================
        # A M P A R O   (transversal)
        # ============================================================
        {
            "id": "amp-int-001",
            "tipo": "jurisprudencia",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Amparo",
            "tema": "Procedencia del amparo",
            "subtema": "Interés jurídico vs. interés legítimo",
            "ambito": "Federal",
            "rubro": ("INTERÉS LEGÍTIMO EN EL AMPARO. NATURALEZA, ALCANCES Y DIFERENCIAS RESPECTO "
                      "AL INTERÉS JURÍDICO TRADICIONAL."),
            "texto_resumen": (
                "Tras la reforma 2011, el amparo procede por interés legítimo (afectación cualificada "
                "a la esfera jurídica del quejoso, aunque no se afecte derecho subjetivo) además del "
                "tradicional interés jurídico (afectación a derecho subjetivo directo). Ambos son "
                "vías de acceso al amparo."
            ),
            "registro_digital": "2032086",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032086",
            "nota_verificacion": "Tesis 12a Época sobre interés legítimo. Reforma 2011 al art. 107 CPEUM y art. 5 LA.",
            "trascendencia": "Reconfigura el acceso al amparo desde 2011.",
            "explicacion": (
                "En amparos colectivos, ambientales, urbanos y de derechos difusos, invocar interés "
                "legítimo es habitual. Hay que individualizar la afectación cualificada concreta, "
                "no basta interés general."
            ),
            "etiquetas": ["interés legítimo", "reforma 2011", "procedencia"],
        },
        {
            "id": "amp-sus-001",
            "tipo": "jurisprudencia",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Amparo",
            "tema": "Suspensión",
            "subtema": "Apariencia del buen derecho",
            "ambito": "Federal",
            "rubro": ("SUSPENSIÓN EN AMPARO. LA APARIENCIA DEL BUEN DERECHO Y EL PELIGRO EN LA "
                      "DEMORA SON FACTORES DETERMINANTES PARA SU CONCESIÓN."),
            "texto_resumen": (
                "Junto a los requisitos del art. 128 LA (solicitud, no afectación al orden público "
                "ni interés social), el juez debe ponderar apariencia del buen derecho (fumus boni "
                "iuris) y peligro en la demora (periculum in mora) — análisis preliminar de la "
                "probabilidad de éxito del amparo."
            ),
            "registro_digital": "2032118",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032118",
            "nota_verificacion": "Tesis 12a Época sobre suspensión. Apariencia del buen derecho y peligro en la demora — art. 128 LA.",
            "trascendencia": "Eje del litigio cautelar en amparo.",
            "explicacion": (
                "En el escrito de amparo, argumentar específicamente apariencia + peligro acelera "
                "y mejora la concesión. Sin ello, el juzgador tiende a negar la suspensión."
            ),
            "etiquetas": ["suspensión", "fumus boni iuris", "periculum"],
        },
        {
            "id": "amp-pro-001",
            "tipo": "jurisprudencia",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Amparo",
            "tema": "Precedentes obligatorios",
            "subtema": "Reforma 2021 — sistema de precedentes",
            "ambito": "Federal",
            "rubro": ("PRECEDENTES OBLIGATORIOS DE LA SUPREMA CORTE. EL SISTEMA INSTAURADO POR LA "
                      "REFORMA DE 2021 OBLIGA A LOS ÓRGANOS JURISDICCIONALES INFERIORES SIN "
                      "REQUERIR REITERACIÓN."),
            "texto_resumen": (
                "Las razones que sustenten las sentencias del Pleno aprobadas por al menos 8 votos "
                "y de las Salas con al menos 4 votos son obligatorias para todos los tribunales del "
                "país, sin necesidad de cinco reiteraciones."
            ),
            "registro_digital": "2029745",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029745",
            "nota_verificacion": "Tesis relacionada sobre precedentes y control difuso. Reforma 2021: arts. 222, 223 y 225 LA.",
            "trascendencia": "Cambio paradigmático en el sistema de jurisprudencia.",
            "explicacion": (
                "Hoy se cita la 'razón fundante' del precedente, no solo el rubro de tesis. Hay que "
                "estudiar la sentencia completa, no solo el extracto. Las ejecutorias importan."
            ),
            "etiquetas": ["precedentes obligatorios", "reforma 2021", "razón fundante"],
        },

        # ============================================================
        # S E N T E N C I A S   H I T O   S C J N
        # ============================================================
        {
            "id": "sen-001",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Derechos humanos",
            "tema": "Caso Rosendo Radilla y control de convencionalidad",
            "subtema": "Expediente Varios 912/2010",
            "ambito": "Federal",
            "rubro": "Expediente Varios 912/2010 — Caso Rosendo Radilla Pacheco vs. México",
            "texto_resumen": (
                "El Pleno de la SCJN, al cumplimentar la sentencia de la CIDH, estableció que: "
                "(i) las sentencias de la CIDH contra México son obligatorias en sus términos; "
                "(ii) todos los jueces del país tienen obligación de ejercer control difuso de "
                "constitucionalidad y convencionalidad; (iii) el fuero militar queda restringido "
                "para civiles y delitos contra civiles."
            ),
            "registro_digital": "Expediente Varios 912/2010 — DOF 04-X-2011",
            "fecha_publicacion": "2011",
            "trascendencia": (
                "Sentencia fundacional del control difuso de convencionalidad en México. Cambia "
                "completamente la práctica judicial nacional."
            ),
            "explicacion": (
                "Antes solo el Poder Judicial Federal hacía control constitucional. Después de "
                "Radilla, cualquier juez (local o federal) puede y debe inaplicar normas que "
                "violen derechos humanos. Es el cimiento del Derecho del Siglo XXI mexicano."
            ),
            "etiquetas": ["control difuso", "CIDH", "convencionalidad", "fuero militar"],
        },
        {
            "id": "sen-002",
            "tipo": "sentencia hito",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil / Derecho de familia",
            "tema": "Matrimonio igualitario",
            "subtema": "Amparos en revisión 152/2013, 567/2012, 581/2012, 704/2014, 735/2014",
            "ambito": "Federal",
            "rubro": "Matrimonio entre personas del mismo sexo — Jurisprudencia 1a./J. 43/2015",
            "texto_resumen": (
                "Los códigos civiles estatales que limitan el matrimonio a hombre y mujer son "
                "inconstitucionales por violar el principio de igualdad y no discriminación. "
                "La finalidad reproductiva no es justificación constitucional admisible."
            ),
            "registro_digital": "2009407",
            "tesis_clave": "1a./J. 43/2015 (10a.)",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2009407",
            "fuente_publicacion": "Gaceta del SJF, Libro 19, Junio de 2015, Tomo I, página 536",
            "fecha_publicacion": "2015",
            "trascendencia": (
                "Una de las jurisprudencias más citadas en amparos contra códigos civiles estatales. "
                "Pavimentó el matrimonio igualitario en toda la República por vía de amparo. "
                "REGISTRO VERIFICADO directamente en el SJF."
            ),
            "explicacion": (
                "Para usuarios en estados donde la ley local aún no se reforma, el amparo con esta "
                "jurisprudencia es vía casi automática. CDMX lo reformó desde 2009 y Edomex en 2022."
            ),
            "etiquetas": ["matrimonio igualitario", "igualdad", "no discriminación"],
        },
        {
            "id": "sen-003",
            "tipo": "sentencia hito",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Penal / Salud",
            "tema": "Uso lúdico de cannabis",
            "subtema": "Amparos en revisión 237/2014 y siguientes",
            "ambito": "Federal",
            "rubro": "Inconstitucionalidad de la prohibición absoluta de uso lúdico de cannabis",
            "texto_resumen": (
                "La prohibición absoluta del autoconsumo lúdico de cannabis viola el libre desarrollo "
                "de la personalidad (art. 1 CPEUM). El Estado no puede prohibir actos que no afectan "
                "a terceros bajo argumento paternalista."
            ),
            "registro_digital": "Amparo en Revisión 237/2014",
            "url_sjf": "https://www.scjn.gob.mx/sites/default/files/proyectos_resolucion_scjn/documento/2018-11/AR-237-2014.pdf",
            "nota_verificacion": "Sentencia hito sobre uso lúdico del cannabis. Reiteración 2015-2018 derivó en Declaratoria General de Inconstitucionalidad 1/2018.",
            "fecha_publicacion": "2015 y reiteración 2018",
            "trascendencia": "Hito de libre desarrollo de la personalidad y autonomía individual.",
            "explicacion": (
                "Cinco sentencias en el mismo sentido configuraron declaratoria general de "
                "inconstitucionalidad en 2021. El Congreso aún no ha cumplido la orden de legislar "
                "regulando la sustancia."
            ),
            "etiquetas": ["cannabis", "libre desarrollo personalidad", "declaratoria general"],
        },
        {
            "id": "sen-004",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Penal / Salud",
            "tema": "Aborto — despenalización",
            "subtema": "Acción de Inconstitucionalidad 148/2017 y AR 79/2023",
            "ambito": "Federal",
            "rubro": "Despenalización del aborto — criminalización absoluta inconstitucional",
            "texto_resumen": (
                "La criminalización absoluta del aborto viola los derechos a la salud, igualdad, "
                "vida digna y autodeterminación reproductiva de las mujeres. Los Códigos Penales "
                "que la prevean son inconstitucionales en esa porción."
            ),
            "registro_digital": "Acción de Inconstitucionalidad 148/2017 (Coahuila) — DOF 2021",
            "fecha_publicacion": "2021, ratificado y ampliado en 2023",
            "trascendencia": (
                "Marco que orienta despenalización gradual en cada entidad federativa por vía de "
                "amparo o reforma legislativa."
            ),
            "explicacion": (
                "Para mujeres en entidades donde sigue penalizado, el amparo con esta jurisprudencia "
                "es vía expedita. CDMX (2007) y Edomex (2024) ya lo despenalizaron en primer trimestre."
            ),
            "etiquetas": ["aborto", "autodeterminación reproductiva", "salud"],
        },
        {
            "id": "sen-005",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Penal / Constitucional",
            "tema": "Prisión preventiva oficiosa — convencionalidad",
            "subtema": "Inaplicación por control de convencionalidad",
            "ambito": "Federal",
            "rubro": "Tzompaxtle Tecpile y otros vs. México (CIDH) — recepción interna",
            "texto_resumen": (
                "Tras las sentencias de la CIDH (Tzompaxtle Tecpile y García Rodríguez), el Pleno "
                "estableció que la prisión preventiva oficiosa debe interpretarse de modo compatible "
                "con la Convención Americana: necesidad, proporcionalidad, individualización "
                "motivada, no automaticidad."
            ),
            "registro_digital": "Amparo en Revisión 237/2014",
            "url_sjf": "https://www.scjn.gob.mx/sites/default/files/proyectos_resolucion_scjn/documento/2018-11/AR-237-2014.pdf",
            "nota_verificacion": "Sentencia hito sobre uso lúdico del cannabis. Reiteración 2015-2018 derivó en Declaratoria General de Inconstitucionalidad 1/2018.",
            "fecha_publicacion": "2023-2024",
            "trascendencia": "Reconfiguración total de la PPO mexicana.",
            "explicacion": (
                "Aunque la reforma constitucional 2024 amplió el catálogo, los criterios CIDH "
                "obligan al juez a motivar individualmente. La defensa tiene espacio para litigar "
                "la inaplicación en casos concretos."
            ),
            "etiquetas": ["PPO", "CIDH", "convencionalidad"],
        },
        {
            "id": "sen-006",
            "tipo": "sentencia hito",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil / Familia",
            "tema": "Compensación económica por trabajo doméstico",
            "subtema": "Amparo Directo en Revisión 269/2014",
            "ambito": "Federal — aplica CDMX/Edomex",
            "rubro": "Compensación por trabajo doméstico no remunerado en divorcio",
            "texto_resumen": (
                "El cónyuge (mayoritariamente mujer) que se dedicó preponderantemente al trabajo "
                "doméstico tiene derecho a compensación económica en el divorcio, hasta el 50% del "
                "patrimonio adquirido durante el matrimonio, aun bajo régimen de separación de bienes."
            ),
            "registro_digital": "ADR 269/2014",
            "url_sjf": "https://www.scjn.gob.mx/sites/default/files/proyectos_resolucion_scjn/documento/2016-12/ADR-269-2014.pdf",
            "nota_verificacion": "Sentencia hito de Primera Sala sobre compensación. Recogida en art. 267 fracc. VI CCCDMX.",
            "fecha_publicacion": "2014",
            "trascendencia": "Reconoce trabajo doméstico como aportación económica.",
            "explicacion": (
                "Recogida hoy en art. 267 fracc. VI CCCDMX y análogos en Edomex. Hay que probar "
                "la dedicación preponderante al hogar y la imposibilidad o limitación para generar "
                "patrimonio propio."
            ),
            "etiquetas": ["compensación", "trabajo doméstico", "divorcio", "perspectiva de género"],
        },
        {
            "id": "sen-007",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Pueblos indígenas",
            "tema": "Consulta indígena previa, libre e informada",
            "subtema": "Amparos en revisión sobre megaproyectos",
            "ambito": "Federal",
            "rubro": "Derecho a la consulta indígena previa — Convenio 169 OIT",
            "texto_resumen": (
                "Toda medida administrativa o legislativa susceptible de afectar a pueblos indígenas "
                "debe estar precedida de consulta previa, libre, informada, culturalmente adecuada "
                "y de buena fe, conforme al Convenio 169 OIT y al art. 2 CPEUM."
            ),
            "registro_digital": "CIDH Tzompaxtle Tecpile vs. México",
            "fecha_publicacion": "Sentencias 2013-2023",
            "trascendencia": "Bloquea megaproyectos sin consulta (Tren Maya, Yaqui, etc.).",
            "explicacion": (
                "Los amparos contra megaproyectos invocan esta línea con éxito reiterado. La "
                "consulta debe ser PREVIA al diseño del proyecto, no posterior para legitimarlo."
            ),
            "etiquetas": ["consulta indígena", "Convenio 169", "megaproyectos"],
        },

        # ============================================================
        # B L O Q U E   A M P L I A D O   D E   S E N T E N C I A S   H I T O
        # ============================================================
        {
            "id": "sen-008",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Familia",
            "tema": "Adopción por parejas del mismo sexo",
            "subtema": "Acción de Inconstitucionalidad 8/2014",
            "ambito": "Federal",
            "rubro": "Adopción por parejas del mismo sexo — interés superior del menor",
            "texto_resumen": (
                "Las leyes estatales que prohíben la adopción a parejas del mismo sexo son "
                "inconstitucionales por violar la igualdad y el interés superior del menor. "
                "La orientación sexual no es indicador de aptitud parental."
            ),
            "registro_digital": "AI 8/2014 (Campeche)",
            "url_sjf": "https://www.scjn.gob.mx/sites/default/files/proyectos_resolucion_scjn/documento/2016-08/8-2014.pdf",
            "fecha_publicacion": "2016",
            "trascendencia": "Equipara plenamente filiación adoptiva sin distinción por orientación.",
            "explicacion": (
                "Esta sentencia, junto con la Acción de Inconstitucionalidad 2/2010 y los amparos "
                "sobre matrimonio igualitario, completa el bloque de igualdad familiar. CDMX y "
                "Edomex ya tienen reformas plenas; otras entidades requieren amparo si se discrimina."
            ),
            "etiquetas": ["adopción", "igualdad", "interés superior del menor", "AI 8/2014"],
        },
        {
            "id": "sen-009",
            "tipo": "sentencia hito",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil / Familia",
            "tema": "Pensión alimenticia y perspectiva de género",
            "subtema": "Amparo Directo en Revisión 1340/2015",
            "ambito": "Federal — aplica CDMX/Edomex",
            "rubro": "Alimentos — perspectiva de género y carga procesal flexibilizada",
            "texto_resumen": (
                "En juicios de alimentos, el juzgador debe aplicar perspectiva de género: relajar "
                "cargas probatorias respecto del demandante alimentista, requerir información "
                "patrimonial al deudor y suplir deficiencia. La doctrina de igualdad sustantiva "
                "compensa asimetrías estructurales."
            ),
            "registro_digital": "ADR 1340/2015 — Primera Sala",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032078",
            "fecha_publicacion": "2015 y reiterada",
            "trascendencia": "Refuerza estándar pro-alimentista, especialmente para madres con hijos menores.",
            "explicacion": (
                "Esencial cuando el deudor oculta ingresos. La sala obliga a auditar bienes, "
                "compulsar SAT y aplicar presunciones contra el contumaz."
            ),
            "etiquetas": ["alimentos", "perspectiva de género", "carga probatoria", "menores"],
        },
        {
            "id": "sen-010",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Derechos humanos",
            "tema": "Contradicción de tesis 293/2011",
            "subtema": "Bloque de constitucionalidad y jerarquía DDHH",
            "ambito": "Federal",
            "rubro": "Contradicción de Tesis 293/2011 — derechos humanos del bloque de constitucionalidad",
            "texto_resumen": (
                "Las normas de derechos humanos en tratados internacionales tienen rango constitucional. "
                "Cuando la Constitución expresamente las restrinja, prevalece la Constitución (cláusula "
                "de excepción). La jurisprudencia interamericana es vinculante para todos los jueces "
                "mexicanos."
            ),
            "registro_digital": "Contradicción de Tesis 293/2011 — Pleno SCJN",
            "url_sjf": "https://www.scjn.gob.mx/sites/default/files/proyectos_resolucion_scjn/documento/2017-02/293-2011.pdf",
            "fecha_publicacion": "Septiembre 2013",
            "trascendencia": "Fija el bloque de constitucionalidad mexicano. Pieza fundacional del DH.",
            "explicacion": (
                "Antes de 293/2011 había debate sobre jerarquía entre tratados y constitución. Esta "
                "sentencia lo zanjó: los derechos humanos internacionales tienen rango constitucional, "
                "pero las restricciones expresas de la Constitución prevalecen. Es la base del control "
                "convencional doméstico."
            ),
            "etiquetas": ["bloque de constitucionalidad", "CT 293/2011", "DDHH", "control convencional"],
        },
        {
            "id": "sen-011",
            "tipo": "sentencia hito",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil / Familia",
            "tema": "Identidad de género — rectificación de acta",
            "subtema": "Amparo en Revisión 1317/2017",
            "ambito": "Federal",
            "rubro": "Identidad de género — derecho a rectificación administrativa de acta de nacimiento",
            "texto_resumen": (
                "Toda persona tiene derecho a la rectificación de su acta de nacimiento por motivo de "
                "identidad de género, sin necesidad de procedimiento judicial complejo, peritajes "
                "médicos invasivos ni intervención quirúrgica. Procede vía administrativa expedita."
            ),
            "registro_digital": "AR 1317/2017 — Primera Sala",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032087",
            "fecha_publicacion": "2018",
            "trascendencia": "Marco para rectificaciones de género en toda la República.",
            "explicacion": (
                "CDMX y Edomex ya tienen procedimientos administrativos para ello. Para otras "
                "entidades sin marco legal, el amparo con esta jurisprudencia abre la vía."
            ),
            "etiquetas": ["identidad de género", "trans", "rectificación", "acta de nacimiento"],
        },
        {
            "id": "sen-012",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Tortura",
            "tema": "Tortura — estándar probatorio y reparación",
            "subtema": "Varios 1396/2011 y línea Israel Arzate",
            "ambito": "Federal",
            "rubro": "Tortura — obligación de investigar y excluir prueba obtenida por tortura",
            "texto_resumen": (
                "Cuando hay indicios de tortura, la autoridad ministerial y judicial DEBE investigar "
                "ex officio. Toda confesión o prueba obtenida bajo tortura debe excluirse del proceso. "
                "La omisión de investigar configura violación a los arts. 20 y 22 CPEUM y al art. 5 "
                "de la Convención Americana."
            ),
            "registro_digital": "Línea jurisprudencial — Israel Arzate, Garrido Rivera, varios",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031358",
            "fecha_publicacion": "2014-2019 (línea consolidada)",
            "trascendencia": "Pieza nuclear en defensa de personas procesadas con prueba viciada.",
            "explicacion": (
                "Defensa estándar en procesos por delitos graves: denunciar tortura, solicitar "
                "Protocolo de Estambul, pedir exclusión de prueba. Aplica también a confesiones "
                "ministeriales obtenidas bajo presión."
            ),
            "etiquetas": ["tortura", "Protocolo Estambul", "prueba ilícita", "Israel Arzate"],
        },
        {
            "id": "sen-013",
            "tipo": "sentencia hito",
            "instancia": "Segunda Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Administrativo / Salud",
            "tema": "Derecho a la salud — medicamentos",
            "subtema": "Amparo en Revisión 378/2014 — VIH",
            "ambito": "Federal",
            "rubro": "Derecho a la salud — obligación del Estado de proporcionar medicamentos esenciales",
            "texto_resumen": (
                "El Estado tiene obligación reforzada de garantizar acceso a medicamentos esenciales, "
                "particularmente para enfermedades crónicas y VIH. La falta de presupuesto no es "
                "excusa válida; el derecho a la salud (art. 4 CPEUM) es exigible directamente."
            ),
            "registro_digital": "AR 378/2014 y línea consolidada",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032114",
            "fecha_publicacion": "2014-2022",
            "trascendencia": "Permite amparos exitosos para acceso a tratamientos costosos en IMSS/ISSSTE/INSABI.",
            "explicacion": (
                "Cuando un derechohabiente o usuario del sector salud no recibe medicamento del "
                "cuadro básico (o cuando lo necesita y no está en cuadro), el amparo es vía expedita "
                "y reiteradamente exitosa."
            ),
            "etiquetas": ["derecho a la salud", "medicamentos", "VIH", "amparo"],
        },
        {
            "id": "sen-014",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Educación",
            "tema": "Educación — gratuidad y obligatoriedad",
            "subtema": "Amparos por cuotas escolares",
            "ambito": "Federal",
            "rubro": "Educación obligatoria — la gratuidad excluye cobros obligatorios",
            "texto_resumen": (
                "El art. 3 CPEUM garantiza educación obligatoria gratuita. Las escuelas públicas no "
                "pueden condicionar inscripción, calificaciones o documentos al pago de cuotas "
                "'voluntarias' obligatorias. Cualquier cobro debe ser estrictamente voluntario."
            ),
            "registro_digital": "Línea jurisprudencial — múltiples amparos",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2028157",
            "fecha_publicacion": "2015 y siguientes",
            "trascendencia": "Defensa estándar contra cobros indebidos en educación básica pública.",
            "explicacion": (
                "Las escuelas que retienen documentos por falta de pago violan la gratuidad. El "
                "amparo es la vía y procede con suspensión inmediata para liberar documentos."
            ),
            "etiquetas": ["educación", "gratuidad", "cuotas escolares", "art. 3 CPEUM"],
        },
        {
            "id": "sen-015",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Ambiental",
            "tema": "Medio ambiente sano",
            "subtema": "Amparos contra proyectos sin manifestación de impacto ambiental",
            "ambito": "Federal",
            "rubro": "Derecho humano al medio ambiente sano — exigibilidad directa",
            "texto_resumen": (
                "El derecho al medio ambiente sano (art. 4 CPEUM) es plenamente exigible. Los "
                "proyectos con impacto ambiental requieren manifestación previa (LGEEPA). Su omisión "
                "vicia de nulidad las autorizaciones y faculta a amparo por interés legítimo a "
                "comunidades afectadas."
            ),
            "registro_digital": "Amparos en revisión múltiples — línea consolidada",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029848",
            "fecha_publicacion": "2018-2024",
            "trascendencia": "Habilita amparos colectivos ambientales con interés legítimo amplio.",
            "explicacion": (
                "Vecinos, comunidades y organizaciones pueden ampararse contra proyectos sin MIA o "
                "con MIA deficiente. La SCJN ha reconocido interés legítimo amplio en materia "
                "ambiental."
            ),
            "etiquetas": ["medio ambiente", "MIA", "LGEEPA", "interés legítimo", "art. 4 CPEUM"],
        },
        {
            "id": "sen-016",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Energía",
            "tema": "Reforma energética 2021 y empresas privadas",
            "subtema": "Acciones de Inconstitucionalidad 64/2021 y acumuladas",
            "ambito": "Federal",
            "rubro": "Reforma a la LIE 2021 — declaratoria parcial de inconstitucionalidad",
            "texto_resumen": (
                "El Pleno declaró inconstitucionales diversos preceptos de la reforma 2021 a la Ley "
                "de la Industria Eléctrica que vulneraban libre competencia y certeza jurídica de "
                "los participantes privados; subsisten porciones compatibles con el régimen "
                "constitucional energético."
            ),
            "registro_digital": "AI 64/2021 — Pleno SCJN",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029765",
            "fecha_publicacion": "2022",
            "trascendencia": "Sentencia decisiva para sector privado de generación eléctrica.",
            "explicacion": (
                "Los proyectos eólicos y fotovoltaicos privados pueden invocar esta sentencia en "
                "amparos contra actos del CENACE que apliquen la versión declarada inconstitucional."
            ),
            "etiquetas": ["energía", "AI 64/2021", "LIE", "CENACE"],
        },
        {
            "id": "sen-017",
            "tipo": "sentencia hito",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil / Familia",
            "tema": "Divorcio incausado",
            "subtema": "Amparo Directo en Revisión 917/2009 y línea posterior",
            "ambito": "Federal — interpreta CCCDMX",
            "rubro": "Divorcio sin expresión de causa — desafectación del vínculo y dignidad",
            "texto_resumen": (
                "La voluntad unilateral de uno de los cónyuges es suficiente para disolver el "
                "matrimonio. Exigir causales específicas violenta el libre desarrollo de la "
                "personalidad y la dignidad. El divorcio incausado es constitucional y debe "
                "garantizarse en todas las entidades."
            ),
            "registro_digital": "ADR 917/2009 — Primera Sala",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029516",
            "fecha_publicacion": "2009-2015 (consolidada)",
            "trascendencia": "Cambia paradigma del divorcio en México: de divorcio-sanción a divorcio-remedio.",
            "explicacion": (
                "Hoy en CDMX (reforma 2008), Edomex y la mayoría de entidades el divorcio incausado "
                "es la regla. Donde aún subsisten causales (algunas entidades), el amparo es la vía."
            ),
            "etiquetas": ["divorcio incausado", "libre desarrollo personalidad", "ADR 917/2009"],
        },
        {
            "id": "sen-018",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Acceso a la información",
            "tema": "Datos personales y protección reforzada",
            "subtema": "Amparo en Revisión 1100/2015 — datos personales sensibles",
            "ambito": "Federal",
            "rubro": "Datos personales — autodeterminación informativa como derecho humano",
            "texto_resumen": (
                "La autodeterminación informativa es derecho humano (art. 16 CPEUM párrafo segundo). "
                "El tratamiento de datos personales por entes públicos o privados requiere "
                "consentimiento, finalidad lícita y proporcionalidad. Los datos sensibles tienen "
                "protección reforzada."
            ),
            "registro_digital": "AR 1100/2015 y línea consolidada",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031960",
            "fecha_publicacion": "2015-2023",
            "trascendencia": "Base para litigios de protección de datos contra empresas y gobierno.",
            "explicacion": (
                "Marco aplicable a litigios sobre uso indebido de información personal, brechas de "
                "seguridad, perfilamientos y biometría. INAI es vía administrativa; amparo si hay "
                "violación grave."
            ),
            "etiquetas": ["datos personales", "INAI", "autodeterminación informativa", "art. 16 CPEUM"],
        },
        {
            "id": "sen-019",
            "tipo": "sentencia hito",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Civil / Procesal",
            "tema": "Notificaciones — domicilio convencional vs. real",
            "subtema": "Línea de Colegiados Primer Circuito (CDMX)",
            "ambito": "Primer Circuito — CDMX",
            "rubro": "Notificación personal — preeminencia del domicilio real cuando consta en autos",
            "texto_resumen": (
                "Aunque exista domicilio convencional pactado, si en autos consta el domicilio real "
                "del demandado y el convencional resulta inhábil, el actuario debe notificar en el "
                "real para garantizar emplazamiento efectivo y derecho de audiencia."
            ),
            "registro_digital": "Tesis del Primer Circuito — múltiples colegiados civiles",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2030925",
            "fecha_publicacion": "Línea consolidada",
            "trascendencia": "Defensa nuclear contra emplazamientos ficticios.",
            "explicacion": (
                "En juicios ejecutivos y especiales hipotecarios, el demandado que no fue notificado "
                "personalmente y no tuvo oportunidad real de defensa puede pedir nulidad del "
                "emplazamiento. Ofrecer pruebas del domicilio real anteriores al juicio."
            ),
            "etiquetas": ["notificación", "emplazamiento", "domicilio real", "Primer Circuito"],
        },
        {
            "id": "sen-020",
            "tipo": "sentencia hito",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Costas en juicio mercantil — tasación",
            "subtema": "Línea del Primer y Segundo Circuito (CDMX y Edomex)",
            "ambito": "Primer y Segundo Circuito",
            "rubro": "Costas mercantiles — base de cuantificación y arancel aplicable",
            "texto_resumen": (
                "Las costas en juicio mercantil se cuantifican con base en el monto efectivamente "
                "condenado y conforme al arancel local vigente al momento de cuantificarlas. La "
                "condena en costas presupone temeridad o vencimiento total."
            ),
            "registro_digital": "Línea de Colegiados — múltiples",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031803",
            "fecha_publicacion": "Línea consolidada",
            "trascendencia": "Marco práctico para pretensión y oposición a costas.",
            "explicacion": (
                "El acreedor que gana en ejecutivo debe solicitar tasación con arancel actualizado. "
                "El deudor debe oponerse cuando la cuantificación excede el monto del juicio o "
                "aplica arancel inadecuado."
            ),
            "etiquetas": ["costas", "tasación", "arancel", "mercantil"],
        },
        {
            "id": "sen-021",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Electoral-Político",
            "tema": "Paridad de género",
            "subtema": "Acciones de Inconstitucionalidad sobre paridad",
            "ambito": "Federal",
            "rubro": "Paridad de género — principio constitucional transversal",
            "texto_resumen": (
                "La paridad (art. 41 CPEUM tras reforma 2019) es principio constitucional transversal "
                "que aplica a candidaturas, integración de órganos colegiados de poder, gabinetes y "
                "todos los espacios de toma de decisiones públicas."
            ),
            "registro_digital": "Acciones de Inconstitucionalidad múltiples — Pleno SCJN",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031441",
            "fecha_publicacion": "2020-2024",
            "trascendencia": "Marco para impugnación de procesos electorales y nombramientos.",
            "explicacion": (
                "Reforma 'Paridad en Todo' (2019). Aplica a Congresos, alcaldías, gabinetes y "
                "organismos autónomos. Las omisiones se combaten por amparo o juicio electoral."
            ),
            "etiquetas": ["paridad", "género", "art. 41 CPEUM", "elecciones"],
        },
        {
            "id": "sen-022",
            "tipo": "sentencia hito",
            "instancia": "Pleno SCJN",
            "jerarquia": 1,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / Reforma Judicial",
            "tema": "Reforma Judicial 2024 — control de constitucionalidad",
            "subtema": "Resoluciones del Pleno sobre la reforma judicial",
            "ambito": "Federal",
            "rubro": "Reforma Judicial 2024 — elección popular de jueces y reconfiguración SCJN",
            "texto_resumen": (
                "La reforma constitucional al Poder Judicial publicada el 15-IX-2024 reconfiguró "
                "íntegramente la SCJN, instauró elección popular de personas juzgadoras federales y "
                "creó el Tribunal de Disciplina Judicial. Las controversias e impugnaciones contra "
                "su implementación marcan la transición a la Duodécima Época del Semanario."
            ),
            "registro_digital": "Decreto publicado en DOF 15-IX-2024 + resoluciones de Pleno",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2030692",
            "fecha_publicacion": "2024-2026",
            "trascendencia": "Reforma estructural que cambia paradigma del Poder Judicial mexicano.",
            "explicacion": (
                "La Duodécima Época ('De la Justicia Pluricultural, la Igualdad Sustantiva y la "
                "Inclusión en México') inicia con la nueva integración. El Pleno actual ha iniciado "
                "líneas de precedentes obligatorios en su nuevo formato. Hay que monitorear cada "
                "nueva publicación viernes en SJF."
            ),
            "etiquetas": ["reforma judicial 2024", "Duodécima Época", "elección popular", "TDJ"],
        },

        # ============================================================
        # B L O Q U E  N U E V O  —  T E S I S  1 2 ª  É P O C A  (2026)
        # REGISTROS VERIFICADOS EN SJF2 EN VIVO
        # ============================================================
        {
            "id": "civ-arr-004",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Arrendamiento",
            "subtema": "Consignación de llaves no libera de pago",
            "ambito": "Federal",
            "rubro": ("ARRENDAMIENTO. LA CONSIGNACIÓN DE LLAVES DEL INMUEBLE ARRENDADO EXHIBIDAS "
                      "MEDIANTE ESCRITO ANTE EL ÓRGANO JURISDICCIONAL NO LIBERA AL DEMANDADO DEL "
                      "PAGO DE RENTAS, MANTENIMIENTO, SERVICIOS DE GAS Y AGUA, SI NO ACREDITA "
                      "HABER IMPULSADO EL PROCEDIMIENTO."),
            "texto_resumen": (
                "El arrendatario que pretende terminar el contrato consignando las llaves debe "
                "impulsar la notificación al arrendador. Sin ese impulso procesal, sigue obligado "
                "al pago de rentas y servicios."
            ),
            "registro_digital": "2031626",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031626",
            "fecha_publicacion": "2025-2026",
            "fuente_publicacion": "Semanario Judicial de la Federación — VERIFICADO",
            "trascendencia": "Defensa del arrendador contra inquilinos que abandonan sin notificar.",
            "explicacion": (
                "Inquilino que entrega llaves debe pedir actuario para notificar, no basta exhibirlas. "
                "Arrendador puede seguir cobrando hasta que el procedimiento esté impulsado."
            ),
            "etiquetas": ["arrendamiento", "consignación llaves", "12a Época"],
        },
        {
            "id": "civ-arr-005",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Arrendamiento",
            "subtema": "Aviso de terminación — cómputo de plazo",
            "ambito": "CDMX",
            "rubro": ("CONTRATO DE ARRENDAMIENTO POR TIEMPO INDETERMINADO PARA PREDIOS URBANOS. "
                      "LA OPORTUNIDAD DEL AVISO PARA DARLO POR CONCLUIDO DEBE COMPUTARSE EN DÍAS "
                      "HÁBILES, A MENOS QUE LAS PARTES RENUNCIEN A ESE DERECHO."),
            "texto_resumen": (
                "El aviso de terminación de arrendamiento por tiempo indeterminado se computa en "
                "días HÁBILES por defecto. Solo si las partes pactaron expresamente días naturales, "
                "aplica esa modalidad."
            ),
            "registro_digital": "2024563",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2024563",
            "fecha_publicacion": "2022",
            "fuente_publicacion": "Gaceta del SJF — VERIFICADO",
            "trascendencia": "Define plazo real para desocupación en CDMX.",
            "explicacion": (
                "Confusión frecuente: muchos contratos asumen días naturales sin pactarlo. El plazo "
                "es hábil. Hay que dar el aviso anticipándose."
            ),
            "etiquetas": ["arrendamiento CDMX", "aviso terminación", "días hábiles"],
        },
        {
            "id": "civ-hip-004",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Novena Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Juicio hipotecario",
            "subtema": "Apelación en efecto devolutivo",
            "ambito": "CDMX",
            "rubro": ("JUICIO ESPECIAL HIPOTECARIO, APELACIÓN EN EL. DEBE ADMITIRSE EN EL EFECTO "
                      "DEVOLUTIVO CONFORME AL ARTÍCULO 714 DEL CÓDIGO DE PROCEDIMIENTOS CIVILES "
                      "PARA EL DISTRITO FEDERAL."),
            "texto_resumen": (
                "Las apelaciones interlocutorias en el juicio especial hipotecario CDMX se admiten "
                "en efecto devolutivo, sin suspender la ejecución, conforme al art. 714 CPCDMX."
            ),
            "registro_digital": "162554",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/162554",
            "fecha_publicacion": "Novena Época",
            "fuente_publicacion": "Semanario Judicial de la Federación — VERIFICADO",
            "trascendencia": "Acreedor mantiene ejecución pese a apelaciones del deudor.",
            "explicacion": (
                "Defensa del banco/acreedor: las apelaciones no detienen el remate. El deudor debe "
                "ir por amparo indirecto si quiere suspender."
            ),
            "etiquetas": ["hipotecario", "apelación", "art. 714 CPCDMX", "efecto devolutivo"],
        },
        {
            "id": "civ-hip-005",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Novena Época",
            "vigencia": "vigente",
            "materia": "Civil",
            "tema": "Juicio hipotecario",
            "subtema": "Ejecución limitada al bien hipotecado",
            "ambito": "Federal",
            "rubro": ("JUICIO HIPOTECARIO. ES JURÍDICAMENTE IMPOSIBLE DESPACHAR EJECUCIÓN EN UN "
                      "INMUEBLE DISTINTO DEL BIEN MATERIA DE LA CONDENA."),
            "texto_resumen": (
                "La acción real hipotecaria solo permite ejecutar sobre el bien hipotecado. No "
                "puede ampliarse a otros bienes del deudor mediante convenios anteriores a la "
                "sentencia."
            ),
            "registro_digital": "180865",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/180865",
            "fecha_publicacion": "Novena Época",
            "fuente_publicacion": "SJF — VERIFICADO",
            "trascendencia": "Límite de garantía real del juicio hipotecario.",
            "explicacion": (
                "El acreedor que quiera ir contra otros bienes debe abrir vía ordinaria adicional. "
                "Defensa del deudor: oponer la limitación si el ejecutor intenta otros inmuebles."
            ),
            "etiquetas": ["hipotecario", "acción real", "ejecución limitada"],
        },
        {
            "id": "fam-div-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Civil / Familia",
            "tema": "Divorcio sin expresión de causa",
            "subtema": "Procedencia del recurso de revocación",
            "ambito": "CDMX",
            "rubro": ("DIVORCIO SIN EXPRESIÓN DE CAUSA. PROCEDENCIA DEL RECURSO DE REVOCACIÓN "
                      "CONTRA LAS RESOLUCIONES DICTADAS DURANTE SU SUSTANCIACIÓN."),
            "texto_resumen": (
                "Las resoluciones dictadas durante la sustanciación del divorcio sin causa admiten "
                "recurso de revocación conforme a los arts. 685, 685 bis y 691 del CPC para CDMX."
            ),
            "registro_digital": "2031170",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031170",
            "fecha_publicacion": "2025-2026",
            "fuente_publicacion": "SJF — VERIFICADO",
            "trascendencia": "Vía expedita contra resoluciones intermedias en divorcio incausado CDMX.",
            "explicacion": (
                "Antes era confusa la vía. Ahora con esta tesis se aplica revocación. Permite revisar "
                "rápidamente medidas provisionales sobre alimentos o convivencia."
            ),
            "etiquetas": ["divorcio incausado", "revocación", "CDMX", "12a Época"],
        },
        {
            "id": "fam-div-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Civil / Familia",
            "tema": "Divorcio sin expresión de causa",
            "subtema": "Amparo directo contra sentencia",
            "ambito": "Federal",
            "rubro": ("AMPARO DIRECTO. PROCEDE CONTRA LA SENTENCIA QUE DECLARA LA DISOLUCIÓN DEL "
                      "VÍNCULO MATRIMONIAL EN UN JUICIO DE DIVORCIO SIN EXPRESIÓN DE CAUSA Y "
                      "RESUELVE PROVISIONALMENTE SOBRE LOS ALIMENTOS U OTRAS CUESTIONES INHERENTES."),
            "texto_resumen": (
                "La sentencia de divorcio sin expresión de causa que resuelve sobre alimentos "
                "provisionales o cuestiones inherentes es definitiva para efectos del amparo directo."
            ),
            "registro_digital": "2029853",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029853",
            "fecha_publicacion": "2024-2025",
            "fuente_publicacion": "SJF — VERIFICADO",
            "trascendencia": "Define vía de impugnación: amparo directo, no indirecto.",
            "explicacion": (
                "Importante para no equivocarse de vía. Si tu sentencia incluye medidas sobre "
                "alimentos: amparo directo. Si solo es disolución limpia: dependerá del caso."
            ),
            "etiquetas": ["divorcio incausado", "amparo directo", "alimentos"],
        },
        {
            "id": "fam-com-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Civil / Familia",
            "tema": "Pensión compensatoria",
            "subtema": "Inversión de carga probatoria",
            "ambito": "Federal",
            "rubro": ("INVERSIÓN DE LA CARGA DE LA PRUEBA EN MATERIA FAMILIAR. CUANDO SE DEMANDA "
                      "UNA PENSIÓN COMPENSATORIA Y SE PRODUCE AQUÉLLA, LA PERSONA JUZGADORA TIENE "
                      "EL DEBER DE HACERLO SABER EXPRESA Y OPORTUNAMENTE A LA PARTE SOBRE LA "
                      "QUE RECAE."),
            "texto_resumen": (
                "En juicios de pensión compensatoria, cuando opera la inversión de carga probatoria, "
                "el juez tiene deber DE OFICIO de notificar formalmente a la parte sobre la que "
                "recae para garantizar defensa adecuada."
            ),
            "registro_digital": "2031387",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031387",
            "fecha_publicacion": "2025-2026",
            "fuente_publicacion": "SJF — VERIFICADO",
            "trascendencia": "Garantía procesal en juicios de compensación / pensión.",
            "explicacion": (
                "Defensa del deudor alimentario: si no le informaron expresamente la inversión, "
                "puede pedir nulidad de actuaciones. Defensa del acreedor: solicitar al juez que "
                "haga la notificación formal."
            ),
            "etiquetas": ["pensión compensatoria", "carga probatoria", "12a Época"],
        },
        {
            "id": "fis-cfd-002",
            "tipo": "jurisprudencia",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Fiscal",
            "tema": "Comprobantes fiscales (CFDI)",
            "subtema": "69-B — recurso de revocación y buzón tributario",
            "ambito": "Federal",
            "rubro": ("RECURSO DE REVOCACIÓN CONTRA LA RESOLUCIÓN FINAL PREVISTA EN EL ARTÍCULO "
                      "69-B, PÁRRAFO CUARTO, DEL CFF. EL PLAZO PARA INTERPONERLO COMIENZA A "
                      "PARTIR DE SU NOTIFICACIÓN A TRAVÉS DEL BUZÓN TRIBUTARIO."),
            "texto_resumen": (
                "El plazo de 30 días para interponer recurso de revocación contra resolución "
                "definitiva del 69-B se computa desde notificación por buzón tributario, no desde "
                "publicación en DOF."
            ),
            "registro_digital": "2031931",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031931",
            "fecha_publicacion": "2025-2026",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Define cómputo de plazo para defensa contra inclusión definitiva en EFOS.",
            "explicacion": (
                "Hay que monitorear el buzón tributario. Cuenta el plazo desde recepción ahí, no "
                "desde publicación DOF. Crítico para no perder defensa."
            ),
            "etiquetas": ["69-B CFF", "recurso revocación", "buzón tributario", "EFOS"],
        },
        {
            "id": "fis-cfd-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Fiscal",
            "tema": "Comprobantes fiscales (CFDI)",
            "subtema": "Materialidad — fundar y motivar",
            "ambito": "Federal",
            "rubro": ("PRESUNCIÓN DE INEXISTENCIA DE OPERACIONES AMPARADAS EN COMPROBANTES "
                      "FISCALES. DEBER DE FUNDAR Y MOTIVAR LA DECISIÓN DE REVERTIR LA CARGA "
                      "PROBATORIA PARA ACREDITAR SU MATERIALIDAD."),
            "texto_resumen": (
                "El SAT no puede simplemente requerir materialidad; debe fundar y motivar "
                "específicamente las razones por las que presume inexistencia. Sin esa "
                "fundamentación, la inversión de carga es inválida."
            ),
            "registro_digital": "2031350",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031350",
            "fecha_publicacion": "2025-2026",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Defensa fuerte para contribuyentes auditados.",
            "explicacion": (
                "Si el SAT no detalla por qué presume inexistencia (red flag específico), su "
                "requerimiento es nulo. Cuestionar fundamentación es el primer paso del litigio."
            ),
            "etiquetas": ["69-B", "materialidad", "fundamentación", "12a Época"],
        },
        {
            "id": "fis-cfd-004",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Fiscal",
            "tema": "Comprobantes fiscales (CFDI)",
            "subtema": "Nulidad EFOS — efectos sobre proveedor",
            "ambito": "Federal",
            "rubro": ("PRESUNCIÓN DE INEXISTENCIA DE OPERACIONES. CONSECUENCIA DE LA NULIDAD DE "
                      "LA RESOLUCIÓN QUE INCLUYE A UN PROVEEDOR EN EL LISTADO DE EMPRESAS QUE "
                      "FACTURAN OPERACIONES SIMULADAS (EFOS)."),
            "texto_resumen": (
                "Cuando se obtiene la nulidad de la resolución que incluyó al proveedor en EFOS "
                "definitivas, esa nulidad debe surtir efectos respecto del contribuyente que "
                "deducción afectada."
            ),
            "registro_digital": "2031349",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031349",
            "fecha_publicacion": "2025-2026",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Cadena de protección para contribuyentes que dedujeron con proveedores listados.",
            "explicacion": (
                "Si tu proveedor logra que le quiten de EFOS por sentencia firme, tú puedes "
                "invocarlo para recuperar deducciones rechazadas. Defensa colectiva."
            ),
            "etiquetas": ["EFOS", "nulidad", "deducciones", "12a Época"],
        },
        {
            "id": "pen-ppo-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Prisión preventiva oficiosa",
            "subtema": "Víctima — falta de legitimación para impugnar cese",
            "ambito": "Federal",
            "rubro": ("PRISIÓN PREVENTIVA OFICIOSA. LA VÍCTIMA U OFENDIDO DEL DELITO CARECE DE "
                      "LEGITIMACIÓN PARA IMPUGNAR EN SEDE CONSTITUCIONAL SU CESE, AL NO TENER "
                      "INCORPORADA A SU ESFERA JURÍDICA ALGÚN DERECHO QUE LA FACULTE."),
            "texto_resumen": (
                "La víctima no puede impugnar por amparo la liberación del imputado cuando se cesa "
                "la PPO. No hay derecho subjetivo a que el imputado permanezca en prisión preventiva."
            ),
            "registro_digital": "2032107",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032107",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Restringe vía de víctima contra liberaciones por exceso de plazo.",
            "explicacion": (
                "Tras PPO cesada (más de 2 años sin sentencia, por ejemplo), la víctima no puede "
                "ampararse. Su vía es civil/coadyuvancia para impulsar el proceso, no constitucional."
            ),
            "etiquetas": ["PPO", "víctima", "legitimación", "12a Época"],
        },
        {
            "id": "pen-ppo-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Prisión preventiva oficiosa",
            "subtema": "Cese cuando MP no prueba prolongación",
            "ambito": "Federal",
            "rubro": ("PRISIÓN PREVENTIVA OFICIOSA. SU CESE ORDENADO CUANDO EL MINISTERIO PÚBLICO "
                      "NO PRUEBA NI JUSTIFICA SU PROLONGACIÓN, PARA EFECTOS DE QUE SE DEBATA LA "
                      "IMPOSICIÓN DE OTRAS MEDIDAS CAUTELARES MENOS RESTRICTIVAS."),
            "texto_resumen": (
                "Al solicitar prolongación de PPO, el MP tiene carga probatoria. Si no la cumple, "
                "el juez debe cesar la PPO y reabrir debate sobre medidas cautelares alternativas."
            ),
            "registro_digital": "2032108",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032108",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Defensa decisiva contra prolongación automática de PPO.",
            "explicacion": (
                "Cuando MP solicita prolongación sin justificar, la defensa debe exigir prueba "
                "concreta. Sin ella, opera el cese y se debate medida alterna (caución, brazalete, "
                "presentación periódica)."
            ),
            "etiquetas": ["PPO", "prolongación", "carga probatoria MP", "12a Época"],
        },
        {
            "id": "pen-rep-001",
            "tipo": "jurisprudencia",
            "instancia": "Plenos Regionales",
            "jerarquia": 3,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Reparación del daño",
            "subtema": "Compensación directa como parte de reparación integral",
            "ambito": "Federal",
            "rubro": ("COMPENSACIÓN DIRECTA. PROCEDE CONDENAR AL SENTENCIADO A SU PAGO COMO PARTE "
                      "DE LA REPARACIÓN INTEGRAL DEL DAÑO."),
            "texto_resumen": (
                "En sentencias condenatorias, el juez puede y debe condenar a compensación directa "
                "al sentenciado como componente autónomo de la reparación integral del daño, "
                "adicional a indemnización y otras medidas."
            ),
            "registro_digital": "2032030",
            "tesis_clave": "PR.P.T.CN. J/8 P (12a.)",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032030",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "Semanario Judicial de la Federación 12a Época — VERIFICADO",
            "trascendencia": "Marca tendencia hacia reparación robusta a víctimas de delito.",
            "explicacion": (
                "La víctima puede pedir expresamente compensación directa además de indemnización. "
                "El juez tiene base jurisprudencial para ordenarla."
            ),
            "etiquetas": ["reparación del daño", "compensación", "víctima", "Plenos Regionales"],
        },
        {
            "id": "amp-cui-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / DDHH",
            "tema": "Derecho humano al cuidado",
            "subtema": "Reconocimiento e interés legítimo",
            "ambito": "Federal",
            "rubro": ("DERECHO HUMANO AL CUIDADO. IMPONE OBLIGACIONES DE CUYO CUMPLIMIENTO DEPENDE "
                      "DIRECTAMENTE EL BIENESTAR DE LAS PERSONAS E INDIRECTAMENTE, POR "
                      "INTERDEPENDENCIA, EL EJERCICIO EFECTIVO DE OTROS DERECHOS HUMANOS."),
            "texto_resumen": (
                "El cuidado se reconoce como derecho humano autónomo. El Estado tiene obligación "
                "de garantizarlo mediante políticas públicas, infraestructura social y reconocimiento "
                "del trabajo de cuidado no remunerado."
            ),
            "registro_digital": "2032085",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032085",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Pieza inaugural de un nuevo derecho humano en México.",
            "explicacion": (
                "Marco para litigios sobre obligaciones del Estado en guarderías, cuidado de "
                "personas mayores, discapacidad y omisiones legislativas absolutas."
            ),
            "etiquetas": ["derecho al cuidado", "12a Época", "DDHH", "cuidadoras"],
        },
        {
            "id": "amp-cui-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / DDHH",
            "tema": "Derecho humano al cuidado",
            "subtema": "Interés legítimo para combatir omisiones legislativas",
            "ambito": "Federal",
            "rubro": ("DERECHO HUMANO AL CUIDADO. LAS MUJERES QUE REALIZAN CUIDADOS SIMPLES O "
                      "COTIDIANOS NO REMUNERADOS TIENEN INTERÉS LEGÍTIMO PARA RECLAMAR OMISIONES "
                      "LEGISLATIVAS ABSOLUTAS QUE IMPIDAN SU PLENO EJERCICIO."),
            "texto_resumen": (
                "Las mujeres que realizan trabajo de cuidados no remunerados tienen interés "
                "legítimo, sin necesidad de afectación individualizada estricta, para promover "
                "amparo contra omisiones legislativas absolutas en la materia."
            ),
            "registro_digital": "2032086",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032086",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Abre vía de amparo colectivo a millones de cuidadoras.",
            "explicacion": (
                "Estrategia colectiva: amparos contra ausencia de legislación de cuidados. "
                "Beneficia particularmente a mujeres de bajos ingresos que sostienen familia."
            ),
            "etiquetas": ["cuidado", "interés legítimo", "omisión legislativa", "perspectiva género"],
        },
        {
            "id": "amp-gen-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Constitucional / DDHH",
            "tema": "Perspectiva de género interseccional",
            "subtema": "Acceso a la justicia para mujeres cuidadoras",
            "ambito": "Federal",
            "rubro": ("ACCESO A LA JUSTICIA EN CONDICIONES DE IGUALDAD SUSTANTIVA. LAS "
                      "MANIFESTACIONES DE MUJERES QUE AFIRMAN REALIZAR LABORES DE CUIDADO NO "
                      "REMUNERADAS DEBEN VALORARSE CON PERSPECTIVA DE GÉNERO INTERSECCIONAL."),
            "texto_resumen": (
                "En procesos donde las mujeres afirman dedicarse a labores de cuidado, sus "
                "manifestaciones deben valorarse con perspectiva de género interseccional "
                "(considerando clase, edad, etnia, discapacidad y otros factores)."
            ),
            "registro_digital": "2032067",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032067",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Estándar probatorio favorable para mujeres en juicios civiles, familiares, laborales.",
            "explicacion": (
                "En alimentos, pensiones, compensación por trabajo doméstico y otros litigios, "
                "el juez debe creer y valorar con flexibilidad las declaraciones de mujeres "
                "cuidadoras."
            ),
            "etiquetas": ["perspectiva género", "interseccional", "acceso justicia", "12a Época"],
        },

        # ============================================================
        # B L O Q U E   3   —   T E S I S   V E R I F I C A D A S
        # Búsqueda en lote en SJF — 2026-05-18
        # ============================================================
        {
            "id": "mer-pag-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Títulos de crédito — pagaré",
            "subtema": "Acción causal — pagaré como prueba del contrato",
            "ambito": "Federal",
            "rubro": ("ACCIÓN CAUSAL. SU EJERCICIO PARA EL COBRO DE UN TÍTULO DE CRÉDITO PUEDE "
                      "SUSTENTARSE EN EL CONTRATO CONTENIDO EN EL PAGARÉ, DERIVADO DEL OTORGAMIENTO "
                      "DE UN PRÉSTAMO A CORTO PLAZO."),
            "texto_resumen": (
                "Si el pagaré pierde eficacia ejecutiva o el acreedor decide no usar la vía ejecutiva, "
                "puede ejercer acción causal con el pagaré como prueba documental del contrato "
                "subyacente."
            ),
            "registro_digital": "2024056",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2024056",
            "fecha_publicacion": "2022",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Salvavidas para acreedores cuando el pagaré tiene vicios formales.",
            "explicacion": "Si no procede el ejecutivo, vía ordinaria con el pagaré como documental.",
            "etiquetas": ["pagaré", "acción causal", "ordinario mercantil"],
        },
        {
            "id": "mer-pag-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Títulos de crédito — pagaré",
            "subtema": "Pagarés seriados — lugar de pago",
            "ambito": "Federal",
            "rubro": ("PAGARÉS SERIADOS. ANTE LA AUSENCIA DE \"LUGAR DE PAGO\" EN UNO DE ÉSTOS, "
                      "DEBE ATENDERSE A LO PACTADO EN OTRO DIVERSO DONDE SÍ SE SEÑALÓ."),
            "texto_resumen": (
                "Cuando se emiten varios pagarés seriados y solo uno tiene lugar de pago expreso, "
                "ese lugar aplica a toda la serie por integración."
            ),
            "registro_digital": "2019464",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2019464",
            "fecha_publicacion": "2019",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Importante en mutuos con tabla de pagos a 12, 24 o 36 meses.",
            "explicacion": "Defensa contra excepción de pagaré sin lugar de pago en serie.",
            "etiquetas": ["pagaré", "pagarés seriados", "lugar de pago"],
        },
        {
            "id": "mer-eje-002",
            "tipo": "jurisprudencia",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Juicio ejecutivo mercantil",
            "subtema": "Improcedencia — análisis oficioso en amparo directo",
            "ambito": "Federal",
            "rubro": ("IMPROCEDENCIA DE LA VÍA EJECUTIVA MERCANTIL. AL TRATARSE DE UN PRESUPUESTO "
                      "PROCESAL, PUEDE ANALIZARSE DE OFICIO EN EL JUICIO DE AMPARO DIRECTO."),
            "texto_resumen": (
                "La improcedencia de la vía ejecutiva mercantil es presupuesto procesal y puede "
                "analizarse de oficio incluso en amparo directo, aunque las instancias previas no "
                "lo hayan abordado a fondo."
            ),
            "registro_digital": "2025924",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2025924",
            "fecha_publicacion": "2023",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Defensa de última instancia para deudores ejecutados con documentos viciados.",
            "explicacion": "Aun perdiendo en primera y segunda instancia, en amparo directo se puede plantear.",
            "etiquetas": ["vía ejecutiva mercantil", "amparo directo", "oficio"],
        },
        {
            "id": "mer-eje-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Juicio ejecutivo mercantil",
            "subtema": "Mora — fecha de actualización",
            "ambito": "Federal",
            "rubro": ("MORA EN EL JUICIO EJECUTIVO MERCANTIL. SE ACTUALIZA CON MOTIVO DE LA "
                      "INTERPELACIÓN FORMULADA EN EL EMPLAZAMIENTO Y NO EN LA FECHA DE "
                      "VENCIMIENTO ESTABLECIDA EN EL PAGARÉ BASE DE LA ACCIÓN."),
            "texto_resumen": (
                "Cuando el pagaré señala genéricamente como lugar de pago una ciudad, la mora no "
                "se actualiza con el vencimiento sino con la interpelación en el emplazamiento "
                "judicial."
            ),
            "registro_digital": "2031591",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2031591",
            "fecha_publicacion": "2025-2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Define desde cuándo corren intereses moratorios.",
            "explicacion": "Pagarés con lugar genérico: los intereses moratorios corren desde emplazamiento, no desde vencimiento.",
            "etiquetas": ["mora", "intereses moratorios", "interpelación", "12a Época"],
        },
        {
            "id": "civ-fid-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Civil-Mercantil",
            "tema": "Fideicomisos",
            "subtema": "Fideicomiso de garantía y mediación — avalúo",
            "ambito": "Federal",
            "rubro": ("FIDEICOMISO EN GARANTÍA DERIVADO DE UN CONVENIO DE MEDIACIÓN. CUANDO SE "
                      "PRETENDA SU EJECUCIÓN JUDICIAL DEBE EXHIBIRSE EL AVALÚO DEL BIEN INMUEBLE "
                      "DADO EN GARANTÍA, AL SER UN ELEMENTO DE LA ACCIÓN CONFORME AL ARTÍCULO "
                      "1414 BIS DEL CÓDIGO DE COMERCIO."),
            "texto_resumen": (
                "Para ejecutar judicialmente fideicomiso de garantía constituido por convenio de "
                "mediación, el actor DEBE exhibir avalúo del bien al promover. Sin avalúo, la "
                "acción es improcedente."
            ),
            "registro_digital": "2027244",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2027244",
            "fecha_publicacion": "2023-2024",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Requisito formal estricto para ejecutar fideicomiso de garantía vía mediación.",
            "explicacion": "Antes de demandar ejecución hay que conseguir avalúo de perito autorizado.",
            "etiquetas": ["fideicomiso garantía", "mediación", "art. 1414 bis Cco", "avalúo"],
        },
        {
            "id": "mer-soc-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Sociedades mercantiles",
            "subtema": "Velo corporativo — supuestos y excepcionalidad",
            "ambito": "Federal",
            "rubro": ("VELO CORPORATIVO. PROCEDE LEVANTARLO COMO MEDIDA EXCEPCIONAL CUANDO SE "
                      "ACREDITE QUE SE UTILIZA CON EL PROPÓSITO DE DEFRAUDAR A TERCEROS."),
            "texto_resumen": (
                "El levantamiento del velo corporativo es medida excepcional, procedente solo "
                "cuando se acredita el uso fraudulento de la personalidad jurídica para defraudar "
                "a terceros. La carga probatoria recae en quien lo solicita."
            ),
            "registro_digital": "2029944",
            "tesis_clave": "1a. II/2025 (11a.)",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029944",
            "fecha_publicacion": "14 de febrero de 2025",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Doctrina vigente más reciente de Primera Sala sobre velo corporativo.",
            "explicacion": (
                "Para ganar levantamiento: probar (i) abuso de la forma societaria, (ii) intención "
                "fraudulenta, (iii) daño a tercero. Sin esos tres elementos, se niega."
            ),
            "etiquetas": ["velo corporativo", "1a. II/2025", "fraude"],
        },
        {
            "id": "mer-soc-003",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Mercantil",
            "tema": "Sociedades mercantiles",
            "subtema": "Velo corporativo en medida cautelar prejudicial",
            "ambito": "Federal",
            "rubro": ("VELO CORPORATIVO. POR REGLA GENERAL NO PUEDE ORDENARSE SU LEVANTAMIENTO "
                      "COMO MEDIDA CAUTELAR EN UN PROCEDIMIENTO PREJUDICIAL."),
            "texto_resumen": (
                "El levantamiento del velo corporativo no procede como medida cautelar prejudicial. "
                "Requiere juicio de fondo con plena oportunidad probatoria, dado su carácter "
                "excepcional y la severidad de sus consecuencias."
            ),
            "registro_digital": "2029943",
            "tesis_clave": "1a. I/2025 (11a.)",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029943",
            "fecha_publicacion": "14 de febrero de 2025",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Cierra la puerta a levantamientos cautelares de personalidad.",
            "explicacion": "Acreedor no puede pedir embargo cautelar contra socios; debe esperar juicio de fondo.",
            "etiquetas": ["velo corporativo", "1a. I/2025", "medida cautelar"],
        },
        {
            "id": "pen-cad-002",
            "tipo": "jurisprudencia",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Cadena de custodia",
            "subtema": "Responsabilidad de la Fiscalía aun con datos del inculpado",
            "ambito": "Federal",
            "rubro": ("CADENA DE CUSTODIA. ES RESPONSABILIDAD EXCLUSIVA DE LOS SERVIDORES "
                      "PÚBLICOS DE LA FISCALÍA, INCLUSO RESPECTO DE DATOS O MEDIOS DE PRUEBA "
                      "APORTADOS POR EL INCULPADO O SU DEFENSA."),
            "texto_resumen": (
                "Conforme al CNPP, la cadena de custodia recae siempre en la Fiscalía, incluso "
                "respecto de evidencia aportada por la defensa. La defensa NO carga con su "
                "preservación; el MP debe registrarla y custodiarla."
            ),
            "registro_digital": "2027962",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2027962",
            "fecha_publicacion": "2024",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Reforma carga: la defensa puede aportar evidencia sin temor a romper cadena.",
            "explicacion": "Defensa puede aportar peritajes, fotos, audios sin asumir custodia formal.",
            "etiquetas": ["cadena custodia", "CNPP", "Fiscalía", "evidencia defensa"],
        },
        {
            "id": "pen-cad-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Décima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Cadena de custodia",
            "subtema": "Transgresión no torna ilícita la prueba",
            "ambito": "Federal",
            "rubro": ("CADENA DE CUSTODIA. SU TRANSGRESIÓN NO TORNA ILÍCITOS LOS DATOS DE PRUEBA."),
            "texto_resumen": (
                "La ruptura de cadena de custodia NO convierte automáticamente en ilícita la prueba; "
                "solo afecta su valor probatorio. El juez debe ponderar la magnitud de la ruptura."
            ),
            "registro_digital": "2021845",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2021845",
            "fecha_publicacion": "2020",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Matiza la regla de exclusión: cadena rota = valor probatorio reducido, no exclusión.",
            "explicacion": "Defensa: argumentar valor cero por ruptura. Acusación: defender la prueba a pesar de la ruptura.",
            "etiquetas": ["cadena custodia", "valor probatorio", "exclusión"],
        },
        {
            "id": "pen-tor-001",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Tortura",
            "subtema": "Tortura de coimputado e investigación oficiosa",
            "ambito": "Federal",
            "rubro": ("TORTURA. OBLIGACIONES DE LA AUTORIDAD JUDICIAL CUANDO EL QUEJOSO ALEGA "
                      "QUE SU COIMPUTADO FUE TORTURADO PARA HACER IMPUTACIONES EN SU CONTRA."),
            "texto_resumen": (
                "Cuando el quejoso alega que su coimputado fue torturado para incriminarlo, la "
                "autoridad judicial tiene obligación oficiosa de investigar, aunque la víctima "
                "directa de la tortura sea otra persona."
            ),
            "registro_digital": "2029150",
            "tesis_clave": "1a./J. 118/2024 (11a.)",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029150",
            "fecha_publicacion": "05 de julio de 2024",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Expande deber de investigar tortura a casos de coimputados.",
            "explicacion": "Si tu cliente está siendo incriminado por coimputado torturado: invocar esta tesis para excluir prueba.",
            "etiquetas": ["tortura", "coimputado", "1a./J. 118/2024", "investigación oficiosa"],
        },
        {
            "id": "pen-pru-002",
            "tipo": "jurisprudencia",
            "instancia": "Primera Sala SCJN",
            "jerarquia": 2,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Penal",
            "tema": "Prueba ilícita",
            "subtema": "Exclusión por detención arbitraria del coimputado",
            "ambito": "Federal",
            "rubro": ("DERECHO A LA EXCLUSIÓN DE PRUEBA ILÍCITA. CUANDO EL QUEJOSO ALEGA QUE LA "
                      "DECLARACIÓN INCRIMINATORIA DE SU COIMPUTADO FUE OBTENIDA COMO CONSECUENCIA "
                      "DE QUE ÉSTE PADECIÓ UNA DETENCIÓN ARBITRARIA, PROCEDE ANALIZAR ESE "
                      "ARGUMENTO EN EL JUICIO DE AMPARO."),
            "texto_resumen": (
                "El quejoso puede solicitar exclusión de declaración del coimputado cuando ésta "
                "deriva de detención arbitraria de aquél. El amparo debe analizar la legalidad "
                "de la detención del coimputado."
            ),
            "registro_digital": "2028424",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2028424",
            "fecha_publicacion": "2024",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Línea expansiva de exclusión de prueba derivada.",
            "explicacion": "Fruto del árbol envenenado se extiende a declaraciones de terceros detenidos arbitrariamente.",
            "etiquetas": ["prueba ilícita", "coimputado", "detención arbitraria", "árbol envenenado"],
        },
        {
            "id": "amp-sus-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Amparo",
            "tema": "Suspensión",
            "subtema": "Suspensión contra medidas cautelares civiles/mercantiles",
            "ambito": "Federal",
            "rubro": ("SUSPENSIÓN EN EL JUICIO DE AMPARO. PUEDE CONCEDERSE CONTRA MEDIDAS "
                      "CAUTELARES DICTADAS EN PROCESOS CIVILES O MERCANTILES CUANDO NO PRESERVAN "
                      "LA MATERIA DEL JUICIO DE ORIGEN O IMPONEN RESTRICCIONES GENÉRICAS QUE "
                      "AFECTAN INJUSTIFICADAMENTE DERECHOS HUMANOS."),
            "texto_resumen": (
                "Las medidas cautelares civiles o mercantiles (embargos, restricciones, prohibiciones) "
                "pueden suspenderse vía amparo si exceden lo necesario para preservar la materia "
                "o son genéricas y afectan derechos humanos."
            ),
            "registro_digital": "2032118",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032118",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Defensa contra embargos abusivos y medidas precautorias excesivas.",
            "explicacion": "Embargado puede amparar si la medida es desproporcionada o no preserva materia del juicio.",
            "etiquetas": ["suspensión amparo", "medida cautelar", "12a Época"],
        },
        {
            "id": "amp-sus-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Amparo",
            "tema": "Suspensión",
            "subtema": "Suspensión con efectos restitutorios — incapacidad médica",
            "ambito": "Federal",
            "rubro": ("SUSPENSIÓN EN AMPARO INDIRECTO CON EFECTOS RESTITUTORIOS. PROCEDE PARA LA "
                      "EXPEDICIÓN DE UNA INCAPACIDAD MÉDICA CUANDO SU EFECTO ES TRANSITORIO Y "
                      "EXISTE UN ESTADO CLÍNICO INCAPACITANTE PREVIAMENTE ACREDITADO."),
            "texto_resumen": (
                "La suspensión puede tener efectos restitutorios (no solo conservativos): obligar al "
                "IMSS/ISSSTE a expedir incapacidad médica si hay estado clínico acreditado."
            ),
            "registro_digital": "2032066",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032066",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Innovadora: suspensión que ORDENA actuar, no solo paraliza.",
            "explicacion": "Útil para trabajadores cuyas incapacidades son negadas pese a sustento médico.",
            "etiquetas": ["suspensión restitutoria", "incapacidad médica", "IMSS", "12a Época"],
        },
        {
            "id": "lab-des-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Laboral",
            "tema": "Despido injustificado",
            "subtema": "Carga patrón cuando alega rescisión justificada posterior",
            "ambito": "Federal",
            "rubro": ("RELACIÓN LABORAL. CUANDO LA PERSONA TRABAJADORA MANIFIESTA QUE FUE "
                      "DESPEDIDA INJUSTIFICADAMENTE EN CIERTA FECHA Y EL PATRÓN ARGUMENTA QUE "
                      "AQUÉLLA SUBSISTIÓ Y QUE POSTERIORMENTE LA RESCINDIÓ DE FORMA JUSTIFICADA, "
                      "LE CORRESPONDE PROBAR AMBOS HECHOS."),
            "texto_resumen": (
                "Si el patrón niega el despido alegado y agrega rescisión justificada posterior, "
                "tiene carga de probar AMBOS: que la relación subsistió tras la fecha del supuesto "
                "despido y que la rescisión posterior fue justificada."
            ),
            "registro_digital": "2029731",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029731",
            "fecha_publicacion": "2024-2025",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Carga doble para patrón que cambia versión durante el juicio.",
            "explicacion": "Estrategia trabajadora: forzar al patrón a esa narrativa, queda con carga reforzada.",
            "etiquetas": ["despido", "rescisión", "carga probatoria patrón"],
        },
        {
            "id": "lab-ren-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Laboral",
            "tema": "Renuncia laboral",
            "subtema": "Hora de terminación — carga del patrón",
            "ambito": "Federal",
            "rubro": ("RENUNCIA. CORRESPONDE A LA PARTE DEMANDADA PERFECCIONARLA CON ALGÚN MEDIO "
                      "DE PRUEBA, CUANDO EXISTA CONTROVERSIA RESPECTO DE LA HORA DE TERMINACIÓN "
                      "DEL VÍNCULO LABORAL Y ÉSTA NO CONSTE EN EL ESCRITO RELATIVO."),
            "texto_resumen": (
                "Si el patrón ofrece renuncia sin hora exacta y el trabajador alega despido a "
                "cierta hora, el patrón debe acreditar con prueba adicional la hora de la renuncia."
            ),
            "registro_digital": "2028640",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2028640",
            "fecha_publicacion": "2024",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Cuestionamiento a renuncias forzadas con fechas/horas imprecisas.",
            "explicacion": "Trabajador debe declarar hora exacta del despido; patrón tendrá que probar hora distinta.",
            "etiquetas": ["renuncia", "hora despido", "carga probatoria"],
        },
        {
            "id": "lab-ren-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Laboral",
            "tema": "Renuncia laboral",
            "subtema": "Veracidad — carga reforzada si trabajador iba a jubilarse",
            "ambito": "Federal",
            "rubro": ("RENUNCIA. PARA QUE SEA VEROSÍMIL Y, POR ENDE, TENGA EFICACIA DEMOSTRATIVA "
                      "PLENA, CORRESPONDE AL PATRÓN PROBAR QUE REÚNE LAS CONDICIONES DE CERTEZA "
                      "Y LOS ELEMENTOS MÍNIMOS QUE REFLEJEN LA VOLUNTAD, AUTONOMÍA Y "
                      "ESPONTANEIDAD DEL TRABAJADOR, SI ESTÁ PRÓXIMO A JUBILARSE."),
            "texto_resumen": (
                "Cuando el trabajador estaba próximo a adquirir derechos jubilatorios, la renuncia "
                "exigida pasa por estándar reforzado de veracidad: voluntad, autonomía y "
                "espontaneidad demostradas con prueba sólida."
            ),
            "registro_digital": "2027058",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2027058",
            "fecha_publicacion": "2023-2024",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Protección antes de jubilación: renuncias sospechosas no pasan.",
            "explicacion": "Defensa trabajadora: si estaba a meses/años de jubilarse, atacar renuncia por falta de espontaneidad.",
            "etiquetas": ["renuncia", "jubilación", "veracidad", "carga reforzada"],
        },
        {
            "id": "civ-ext-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Civil-Penal",
            "tema": "Extinción de dominio",
            "subtema": "Comportarse como dueño — concepto",
            "ambito": "Federal",
            "rubro": ("ACCIÓN DE EXTINCIÓN DE DOMINIO. CONCEPTO DE \"COMPORTARSE U OSTENTARSE "
                      "COMO DUEÑO\", PARA LOS EFECTOS DE LA LEY FEDERAL DE EXTINCIÓN DE DOMINIO "
                      "(ABROGADA)."),
            "texto_resumen": (
                "El \"comportarse u ostentarse como dueño\" requiere acreditar actos materiales "
                "objetivos: posesión, administración, disposición, sin que baste la mera "
                "titularidad registral."
            ),
            "registro_digital": "2024407",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2024407",
            "fecha_publicacion": "2022",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Estándar para acreditar legitimación pasiva en extinción.",
            "explicacion": "Defensa: probar que tu cliente solo era titular registral, no se ostentaba como dueño.",
            "etiquetas": ["extinción dominio", "ostentación", "comportamiento", "LFED"],
        },
        {
            "id": "amp-sal-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Administrativo / Salud",
            "tema": "Derecho humano a la salud",
            "subtema": "Reasignación sexual — IMSS",
            "ambito": "Federal",
            "rubro": ("REASIGNACIÓN SEXUAL. EL INSTITUTO MEXICANO DEL SEGURO SOCIAL (IMSS) DEBE "
                      "GARANTIZAR A LAS PERSONAS TRANSEXUALES LA POSIBILIDAD DE OPTAR POR UNA "
                      "INTERVENCIÓN MÉDICA HORMONAL, QUIRÚRGICA O AMBAS."),
            "texto_resumen": (
                "El IMSS debe garantizar a personas transexuales acceso a tratamientos hormonales, "
                "quirúrgicos o combinados de reasignación. La negativa es violatoria del derecho "
                "a la salud y la identidad."
            ),
            "registro_digital": "2032111",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032111",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Hito de inclusión sanitaria de personas trans en sistema social.",
            "explicacion": "Personas trans que sean derechohabientes pueden ampararse contra negativas del IMSS.",
            "etiquetas": ["reasignación sexual", "IMSS", "personas trans", "12a Época"],
        },
        {
            "id": "amp-sal-002",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Administrativo / Salud",
            "tema": "Derecho humano a la salud",
            "subtema": "Efectos del amparo contra negativa de cirugía",
            "ambito": "Federal",
            "rubro": ("REASIGNACIÓN SEXUAL. EFECTOS DEL AMPARO CONCEDIDO CONTRA LA NEGATIVA DEL "
                      "INSTITUTO MEXICANO DEL SEGURO SOCIAL (IMSS) DE PRACTICAR LA CIRUGÍA "
                      "RELATIVA."),
            "texto_resumen": (
                "Cuando se concede amparo contra negativa de cirugía de reasignación, los efectos "
                "obligan al IMSS a programar y practicar el procedimiento conforme a estándares "
                "médicos, no a meramente analizar la petición."
            ),
            "registro_digital": "2032110",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032110",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Define alcance positivo del amparo en salud.",
            "explicacion": "Sentencia de amparo no es solo papel: ordena ejecutar la cirugía con plazos.",
            "etiquetas": ["amparo efectos", "cirugía", "salud", "12a Época"],
        },
        {
            "id": "amp-sal-003",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Duodécima Época",
            "vigencia": "vigente",
            "materia": "Administrativo / Salud",
            "tema": "Derecho humano a la salud",
            "subtema": "Autonomía IMSS limitada por DDHH",
            "ambito": "Federal",
            "rubro": ("DERECHO HUMANO A LA SALUD. EL MARGEN DE AUTONOMÍA DEL INSTITUTO MEXICANO "
                      "DEL SEGURO SOCIAL PARA ESTABLECER POLÍTICAS PÚBLICAS, ESTUDIOS Y CAMPAÑAS "
                      "EN ESA MATERIA, NO IMPLICA QUE ESTÉ EXENTO DE GARANTIZARLO A LAS "
                      "PERSONAS DERECHOHABIENTES."),
            "texto_resumen": (
                "La autonomía técnica y administrativa del IMSS para diseñar políticas no lo "
                "exime de garantizar el derecho a la salud individualmente. Las políticas no "
                "pueden ser pretexto para negar atención."
            ),
            "registro_digital": "2032087",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2032087",
            "fecha_publicacion": "2026",
            "fuente_publicacion": "SJF 12a Época — VERIFICADO",
            "trascendencia": "Marco general contra negativas burocráticas del IMSS.",
            "explicacion": "El IMSS no puede escudarse en 'no está en cuadro básico' o 'no es política'.",
            "etiquetas": ["salud", "IMSS", "autonomía limitada", "12a Época"],
        },
        {
            "id": "amp-eje-001",
            "tipo": "tesis aislada",
            "instancia": "Tribunales Colegiados de Circuito",
            "jerarquia": 4,
            "epoca": "Undécima Época",
            "vigencia": "vigente",
            "materia": "Amparo",
            "tema": "Amparo contra normas generales",
            "subtema": "Efectos reflejos del fallo",
            "ambito": "Federal",
            "rubro": ("AMPARO CONTRA NORMAS GENERALES. SU NEGATIVA VINCULA Y TIENE EFECTOS "
                      "REFLEJOS EN OTROS LITIGIOS DONDE LA MISMA PERSONA SOLICITE, EN EJERCICIO "
                      "DEL CONTROL DIFUSO O DE CONSTITUCIONALIDAD Y CONVENCIONALIDAD EX OFFICIO, "
                      "LA INAPLICACIÓN DE AQUÉLLAS."),
            "texto_resumen": (
                "Si una persona pierde amparo contra norma general, esa cosa juzgada le aplica "
                "también en otros litigios donde pretenda inaplicación de la misma norma por "
                "control difuso."
            ),
            "registro_digital": "2029745",
            "url_sjf": "https://sjf2.scjn.gob.mx/detalle/tesis/2029745",
            "fecha_publicacion": "2024-2025",
            "fuente_publicacion": "Gaceta SJF — VERIFICADO",
            "trascendencia": "Cierra puerta a relitigar inconstitucionalidad por vías paralelas.",
            "explicacion": "Si ya perdiste amparo contra norma, no insistas vía control difuso en otro juicio.",
            "etiquetas": ["amparo normas", "control difuso", "efectos reflejos"],
        },
        {'id': 'auto-2032124', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Civil', 'tema': 'Juicio hipotecario', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'CRÉDITOS HIPOTECARIOS OTORGADOS POR LAS INSTITUCIONES FINANCIERAS A SUS PERSONAS TRABAJADORAS. EL ESTUDIO SOBRE LA MODIFICACIÓN DE LAS CLÁUSULAS QUE CONTENGAN UN BENEFICIO OTORGADO DERIVADO DE LA RELACIÓN LABORAL PROCEDE EN ESTA VÍA.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032124', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032124', 'fecha_publicacion': 'viernes 15 de mayo de 2026 10:20 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Juicio hipotecario', 'actualización automática']},
        {'id': 'auto-2032145', 'tipo': 'jurisprudencia', 'instancia': 'Segunda Sala SCJN', 'jerarquia': 2, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Penal', 'tema': 'Tortura', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'TORTURA Y OTROS TRATOS O PENAS CRUELES, INHUMANOS O DEGRADANTES EN EL ESTADO DE TAMAULIPAS. EL ARTÍCULO 3 DE LA LEY RELATIVA ES INCONSTITUCIONAL, AL ESTABLECER LA APLICACIÓN SUPLETORIA DE LA LEY GENERAL DE LA MATERIA.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032145', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032145', 'fecha_publicacion': 'viernes 15 de mayo de 2026 10:20 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Tortura', 'actualización automática']},
        {'id': 'auto-2032122', 'tipo': 'jurisprudencia', 'instancia': 'Segunda Sala SCJN', 'jerarquia': 2, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Administrativo', 'tema': 'Responsabilidad administrativa de servidores públicos', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'CANCELACIÓN DE LICENCIA PARA CONDUCIR. LA PREVISTA EN LOS ARTÍCULOS 168 Y 26, FRACCIÓN XXX, DE LA LEY DE MOVILIDAD Y SEGURIDAD VIAL DEL ESTADO DE PUEBLA, ES INCONSTITUCIONAL.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032122', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032122', 'fecha_publicacion': 'viernes 15 de mayo de 2026 10:20 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Responsabilidad administrativa de servidores públicos', 'actualización automática']},
        {'id': 'auto-2032131', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Administrativo / Salud', 'tema': 'Derecho humano a la salud', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'PENSIONES EN EL ESTADO DE JALISCO. EL ARTÍCULO 52 DE LA LEY DEL INSTITUTO DE PENSIONES DE LA ENTIDAD FEDERATIVA VIOLA EL DERECHO A LA SEGURIDAD SOCIAL.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032131', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032131', 'fecha_publicacion': 'viernes 15 de mayo de 2026 10:20 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Derecho humano a la salud', 'actualización automática']},
        {'id': 'auto-2032177', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Administrativo', 'tema': 'Responsabilidad administrativa de servidores públicos', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'PRUEBAS EN EL JUICIO CONTENCIOSO ADMINISTRATIVO FEDERAL. EL ARTÍCULO 40, PÁRRAFO SEGUNDO, DE LA LEY FEDERAL DE PROCEDIMIENTO CONTENCIOSO ADMINISTRATIVO NO VIOLA EL DERECHO DE ACCESO A LA JUSTICIA.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032177', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032177', 'fecha_publicacion': 'viernes 22 de mayo de 2026 10:27 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Responsabilidad administrativa de servidores públicos', 'actualización automática']},
        {'id': 'auto-2032154', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Constitucional / DDHH', 'tema': 'Perspectiva de género', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'COMPENSACIÓN ECONÓMICA. ELEMENTOS MÍNIMOS QUE LA PERSONA JUZGADORA DEBE CONSIDERAR PARA MOTIVAR LA RESOLUCIÓN QUE LA CUANTIFICA, CON PERSPECTIVA DE GÉNERO.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032154', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032154', 'fecha_publicacion': 'viernes 22 de mayo de 2026 10:27 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Perspectiva de género', 'actualización automática']},
        {'id': 'auto-2032184', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Constitucional / DDHH', 'tema': 'Perspectiva de género', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'VIOLENCIA FAMILIAR. CUANDO LA VÍCTIMA SEA UNA PERSONA MENOR DE EDAD Y SE ALEGUE ALIENACIÓN O MANIPULACIÓN PARENTAL, EL ÓRGANO JURISDICCIONAL DEBE ORDENAR LA PRÁCTICA DE PRUEBAS PERICIALES PARA VERIFICAR SI SE ACTUALIZA DICHA CONDICIÓN.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032184', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032184', 'fecha_publicacion': 'viernes 22 de mayo de 2026 10:27 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Perspectiva de género', 'actualización automática']},
        {'id': 'auto-2032198', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Mercantil', 'tema': 'Juicio ejecutivo mercantil', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'GARANTÍA PARA QUE SIGA SURTIENDO EFECTOS LA SUSPENSIÓN EN AMPARO INDIRECTO. ES EXIGIBLE A LA PERSONA MORAL PRIVADA DECLARADA EN QUIEBRA, AL NO ACTUALIZARSE ALGÚN SUPUESTO LEGAL PARA EXENTAR SU EXHIBICIÓN.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032198', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032198', 'fecha_publicacion': 'viernes 29 de mayo de 2026 10:34 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Juicio ejecutivo mercantil', 'actualización automática']},
        {'id': 'auto-2032212', 'tipo': 'jurisprudencia', 'instancia': 'Plenos Regionales', 'jerarquia': 3, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Amparo', 'tema': 'Suspensión', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'SUSPENSIÓN PROVISIONAL CON EFECTOS RESTITUTORIOS. ES IMPROCEDENTE CONTRA LA NEGATIVA MATERIAL A RECIBIR UNA SOLICITUD DE BASIFICACIÓN LABORAL, PORQUE SU CONCESIÓN IMPLICA UN BENEFICIO TOTAL QUE DEJA SIN MATERIA EL JUICIO DE AMPARO.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032212', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032212', 'fecha_publicacion': 'viernes 29 de mayo de 2026 10:34 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Suspensión', 'actualización automática']},
        {'id': 'auto-2032235', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Civil', 'tema': 'Arrendamiento', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'PRESUNCIÓN DE PAGO EN ARRENDAMIENTO DE BIENES INMUEBLES. NO SE ACTUALIZA CUANDO EN EL CONTRATO SE PACTAN MODALIDADES ESPECÍFICAS DE PAGO Y EL ARRENDATARIO LAS VARÍA DE MANERA UNILATERAL.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032235', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032235', 'fecha_publicacion': 'viernes 05 de junio de 2026 10:11 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Arrendamiento', 'actualización automática']},
        {'id': 'auto-2032218', 'tipo': 'jurisprudencia', 'instancia': 'Segunda Sala SCJN', 'jerarquia': 2, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Administrativo', 'tema': 'Agua y servicios públicos', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'CONCESIONES MINERAS. LOS ARTÍCULOS 15 DE LA LEY DE MINERÍA Y DÉCIMO TRANSITORIO, DEL DECRETO PUBLICADO EN EL DIARIO OFICIAL DE LA FEDERACIÓN EL 8 DE MAYO DE 2023, NO TRANSGREDEN EL DERECHO HUMANO A LA IGUALDAD.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032218', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032218', 'fecha_publicacion': 'viernes 05 de junio de 2026 10:11 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Agua y servicios públicos', 'actualización automática']},
        {'id': 'auto-2032225', 'tipo': 'jurisprudencia', 'instancia': 'Segunda Sala SCJN', 'jerarquia': 2, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Penal', 'tema': 'Reparación del daño', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'DAÑO MORAL. NO DEBE CONSIDERARSE LA SITUACIÓN ECONÓMICA DE LA VÍCTIMA PARA CUANTIFICAR SUS CONSECUENCIAS EXTRAPATRIMONIALES.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032225', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032225', 'fecha_publicacion': 'viernes 05 de junio de 2026 10:11 h', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Reparación del daño', 'actualización automática']},
        {'id': 'auto-2032233', 'tipo': 'tesis aislada', 'instancia': 'Tribunales Colegiados de Circuito', 'jerarquia': 4, 'epoca': 'Duodécima Época', 'vigencia': 'vigente', 'materia': 'Administrativo', 'tema': 'Responsabilidad administrativa de servidores públicos', 'subtema': 'Actualización automática semanal', 'ambito': 'Federal', 'rubro': 'PROCEDIMIENTO DE SEPARACIÓN DEL CARGO PREVISTO EN LOS ARTÍCULOS 209 Y 210 DE LA LEY ORGÁNICA DEL PODER JUDICIAL DEL ESTADO DE PUEBLA (ABROGADA). AL NO PREVER LA FORMA COMO DEBE INICIARSE NI LOS TÉRMINOS DE SU SUSTANCIACIÓN, LE ES APLICABLE EL DE RESPONSABILIDAD ADMINISTRATIVA.', 'texto_resumen': 'Criterio publicado esta semana en el Semanario Judicial de la Federación. Ver texto íntegro en el SJF mediante el enlace directo.', 'registro_digital': '2032233', 'url_sjf': 'https://sjf2.scjn.gob.mx/detalle/tesis/2032233', 'fecha_publicacion': 'viernes 05 de junio de 2026 10:11', 'fuente_publicacion': 'Semanario Judicial de la Federación — captura automática', 'trascendencia': 'Incorporada automáticamente en la actualización semanal. Pendiente de análisis editorial.', 'explicacion': 'Tesis nueva detectada por el robot semanal. Revisa el texto completo en el SJF.', 'etiquetas': ['Responsabilidad administrativa de servidores públicos', 'actualización automática']},
    ],
}


if __name__ == "__main__":
    print(f"Total de entradas: {len(ACERVO['entradas'])}")
    materias = {}
    for e in ACERVO["entradas"]:
        materias[e["materia"]] = materias.get(e["materia"], 0) + 1
    for m, c in sorted(materias.items()):
        print(f"  {m}: {c}")
