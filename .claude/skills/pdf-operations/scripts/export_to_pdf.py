#!/usr/bin/env python3
"""
Export Tax Working Papers to PDF
JATI KIRANA SDN BHD - YA 2025
"""

import os
import sys
import re
from pathlib import Path

# Try to import required libraries
try:
    from weasyprint import HTML, CSS
    from markdown import markdown
    WEASYPRINT_AVAILABLE = True
except ImportError:
    WEASYPRINT_AVAILABLE = False

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
BASE_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
OUTPUT_FILE = BASE_DIR / "JATI_KIRANA_YA2025_Tax_Working_Papers.pdf"

# Ordered list of files to include
FILE_ORDER = [
    # Cover and Main Tax Computation
    ("01_TAX_COMPUTATION", "TC_01_Cover_Page.md", "COVER PAGE"),
    ("01_TAX_COMPUTATION", "TC_02_Main_Tax_Computation.md", "MAIN TAX COMPUTATION"),
    ("01_TAX_COMPUTATION", "TC_03_Tax_Summary.md", "TAX SUMMARY"),
    ("01_TAX_COMPUTATION", "TC_04_CP204_Comparison.md", "CP204 COMPARISON"),

    # Analysis of Accounts (Schedule A)
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_01_Analysis_Summary.md", "ANALYSIS SUMMARY"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_02_Revenue_Analysis.md", "REVENUE ANALYSIS"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_03_Expenditure_Analysis.md", "EXPENDITURE ANALYSIS"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_04_Add_Back_Schedule.md", "ADD BACK SCHEDULE"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_05_Non_Taxable_Income.md", "NON-TAXABLE INCOME"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_06_Reconciliation.md", "RECONCILIATION"),

    # Capital Allowance (Schedule B)
    ("03_CAPITAL_ALLOWANCE", "CA_01_CA_Summary.md", "CA SUMMARY"),
    ("03_CAPITAL_ALLOWANCE", "CA_02_Plant_Machinery.md", "PLANT & MACHINERY"),
    ("03_CAPITAL_ALLOWANCE", "CA_03_Motor_Vehicles.md", "MOTOR VEHICLES"),
    ("03_CAPITAL_ALLOWANCE", "CA_04_Office_Equipment.md", "OFFICE EQUIPMENT"),
    ("03_CAPITAL_ALLOWANCE", "CA_05_Computer_Equipment.md", "COMPUTER EQUIPMENT"),
    ("03_CAPITAL_ALLOWANCE", "CA_06_Small_Value_Assets.md", "SMALL VALUE ASSETS"),
    ("03_CAPITAL_ALLOWANCE", "CA_07_Balancing_Adjustment.md", "BALANCING ADJUSTMENT"),
    ("03_CAPITAL_ALLOWANCE", "CA_08_CA_Brought_Forward.md", "CA BROUGHT FORWARD"),

    # Directors Details (Schedule C)
    ("04_DIRECTORS_DETAILS", "DD_01_Directors_Particulars.md", "DIRECTORS PARTICULARS"),
    ("04_DIRECTORS_DETAILS", "DD_02_Directors_Remuneration.md", "DIRECTORS REMUNERATION"),
    ("04_DIRECTORS_DETAILS", "DD_03_Directors_Interest.md", "DIRECTORS INTEREST"),

    # Shareholders Details (Schedule D)
    ("05_SHAREHOLDERS_DETAILS", "SH_01_Share_Capital_Info.md", "SHARE CAPITAL INFO"),
    ("05_SHAREHOLDERS_DETAILS", "SH_02_Shareholders_List.md", "SHAREHOLDERS LIST"),
    ("05_SHAREHOLDERS_DETAILS", "SH_03_Corporate_Shareholders.md", "CORPORATE SHAREHOLDERS"),
    ("05_SHAREHOLDERS_DETAILS", "SH_04_SME_Status_Verification.md", "SME STATUS"),

    # Beneficial Ownership (Schedule E)
    ("06_BENEFICIAL_OWNERSHIP", "BO_01_Beneficial_Owners_List.md", "BENEFICIAL OWNERS"),
    ("06_BENEFICIAL_OWNERSHIP", "BO_02_Ownership_Structure.md", "OWNERSHIP STRUCTURE"),
    ("06_BENEFICIAL_OWNERSHIP", "BO_03_Declaration.md", "DECLARATION"),

    # PBC & Query
    ("07_PBC_QUERY", "PBC_01_Document_Checklist.md", "PBC CHECKLIST"),
    ("07_PBC_QUERY", "PBC_02_Outstanding_Items.md", "OUTSTANDING ITEMS"),
    ("07_PBC_QUERY", "QRY_01_Query_List.md", "QUERY LIST"),
    ("07_PBC_QUERY", "QRY_02_Query_Response.md", "QUERY RESPONSE"),

    # Supporting Workings
    ("08_SUPPORTING_WORKINGS", "SW_01_Depreciation_vs_CA.md", "DEPRECIATION VS CA"),
    ("08_SUPPORTING_WORKINGS", "SW_02_Interest_Expense.md", "INTEREST EXPENSE"),
    ("08_SUPPORTING_WORKINGS", "SW_03_Related_Party_Trans.md", "RELATED PARTY"),
    ("08_SUPPORTING_WORKINGS", "SW_04_Losses_Summary.md", "LOSSES SUMMARY"),
    ("08_SUPPORTING_WORKINGS", "SW_09_CP204_Tax_Instalment.md", "CP204 TAX INSTALMENT"),

    # Prior Year Reference
    ("09_PRIOR_YEAR_REFERENCE", "PY_01_Prior_Year_Tax_Comp.md", "PRIOR YEAR TAX COMP"),
    ("09_PRIOR_YEAR_REFERENCE", "PY_02_Prior_Year_CA.md", "PRIOR YEAR CA"),
]

