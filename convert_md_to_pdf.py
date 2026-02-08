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
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #24292e;
  background: #fff;
  padding: 2em;
  max-width: 900px;
  margin: 0 auto;
}
h1, h2, h3, h4, h5, h6 {
  margin: 1.5em 0 0.5em 0;
  font-weight: 600;
  line-height: 1.25;
  color: #24292e;
  border-bottom: none;
}
h1 { font-size: 2em; padding-bottom: 0.3em; border-bottom: 1px solid #eaecef; }
h2 { font-size: 1.5em; padding-bottom: 0.3em; border-bottom: 1px solid #eaecef; }
h3 { font-size: 1.25em; }
h4 { font-size: 1em; }
h5 { font-size: 0.875em; }
h6 { font-size: 0.85em; color: #6a737d; }
p { margin: 0.5em 0 1em 0; }
ul, ol { margin: 0.5em 0 1em 1.5em; }
li { margin: 0.25em 0; }
blockquote {
  padding: 0.5em 1em;
  margin: 0.5em 0 1em 0;
  border-left: 0.25em solid #dfe2e5;
  background: #f6f8fa;
  color: #6a737d;
}
code {
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.85em;
  background: #f6f8fa;
  padding: 0.2em 0.4em;
  margin: 0;
  border-radius: 3px;
}
pre {
  background: #f6f8fa;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  padding: 1em;
  margin: 0.5em 0 1em 0;
  overflow: auto;
  line-height: 1.45;
}
pre code {
  background: none;
  padding: 0;
  margin: 0;
  border-radius: 0;
  font-size: 13px;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.5em 0 1em 0;
}
table th, table td {
  border: 1px solid #dfe2e5;
  padding: 0.75em;
  text-align: left;
}
table th {
  background: #f6f8fa;
  font-weight: 600;
}
a { color: #0366d6; text-decoration: none; }
a:hover { text-decoration: underline; }
strong { font-weight: 600; }
em { font-style: italic; }
hr { background: #e1e4e8; border: 0; height: 2px; margin: 2em 0; }
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
