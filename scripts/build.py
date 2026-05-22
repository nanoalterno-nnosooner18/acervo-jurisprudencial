# -*- coding: utf-8 -*-
"""
Regenera los tres formatos del acervo usando rutas RELATIVAS.
Pensado para correr en GitHub Actions o en cualquier máquina.
Escribe los archivos en la carpeta padre de scripts/ (raíz del repo).
"""
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from gen_html import render_html
from gen_docx import make_doc
from gen_xlsx import make_xlsx

def main():
    html = render_html()
    (REPO_ROOT / "Acervo_Jurisprudencial.html").write_text(html, encoding="utf-8")
    (REPO_ROOT / "index.html").write_text(html, encoding="utf-8")
    make_doc().save(str(REPO_ROOT / "Acervo_Jurisprudencial.docx"))
    make_xlsx().save(str(REPO_ROOT / "Acervo_Jurisprudencial.xlsx"))
    print("Archivos regenerados en", REPO_ROOT)

if __name__ == "__main__":
    main()
