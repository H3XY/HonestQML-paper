#!/usr/bin/env bash
# Build the PDF and the arXiv upload bundle (arxiv.zip: main.tex, main.bbl, figures).
# arXiv compiles the source itself and needs the .bbl, not the .bib.
set -euo pipefail
cd "$(dirname "$0")"
tectonic -X compile --keep-intermediates main.tex
tectonic -X compile workshop.tex   # 8-page workshop version -> workshop.pdf
rm -f arxiv.zip
zip -q arxiv.zip main.tex main.bbl figures/*.png
echo "Built main.pdf and arxiv.zip ($(du -h arxiv.zip | cut -f1))"
