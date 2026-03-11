#!/usr/bin/env python3
"""
Export Tax Working Papers to Print-Ready HTML
JATI KIRANA SDN BHD - YA 2025

This script generates a professional HTML file optimized for printing to PDF.
Open the generated HTML in Chrome/Edge and press Ctrl+P to save as PDF.
"""

import os
import sys
import re
from pathlib import Path
from markdown import markdown

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
BASE_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
OUTPUT_FILE = BASE_DIR / "PRINT_Tax_Working_Papers_YA2025.html"

# Ordered list of files to include
FILE_ORDER = [
    # Cover and Main Tax Computation
    ("01_TAX_COMPUTATION", "TC_01_Cover_Page.md", "TC-01", "COVER PAGE"),
    ("01_TAX_COMPUTATION", "TC_02_Main_Tax_Computation.md", "TC-02", "MAIN TAX COMPUTATION"),
    ("01_TAX_COMPUTATION", "TC_03_Tax_Summary.md", "TC-03", "TAX SUMMARY"),
    ("01_TAX_COMPUTATION", "TC_04_CP204_Comparison.md", "TC-04", "CP204 COMPARISON"),
    ("01_TAX_COMPUTATION", "TC_05_Form_C_Presentation.md", "TC-05", "FORM C PRESENTATION GUIDE"),

    # Analysis of Accounts (Schedule A)
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_01_Analysis_Summary.md", "AA-01", "ANALYSIS SUMMARY"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_02_Revenue_Analysis.md", "AA-02", "REVENUE ANALYSIS"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_03_Expenditure_Analysis.md", "AA-03", "EXPENDITURE ANALYSIS"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_04_Add_Back_Schedule.md", "AA-04", "ADD BACK SCHEDULE"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_05_Non_Taxable_Income.md", "AA-05", "NON-TAXABLE INCOME"),
    ("02_ANALYSIS_OF_ACCOUNTS", "AA_06_Reconciliation.md", "AA-06", "RECONCILIATION"),

    # Capital Allowance (Schedule B)
    ("03_CAPITAL_ALLOWANCE", "CA_01_CA_Summary.md", "CA-01", "CA SUMMARY"),
    ("03_CAPITAL_ALLOWANCE", "CA_02_Plant_Machinery.md", "CA-02", "PLANT & MACHINERY"),
    ("03_CAPITAL_ALLOWANCE", "CA_03_Motor_Vehicles.md", "CA-03", "MOTOR VEHICLES"),
    ("03_CAPITAL_ALLOWANCE", "CA_04_Office_Equipment.md", "CA-04", "OFFICE EQUIPMENT"),
    ("03_CAPITAL_ALLOWANCE", "CA_05_Computer_Equipment.md", "CA-05", "COMPUTER EQUIPMENT"),
    ("03_CAPITAL_ALLOWANCE", "CA_06_Small_Value_Assets.md", "CA-06", "SMALL VALUE ASSETS"),
    ("03_CAPITAL_ALLOWANCE", "CA_07_Balancing_Adjustment.md", "CA-07", "BALANCING ADJUSTMENT"),
    ("03_CAPITAL_ALLOWANCE", "CA_08_CA_Brought_Forward.md", "CA-08", "CA BROUGHT FORWARD"),

    # Directors Details (Schedule C)
    ("04_DIRECTORS_DETAILS", "DD_01_Directors_Particulars.md", "DD-01", "DIRECTORS PARTICULARS"),
    ("04_DIRECTORS_DETAILS", "DD_02_Directors_Remuneration.md", "DD-02", "DIRECTORS REMUNERATION"),
    ("04_DIRECTORS_DETAILS", "DD_03_Directors_Interest.md", "DD-03", "DIRECTORS INTEREST"),

    # Shareholders Details (Schedule D)
    ("05_SHAREHOLDERS_DETAILS", "SH_01_Share_Capital_Info.md", "SH-01", "SHARE CAPITAL INFO"),
    ("05_SHAREHOLDERS_DETAILS", "SH_02_Shareholders_List.md", "SH-02", "SHAREHOLDERS LIST"),
    ("05_SHAREHOLDERS_DETAILS", "SH_03_Corporate_Shareholders.md", "SH-03", "CORPORATE SHAREHOLDERS"),
    ("05_SHAREHOLDERS_DETAILS", "SH_04_SME_Status_Verification.md", "SH-04", "SME STATUS"),

    # Beneficial Ownership (Schedule E)
    ("06_BENEFICIAL_OWNERSHIP", "BO_01_Beneficial_Owners_List.md", "BO-01", "BENEFICIAL OWNERS"),
    ("06_BENEFICIAL_OWNERSHIP", "BO_02_Ownership_Structure.md", "BO-02", "OWNERSHIP STRUCTURE"),
    ("06_BENEFICIAL_OWNERSHIP", "BO_03_Declaration.md", "BO-03", "DECLARATION"),

    # PBC & Query
    ("07_PBC_QUERY", "PBC_01_Document_Checklist.md", "PBC-01", "PBC CHECKLIST"),
    ("07_PBC_QUERY", "PBC_02_Outstanding_Items.md", "PBC-02", "OUTSTANDING ITEMS"),
    ("07_PBC_QUERY", "QRY_01_Query_List.md", "QRY-01", "QUERY LIST"),
    ("07_PBC_QUERY", "QRY_02_Query_Response.md", "QRY-02", "QUERY RESPONSE"),

    # Supporting Workings
    ("08_SUPPORTING_WORKINGS", "SW_01_Depreciation_vs_CA.md", "SW-01", "DEPRECIATION VS CA"),
    ("08_SUPPORTING_WORKINGS", "SW_02_Interest_Expense.md", "SW-02", "INTEREST EXPENSE"),
    ("08_SUPPORTING_WORKINGS", "SW_03_Related_Party_Trans.md", "SW-03", "RELATED PARTY"),
    ("08_SUPPORTING_WORKINGS", "SW_04_Losses_Summary.md", "SW-04", "LOSSES SUMMARY"),
    ("08_SUPPORTING_WORKINGS", "SW_09_CP204_Tax_Instalment.md", "SW-09", "CP204 TAX INSTALMENT"),

    # Prior Year Reference
    ("09_PRIOR_YEAR_REFERENCE", "PY_01_Prior_Year_Tax_Comp.md", "PY-01", "PRIOR YEAR TAX COMP"),
    ("09_PRIOR_YEAR_REFERENCE", "PY_02_Prior_Year_CA.md", "PY-02", "PRIOR YEAR CA"),
]