# Section headers for table of contents
SECTIONS = {
    "01_TAX_COMPUTATION": "SECTION 1: TAX COMPUTATION (MAIN)",
    "02_ANALYSIS_OF_ACCOUNTS": "SECTION 2: ANALYSIS OF ACCOUNTS (SCHEDULE A)",
    "03_CAPITAL_ALLOWANCE": "SECTION 3: CAPITAL ALLOWANCE (SCHEDULE B)",
    "04_DIRECTORS_DETAILS": "SECTION 4: DIRECTORS DETAILS (SCHEDULE C)",
    "05_SHAREHOLDERS_DETAILS": "SECTION 5: SHAREHOLDERS DETAILS (SCHEDULE D)",
    "06_BENEFICIAL_OWNERSHIP": "SECTION 6: BENEFICIAL OWNERSHIP (SCHEDULE E)",
    "07_PBC_QUERY": "SECTION 7: PBC & QUERY LIST",
    "08_SUPPORTING_WORKINGS": "SECTION 8: SUPPORTING WORKINGS",
    "09_PRIOR_YEAR_REFERENCE": "SECTION 9: PRIOR YEAR REFERENCE",
}

CSS_STYLES = """
@page {
    size: A4;
    margin: 2cm 1.5cm 2.5cm 1.5cm;

    @top-center {
        content: "JATI KIRANA SDN BHD - Tax Working Papers YA 2025";
        font-size: 9pt;
        color: #666;
        border-bottom: 0.5pt solid #ccc;
        padding-bottom: 5pt;
    }

    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 9pt;
        color: #666;
    }

    @bottom-right {
        content: "CONFIDENTIAL";
        font-size: 8pt;
        color: #999;
    }
}

@page :first {
    @top-center {
        content: "";
        border-bottom: none;
    }
}

@page toc {
    @top-center {
        content: "TABLE OF CONTENTS";
        font-size: 9pt;
        color: #666;
        border-bottom: 0.5pt solid #ccc;
        padding-bottom: 5pt;
    }
}

* {
    box-sizing: border-box;
}

body {
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #333;
}

/* Cover Page Styles */
.cover-page {
    page: first;
    page-break-after: always;
    text-align: center;
    padding-top: 150px;
}

.cover-page h1 {
    font-size: 28pt;
    color: #1a365d;
    margin-bottom: 20px;
}

.cover-page h2 {
    font-size: 18pt;
    color: #2c5282;
    margin-bottom: 40px;
}

.cover-page .details {
    font-size: 12pt;
    margin-top: 60px;
}

/* Table of Contents */
.toc {
    page: toc;
    page-break-after: always;
}

.toc h1 {
    font-size: 18pt;
    color: #1a365d;
    text-align: center;
    margin-bottom: 30px;
    border-bottom: 2pt solid #1a365d;
    padding-bottom: 10px;
}

.toc-section {
    font-weight: bold;
    font-size: 11pt;
    color: #1a365d;
    margin-top: 15px;
    margin-bottom: 5px;
    padding: 5px 0;
    border-bottom: 1px solid #e2e8f0;
}

.toc-item {
    font-size: 10pt;
    margin-left: 20px;
    padding: 3px 0;
    color: #4a5568;
}

/* Section Divider */
.section-divider {
    page-break-before: always;
    background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%);
    color: white;
    padding: 40px;
    text-align: center;
    margin: 0 -1.5cm;
    min-height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.section-divider h1 {
    font-size: 24pt;
    margin: 0;
    color: white;
    border: none;
}

.section-divider p {
    font-size: 12pt;
    margin-top: 10px;
    opacity: 0.9;
}

/* Content Styles */
.document {
    page-break-before: always;
}

.document:first-of-type {
    page-break-before: avoid;
}

.doc-header {
    background: #f7fafc;
    border-left: 4px solid #1a365d;
    padding: 10px 15px;
    margin-bottom: 20px;
}

.doc-header h2 {
    font-size: 14pt;
    color: #1a365d;
    margin: 0;
}

.doc-header .ref {
    font-size: 9pt;
    color: #718096;
}

h1 {
    font-size: 16pt;
    color: #1a365d;
    border-bottom: 2px solid #1a365d;
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 15px;
    page-break-after: avoid;
}

h2 {
    font-size: 13pt;
    color: #2c5282;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 5px;
    margin-top: 20px;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h3 {
    font-size: 11pt;
    color: #2d3748;
    margin-top: 15px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

h4 {
    font-size: 10pt;
    color: #4a5568;
    margin-top: 12px;
    margin-bottom: 8px;
}

p {
    margin-bottom: 10px;
    text-align: justify;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 9pt;
    page-break-inside: avoid;
}

thead {
    display: table-header-group;
}

th {
    background: #1a365d;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    border: 1px solid #1a365d;
}

td {
    padding: 6px 10px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) {
    background: #f7fafc;
}

tr:hover {
    background: #edf2f7;
}

/* Numeric columns right-aligned */
td:last-child, th:last-child {
    text-align: right;
}

/* Lists */
ul, ol {
    margin: 10px 0 10px 25px;
    padding: 0;
}

li {
    margin-bottom: 5px;
}

/* Code blocks */
pre {
    background: #1a202c;
    color: #e2e8f0;
    padding: 15px;
    border-radius: 5px;
    font-family: "Consolas", monospace;
    font-size: 9pt;
    overflow-x: auto;
    page-break-inside: avoid;
}

code {
    background: #edf2f7;
    padding: 2px 5px;
    border-radius: 3px;
    font-family: "Consolas", monospace;
    font-size: 9pt;
    color: #c53030;
}

pre code {
    background: none;
    padding: 0;
    color: inherit;
}

/* Horizontal rule */
hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 20px 0;
}

/* Strong and emphasis */
strong {
    color: #1a202c;
}

em {
    color: #4a5568;
}

/* Blockquote */
blockquote {
    border-left: 4px solid #4299e1;
    margin: 15px 0;
    padding: 10px 20px;
    background: #ebf8ff;
    color: #2c5282;
}

/* Notes and warnings */
.note {
    background: #fffaf0;
    border-left: 4px solid #ed8936;
    padding: 10px 15px;
    margin: 15px 0;
}

/* Totals row in tables */
tr.total td, tr:last-child td {
    font-weight: bold;
    border-top: 2px solid #1a365d;
}

/* Page break utilities */
.page-break {
    page-break-after: always;
}

.no-break {
    page-break-inside: avoid;
}

/* Print-specific */
@media print {
    body {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
}
"""

