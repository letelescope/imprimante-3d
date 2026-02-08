#!/usr/bin/env python3
"""
convert_md_to_pdf.py
Convertit un fichier Markdown en PDF.

Usage:
  python convert_md_to_pdf.py README.md README.pdf
"""
from __future__ import annotations
import argparse
import sys
from markdown import markdown
from xhtml2pdf import pisa

DEFAULT_CSS = """<style>
body { font-family: DejaVu Sans, Arial, sans-serif; padding: 1em; }
h1,h2,h3,h4 { color: #222; }
pre { background: #f5f5f5; padding: 0.75em; overflow: auto; }
code { font-family: monospace; }
table { border-collapse: collapse; }
table, th, td { border: 1px solid #ccc; padding: 6px; }
</style>"""

def md_to_pdf(md_text: str, output_path: str) -> int:
    html_body = markdown(md_text, extensions=["fenced_code", "codehilite", "tables"])
    html = f"<html><head><meta charset='utf-8'>{DEFAULT_CSS}</head><body>{html_body}</body></html>"
    with open(output_path, "wb") as out_file:
        pisa_status = pisa.CreatePDF(html, dest=out_file)
    return 0 if not pisa_status.err else 1

def main(argv=None):
    parser = argparse.ArgumentParser(description="Convertit un fichier Markdown en PDF.")
    parser.add_argument("input", help="Fichier Markdown source (.md)")
    parser.add_argument("output", nargs="?", help="Fichier PDF de sortie (.pdf)") 
    args = parser.parse_args(argv)

    input_path = args.input
    output_path = args.output or input_path.rsplit('.', 1)[0] + ".pdf"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            md_text = f.read()
    except Exception as e:
        print(f"Erreur lecture '{input_path}': {e}", file=sys.stderr)
        return 2

    rc = md_to_pdf(md_text, output_path)
    if rc == 0:
        print(f"PDF créé: {output_path}")
    else:
        print("Erreur lors de la génération du PDF", file=sys.stderr)
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