# Section headers
SECTIONS = {
    "01_TAX_COMPUTATION": ("1", "TAX COMPUTATION", "Main Deliverable"),
    "02_ANALYSIS_OF_ACCOUNTS": ("2", "ANALYSIS OF ACCOUNTS", "Schedule A"),
    "03_CAPITAL_ALLOWANCE": ("3", "CAPITAL ALLOWANCE", "Schedule B"),
    "04_DIRECTORS_DETAILS": ("4", "DIRECTORS DETAILS", "Schedule C"),
    "05_SHAREHOLDERS_DETAILS": ("5", "SHAREHOLDERS DETAILS", "Schedule D"),
    "06_BENEFICIAL_OWNERSHIP": ("6", "BENEFICIAL OWNERSHIP", "Schedule E"),
    "07_PBC_QUERY": ("7", "PBC & QUERY LIST", "Client Documentation"),
    "08_SUPPORTING_WORKINGS": ("8", "SUPPORTING WORKINGS", "Supporting Schedules"),
    "09_PRIOR_YEAR_REFERENCE": ("9", "PRIOR YEAR REFERENCE", "Reference Materials"),
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JATI KIRANA SDN BHD - Tax Working Papers YA 2025</title>
    <style>
        /* CSS Reset and Base */
        *, *::before, *::after {{ box-sizing: border-box; }}

        :root {{
            --primary: #1a365d;
            --secondary: #2c5282;
            --accent: #4299e1;
            --text: #2d3748;
            --text-light: #718096;
            --border: #e2e8f0;
            --bg-light: #f7fafc;
            --bg-section: #ebf8ff;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 10pt;
            line-height: 1.6;
            color: var(--text);
            margin: 0;
            padding: 20px;
            background: #fff;
        }}

        /* Print Styles */
        @media print {{
            body {{
                padding: 0;
                font-size: 9pt;
            }}

            .no-print {{
                display: none !important;
            }}

            .page-break {{
                page-break-after: always;
            }}

            .page-break-before {{
                page-break-before: always;
            }}

            .avoid-break {{
                page-break-inside: avoid;
            }}

            @page {{
                size: A4;
                margin: 1.5cm 1.2cm 2cm 1.2cm;
            }}

            @page :first {{
                margin-top: 0;
            }}

            /* Print header/footer using running elements */
            .document {{
                position: relative;
            }}

            .document::before {{
                content: "JATI KIRANA SDN BHD - Tax Working Papers YA 2025";
                position: running(header);
                font-size: 8pt;
                color: var(--text-light);
            }}
        }}

        /* Screen-only print button */
        .print-controls {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--primary);
            padding: 15px 25px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1000;
        }}

        .print-controls button {{
            background: #fff;
            color: var(--primary);
            border: none;
            padding: 10px 20px;
            font-size: 14px;
            font-weight: 600;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .print-controls button:hover {{
            background: var(--bg-light);
            transform: translateY(-1px);
        }}

        .print-controls p {{
            color: #fff;
            font-size: 11px;
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}

        /* Cover Page */
        .cover-page {{
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 40px;
            background: linear-gradient(180deg, #fff 0%, var(--bg-light) 100%);
        }}

        .cover-logo {{
            width: 120px;
            height: 120px;
            background: var(--primary);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 30px;
        }}

        .cover-logo span {{
            color: #fff;
            font-size: 36pt;
            font-weight: 700;
        }}

        .cover-page h1 {{
            font-size: 28pt;
            color: var(--primary);
            margin: 0 0 10px 0;
            letter-spacing: 2px;
        }}

        .cover-page h2 {{
            font-size: 14pt;
            color: var(--text-light);
            margin: 0 0 40px 0;
            font-weight: 400;
        }}

        .cover-box {{
            border: 3px solid var(--primary);
            padding: 30px 60px;
            margin: 30px 0;
        }}

        .cover-box h3 {{
            font-size: 24pt;
            color: var(--primary);
            margin: 0;
            letter-spacing: 3px;
        }}

        .cover-box p {{
            font-size: 16pt;
            color: var(--secondary);
            margin: 10px 0 0 0;
        }}

        .cover-details {{
            margin-top: 40px;
            font-size: 11pt;
        }}

        .cover-details p {{
            margin: 8px 0;
        }}

        .cover-signature {{
            display: flex;
            justify-content: center;
            gap: 80px;
            margin-top: 60px;
        }}

        .signature-box {{
            text-align: center;
        }}

        .signature-box .line {{
            width: 180px;
            border-bottom: 1px solid var(--text);
            margin-bottom: 5px;
        }}

        .signature-box p {{
            font-size: 10pt;
            color: var(--text-light);
            margin: 0;
        }}

        .cover-footer {{
            margin-top: auto;
            padding-top: 40px;
            font-size: 9pt;
            color: var(--text-light);
        }}

        /* Table of Contents */
        .toc {{
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }}

        .toc h1 {{
            font-size: 20pt;
            color: var(--primary);
            text-align: center;
            border-bottom: 3px solid var(--primary);
            padding-bottom: 15px;
            margin-bottom: 30px;
        }}

        .toc-section {{
            margin: 25px 0 10px 0;
        }}

        .toc-section-header {{
            display: flex;
            align-items: center;
            padding: 10px 15px;
            background: var(--primary);
            color: #fff;
            border-radius: 5px;
        }}

        .toc-section-num {{
            width: 30px;
            height: 30px;
            background: #fff;
            color: var(--primary);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            margin-right: 15px;
        }}

        .toc-section-title {{
            flex: 1;
            font-weight: 600;
        }}

        .toc-section-schedule {{
            font-size: 10pt;
            opacity: 0.8;
        }}

        .toc-items {{
            margin-left: 45px;
            border-left: 2px solid var(--border);
            padding-left: 20px;
        }}

        .toc-item {{
            display: flex;
            padding: 6px 0;
            border-bottom: 1px dotted var(--border);
        }}

        .toc-item-ref {{
            width: 60px;
            font-weight: 600;
            color: var(--secondary);
        }}

        .toc-item-title {{
            flex: 1;
            color: var(--text);
        }}

        /* Section Divider */
        .section-divider {{
            min-height: 300px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: #fff;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 60px 40px;
            margin: 0 -20px;
        }}

        .section-divider .section-num {{
            width: 80px;
            height: 80px;
            background: rgba(255,255,255,0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32pt;
            font-weight: 700;
            margin-bottom: 20px;
        }}

        .section-divider h1 {{
            font-size: 24pt;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 3px;
        }}

        .section-divider p {{
            font-size: 14pt;
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}

        /* Document */
        .document {{
            max-width: 900px;
            margin: 0 auto;
            padding: 30px 20px;
        }}

        .doc-header {{
            display: flex;
            align-items: flex-start;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 15px;
            margin-bottom: 25px;
        }}

        .doc-ref {{
            background: var(--primary);
            color: #fff;
            padding: 8px 15px;
            font-weight: 700;
            font-size: 12pt;
            margin-right: 20px;
            white-space: nowrap;
        }}

        .doc-title {{
            flex: 1;
        }}

        .doc-title h2 {{
            font-size: 16pt;
            color: var(--primary);
            margin: 0;
        }}

        .doc-title p {{
            font-size: 9pt;
            color: var(--text-light);
            margin: 5px 0 0 0;
        }}

        /* Content Styles */
        .content h1 {{
            font-size: 16pt;
            color: var(--primary);
            border-bottom: 2px solid var(--border);
            padding-bottom: 8px;
            margin: 25px 0 15px 0;
        }}

        .content h2 {{
            font-size: 13pt;
            color: var(--secondary);
            border-bottom: 1px solid var(--border);
            padding-bottom: 5px;
            margin: 20px 0 12px 0;
        }}

        .content h3 {{
            font-size: 11pt;
            color: var(--text);
            margin: 18px 0 10px 0;
        }}

        .content h4 {{
            font-size: 10pt;
            color: var(--text-light);
            margin: 15px 0 8px 0;
        }}

        .content p {{
            margin: 0 0 12px 0;
            text-align: justify;
        }}

        .content ul, .content ol {{
            margin: 12px 0 12px 25px;
            padding: 0;
        }}

        .content li {{
            margin-bottom: 5px;
        }}

        .content hr {{
            border: none;
            border-top: 1px solid var(--border);
            margin: 25px 0;
        }}

        .content strong {{
            color: var(--text);
        }}

        .content em {{
            color: var(--text-light);
        }}

        /* Tables */
        .content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
            font-size: 9pt;
        }}

        .content thead {{
            background: var(--primary);
            color: #fff;
        }}

        .content th {{
            padding: 10px 12px;
            text-align: left;
            font-weight: 600;
            border: 1px solid var(--primary);
        }}

        .content td {{
            padding: 8px 12px;
            border: 1px solid var(--border);
            vertical-align: top;
        }}

        .content tr:nth-child(even) {{
            background: var(--bg-light);
        }}

        .content tr:hover {{
            background: #edf2f7;
        }}

        /* Numeric alignment */
        .content td:last-child {{
            text-align: right;
        }}

        .content th:last-child {{
            text-align: right;
        }}

        /* Center alignment for symbols */
        .content td:first-child {{
            text-align: center;
        }}

        .content th:first-child {{
            text-align: center;
        }}

        /* Code blocks */
        .content pre {{
            background: #1a202c;
            color: #e2e8f0;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: Consolas, Monaco, monospace;
            font-size: 9pt;
        }}

        .content code {{
            background: var(--bg-light);
            padding: 2px 6px;
            border-radius: 3px;
            font-family: Consolas, Monaco, monospace;
            font-size: 9pt;
            color: #c53030;
        }}

        .content pre code {{
            background: none;
            padding: 0;
            color: inherit;
        }}

        /* Blockquote */
        .content blockquote {{
            border-left: 4px solid var(--accent);
            margin: 15px 0;
            padding: 10px 20px;
            background: var(--bg-section);
            color: var(--secondary);
        }}

        /* Page break helpers */
        .avoid-break {{
            page-break-inside: avoid;
        }}
    </style>
</head>
<body>
    <!-- Print Controls (hidden when printing) -->
    <div class="print-controls no-print">
        <button onclick="window.print()">🖨️ Print to PDF</button>
        <p>Use Chrome/Edge for best results<br>Enable "Background graphics"</p>
    </div>

    {content}

    <script>
        // Add keyboard shortcut for printing
        document.addEventListener('keydown', function(e) {{
            if (e.ctrlKey && e.key === 'p') {{
                // Allow default print dialog
            }}
        }});
    </script>
</body>
</html>
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
    """Create cover page HTML."""
    return """
    <div class="cover-page page-break">
        <div class="cover-logo">
            <span>JK</span>
        </div>
        <h1>JATI KIRANA SDN BHD</h1>
        <h2>Company No: 724858-P</h2>

        <div class="cover-box">
            <h3>FORM C</h3>
            <p>TAX COMPUTATION</p>
        </div>

        <div class="cover-details">
            <p><strong>Tax File No:</strong> C 2359253703</p>
            <p><strong>Year of Assessment:</strong> 2025</p>
            <p><strong>Basis Period:</strong> 01/07/2024 to 30/06/2025</p>
        </div>

        <div class="cover-signature">
            <div class="signature-box">
                <div class="line"></div>
                <p>Prepared By</p>
            </div>
            <div class="signature-box">
                <div class="line"></div>
                <p>Reviewed By</p>
            </div>
            <div class="signature-box">
                <div class="line"></div>
                <p>Date</p>
            </div>
        </div>

        <div class="cover-footer">
            <p>CONFIDENTIAL - FOR INTERNAL USE ONLY</p>
        </div>
    </div>
    """

def create_toc(files_included):
    """Create table of contents."""
    toc_html = """
    <div class="toc page-break">
        <h1>TABLE OF CONTENTS</h1>
    """

    current_section = None

    for folder, filename, ref, title in files_included:
        if folder != current_section:
            if current_section is not None:
                toc_html += "</div></div>"  # Close previous section

            current_section = folder
            sec_num, sec_title, sec_schedule = SECTIONS.get(folder, ("?", folder, ""))

            toc_html += f"""
            <div class="toc-section">
                <div class="toc-section-header">
                    <div class="toc-section-num">{sec_num}</div>
                    <div class="toc-section-title">{sec_title}</div>
                    <div class="toc-section-schedule">{sec_schedule}</div>
                </div>
                <div class="toc-items">
            """

        toc_html += f"""
            <div class="toc-item">
                <div class="toc-item-ref">{ref}</div>
                <div class="toc-item-title">{title}</div>
            </div>
        """

    toc_html += "</div></div></div>"  # Close last section and toc
    return toc_html

def create_section_divider(folder):
    """Create section divider page."""
    sec_num, sec_title, sec_schedule = SECTIONS.get(folder, ("?", folder, ""))

    return f"""
    <div class="section-divider page-break-before page-break">
        <div class="section-num">{sec_num}</div>
        <h1>{sec_title}</h1>
        <p>{sec_schedule}</p>
    </div>
    """

def create_document(folder, filename, ref, title, content_html):
    """Create document section."""
    return f"""
    <div class="document page-break-before">
        <div class="doc-header avoid-break">
            <div class="doc-ref">{ref}</div>
            <div class="doc-title">
                <h2>{title}</h2>
                <p>{folder}/{filename}</p>
            </div>
        </div>
        <div class="content">
            {content_html}
        </div>
    </div>
    """

def generate_html():
    """Main function to generate HTML."""
    print("=" * 60)
    print("JATI KIRANA SDN BHD - Tax Working Papers Export")
    print("Year of Assessment 2025")
    print("=" * 60)
    print()

    # Collect files that exist
    files_included = []
    for folder, filename, ref, title in FILE_ORDER:
        filepath = BASE_DIR / folder / filename
        if filepath.exists():
            files_included.append((folder, filename, ref, title))
        else:
            print(f"  [SKIP] {folder}/{filename} - not found")

    print(f"\nFound {len(files_included)} files to include.\n")

    # Build HTML content
    content_parts = []

    # Cover page
    print("Creating cover page...")
    content_parts.append(create_cover_page())

    # Table of contents
    print("Creating table of contents...")
    content_parts.append(create_toc(files_included))

    # Process each file
    current_section = None

    for folder, filename, ref, title in files_included:
        filepath = BASE_DIR / folder / filename

        # Add section divider if new section
        if folder != current_section:
            current_section = folder
            sec_num, sec_title, sec_schedule = SECTIONS.get(folder, ("?", folder, ""))
            print(f"\nSECTION {sec_num}: {sec_title}")
            print("-" * 50)
            content_parts.append(create_section_divider(folder))

        print(f"  {ref}: {title}")

        md_content = read_markdown_file(filepath)
        if md_content:
            html_content = markdown_to_html(md_content)
            content_parts.append(create_document(folder, filename, ref, title, html_content))

    # Combine all HTML
    full_html = HTML_TEMPLATE.format(content=''.join(content_parts))

    # Save HTML
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"\n{'=' * 60}")
    print("HTML GENERATED SUCCESSFULLY!")
    print(f"{'=' * 60}")
    print(f"\nOutput file:")
    print(f"  {OUTPUT_FILE}")
    print(f"\nFiles included: {len(files_included)}")
    print(f"\n{'=' * 60}")
    print("HOW TO CREATE PDF:")
    print(f"{'=' * 60}")
    print()
    print("1. Open the HTML file in Chrome or Edge browser")
    print("2. Press Ctrl+P (or click the Print button)")
    print("3. Select 'Save as PDF' as destination")
    print("4. IMPORTANT: Enable 'Background graphics' in More settings")
    print("5. Set margins to 'Default'")
    print("6. Click Save")
    print()
    print("The PDF will have proper page breaks between sections.")
    print()

    return OUTPUT_FILE

if __name__ == "__main__":
    output = generate_html()
    print(f"Opening in default browser...")
    import webbrowser
    webbrowser.open(str(output))