def read_markdown_file(filepath):
    """Read markdown file and return content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return None

def markdown_to_html(md_content):
    """Convert markdown to HTML."""
    # Use markdown library with extensions
    html = markdown(
        md_content,
        extensions=[
            'tables',
            'fenced_code',
            'toc',
            'nl2br',
            'sane_lists',
        ]
    )
    return html

def create_cover_page():
    """Create HTML for cover page."""
    return """
    <div class="cover-page">
        <div style="margin-top: 100px;">
            <h1>JATI KIRANA SDN BHD</h1>
            <h2>Company No: 724858-P</h2>
            <h2>Tax File No: C 2359253703</h2>
        </div>

        <div style="margin-top: 80px;">
            <h1 style="font-size: 32pt; border: 3px solid #1a365d; padding: 20px; display: inline-block;">
                FORM C<br>TAX COMPUTATION
            </h1>
        </div>

        <div style="margin-top: 60px;">
            <h2>YEAR OF ASSESSMENT 2025</h2>
            <p style="font-size: 14pt;">Basis Period: 01/07/2024 to 30/06/2025</p>
        </div>

        <div style="margin-top: 100px; font-size: 11pt; color: #666;">
            <p><strong>PREPARED BY:</strong></p>
            <p>_________________________________</p>
            <p style="margin-top: 30px;"><strong>REVIEWED BY:</strong></p>
            <p>_________________________________</p>
            <p style="margin-top: 30px;"><strong>DATE:</strong></p>
            <p>_________________________________</p>
        </div>

        <div style="position: absolute; bottom: 50px; left: 0; right: 0; text-align: center;">
            <p style="font-size: 10pt; color: #999;">CONFIDENTIAL - FOR INTERNAL USE ONLY</p>
        </div>
    </div>
    """

def create_toc(files_included):
    """Create table of contents HTML."""
    toc_html = """
    <div class="toc">
        <h1>TABLE OF CONTENTS</h1>
    """

    current_section = None
    page_num = 3  # Start after cover and TOC

    for folder, filename, title in files_included:
        section_name = SECTIONS.get(folder, folder)

        if folder != current_section:
            current_section = folder
            toc_html += f'<div class="toc-section">{section_name}</div>\n'

        toc_html += f'<div class="toc-item">{title}</div>\n'

    toc_html += "</div>"
    return toc_html

def create_section_divider(section_key):
    """Create section divider page."""
    section_name = SECTIONS.get(section_key, section_key)

    schedule_map = {
        "01_TAX_COMPUTATION": "Main Deliverable",
        "02_ANALYSIS_OF_ACCOUNTS": "Schedule A",
        "03_CAPITAL_ALLOWANCE": "Schedule B",
        "04_DIRECTORS_DETAILS": "Schedule C",
        "05_SHAREHOLDERS_DETAILS": "Schedule D",
        "06_BENEFICIAL_OWNERSHIP": "Schedule E",
        "07_PBC_QUERY": "Client Documentation",
        "08_SUPPORTING_WORKINGS": "Supporting Schedules",
        "09_PRIOR_YEAR_REFERENCE": "Reference Materials",
    }

    subtitle = schedule_map.get(section_key, "")

    return f"""
    <div class="section-divider">
        <h1>{section_name}</h1>
        <p>{subtitle}</p>
    </div>
    """

def generate_pdf():
    """Main function to generate PDF."""
    print("=" * 60)
    print("JATI KIRANA SDN BHD - Tax Working Papers Export")
    print("Year of Assessment 2025")
    print("=" * 60)
    print()

    if not WEASYPRINT_AVAILABLE:
        print("ERROR: Required libraries not installed.")
        print()
        print("Please install the required packages:")
        print("  pip install weasyprint markdown")
        print()
        print("On Windows, you may also need GTK3:")
        print("  Download from: https://github.com/nickvergessen/gtk-3-mingw-w64-pango-win32")
        return False

    # Build HTML document
    html_parts = []

    # Add cover page
    print("Creating cover page...")
    html_parts.append(create_cover_page())

    # Collect files that exist
    files_included = []
    for folder, filename, title in FILE_ORDER:
        filepath = BASE_DIR / folder / filename
        if filepath.exists():
            files_included.append((folder, filename, title))

    # Add table of contents
    print("Creating table of contents...")
    html_parts.append(create_toc(files_included))

    # Process each file
    current_section = None

    for folder, filename, title in files_included:
        filepath = BASE_DIR / folder / filename

        # Add section divider if new section
        if folder != current_section:
            current_section = folder
            section_name = SECTIONS.get(folder, folder)
            print(f"\n{section_name}")
            print("-" * 50)
            html_parts.append(create_section_divider(folder))

        print(f"  Processing: {filename}")

        md_content = read_markdown_file(filepath)
        if md_content:
            html_content = markdown_to_html(md_content)

            # Wrap in document div with header
            doc_html = f"""
            <div class="document">
                <div class="doc-header">
                    <h2>{title}</h2>
                    <div class="ref">Reference: {folder}/{filename}</div>
                </div>
                {html_content}
            </div>
            """
            html_parts.append(doc_html)

    # Combine all HTML
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>JATI KIRANA SDN BHD - Tax Working Papers YA 2025</title>
    </head>
    <body>
        {''.join(html_parts)}
    </body>
    </html>
    """

    # Save HTML for debugging
    html_file = BASE_DIR / "tax_working_papers.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"\nHTML saved to: {html_file}")

    # Generate PDF
    print(f"\nGenerating PDF...")
    try:
        HTML(string=full_html).write_pdf(
            OUTPUT_FILE,
            stylesheets=[CSS(string=CSS_STYLES)]
        )
        print(f"\n{'=' * 60}")
        print("PDF GENERATED SUCCESSFULLY!")
        print(f"{'=' * 60}")
        print(f"\nOutput file: {OUTPUT_FILE}")
        print(f"Files included: {len(files_included)}")
        print(f"\nReady for printing and boss review.")
        return True
    except Exception as e:
        print(f"\nError generating PDF: {e}")
        print("\nTrying alternative method...")
        return False

if __name__ == "__main__":
    success = generate_pdf()
    if not success:
        print("\n" + "=" * 60)
        print("ALTERNATIVE: Use the HTML file")
        print("=" * 60)
        print("\nThe HTML file has been created successfully.")
        print("You can open it in a browser and print to PDF:")
        print(f"\n  {BASE_DIR / 'tax_working_papers.html'}")
        print("\n1. Open in Chrome/Edge")
        print("2. Press Ctrl+P")
        print("3. Select 'Save as PDF'")
        print("4. Enable 'Background graphics'")
        print("5. Set margins to 'Default' or 'Minimum'")
