---
name: pdf-operations
description: Export Malaysian tax working papers to PDF, annotate General Ledger documents, and generate print-ready reports for LHDN submission. Covers markdown-to-PDF pipeline, Chrome headless printing, PyMuPDF annotations, and Win32com Excel-to-PDF automation.
---

# PDF Operations Skill

## Purpose

Export tax working papers to PDF, annotate GL documents, and generate print-ready reports suitable for LHDN Form C submission.

## Available Scripts

All scripts are located in the `scripts/` folder.

### `export_to_pdf.py`

Exports markdown files to PDF using WeasyPrint via an HTML-to-PDF conversion pipeline.

- Reads `.md` files from working paper folders
- Parses markdown to HTML using the `markdown` library
- Applies professional CSS styling
- Handles file ordering based on naming convention (TC_, AA_, CA_, etc.)
- Outputs a single merged PDF or per-file PDFs

**Usage:**
```bash
python scripts/export_to_pdf.py --folder "CLIENT YA 2025" --output output.pdf
```

### `export_to_print_pdf.py`

Generates a print-optimized HTML file (~25KB) designed for Ctrl+P browser printing.

- Embeds all content inline (no external dependencies)
- Applies print-specific CSS (page breaks, margins, headers/footers)
- Comprehensive formatting matching LHDN professional standards
- Output opens directly in browser for immediate printing

**Usage:**
```bash
python scripts/export_to_print_pdf.py --folder "CLIENT YA 2025" --output print_ready.html
```

### `generate_pdf_direct.py`

Uses Chrome or Edge in headless CLI mode to print HTML directly to PDF.

- Invokes `chrome --headless --print-to-pdf` or equivalent Edge command
- Accepts an HTML file or URL as input
- Produces high-fidelity PDF matching browser rendering
- Suitable for automated batch PDF generation

**Usage:**
```bash
python scripts/generate_pdf_direct.py --input tax_viewer.html --output working_papers.pdf
```

### `annotate_gl.py`

Adds PDF annotations to General Ledger documents using PyMuPDF (`fitz`).

- Searches for text strings within PDF pages
- Places tickmark symbols at matched locations
- Applies color overlays (highlight, underline, strikethrough)
- Supports annotation export to a summary log

**Usage:**
```bash
python scripts/annotate_gl.py --pdf general_ledger.pdf --terms "depreciation,provision"
```

### `annotate_gl_v2.py`

Enhanced GL annotation script with improved capabilities.

- Improved text search with fuzzy matching tolerance
- Circle/box annotations around matched amounts
- Multi-color support (red, green, yellow highlights)
- Batch annotation from a reference list (e.g., add-back items)
- Outputs annotated PDF with annotation summary report

**Usage:**
```bash
python scripts/annotate_gl_v2.py --pdf gl.pdf --config annotations.json --output gl_annotated.pdf
```

### `print_kilat_ya2021.py`

Automates Excel-to-PDF conversion via Win32com COM automation (Windows only).

- Opens Excel workbooks using `win32com.client`
- Configures page setup (orientation, margins, print area, scaling)
- Prints specified sheets to PDF via the Windows print-to-PDF driver
- Handles multi-sheet workbooks with consistent formatting

**Usage:**
```bash
python scripts/print_kilat_ya2021.py --excel workbook.xlsx --sheets "CA,TC" --output output.pdf
```

## Key Capabilities

| Capability | Script | Library |
|---|---|---|
| Markdown to PDF | `export_to_pdf.py` | weasyprint, markdown |
| Print-ready HTML | `export_to_print_pdf.py` | markdown |
| Chrome headless PDF | `generate_pdf_direct.py` | subprocess (Chrome/Edge CLI) |
| GL PDF annotation | `annotate_gl.py`, `annotate_gl_v2.py` | PyMuPDF (fitz) |
| Excel to PDF | `print_kilat_ya2021.py` | win32com (Windows only) |

## Dependencies

```
weasyprint
PyMuPDF
markdown
pywin32  # Windows only, for win32com
```

Install with:
```bash
pip install weasyprint PyMuPDF markdown pywin32
```

## Notes

- Chrome or Edge must be installed for `generate_pdf_direct.py`
- `print_kilat_ya2021.py` requires Windows with Microsoft Excel installed
- All scripts assume working papers follow the standard folder structure defined in CLAUDE.md
- Output PDFs are formatted for A4 paper, suitable for physical filing and LHDN submission
