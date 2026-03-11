#!/usr/bin/env python3
"""
Generate PDF directly using Chrome Headless
JATI KIRANA SDN BHD - YA 2025
"""

import os
import sys
import subprocess
from pathlib import Path
import time

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Paths
BASE_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
HTML_FILE = BASE_DIR / "PRINT_Tax_Working_Papers_YA2025.html"
PDF_OUTPUT = BASE_DIR / "JATI_KIRANA_YA2025_Tax_Working_Papers.pdf"

# Browser paths
CHROME_PATHS = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
]

EDGE_PATHS = [
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
]

def find_browser():
    """Find Chrome or Edge browser."""
    for path in CHROME_PATHS:
        if os.path.exists(path):
            return path, "Chrome"
    for path in EDGE_PATHS:
        if os.path.exists(path):
            return path, "Edge"
    return None, None

def generate_pdf():
    """Generate PDF using Chrome/Edge headless mode."""
    print("=" * 60)
    print("JATI KIRANA SDN BHD - Direct PDF Generation")
    print("Year of Assessment 2025")
    print("=" * 60)
    print()

    # Check HTML file exists
    if not HTML_FILE.exists():
        print(f"ERROR: HTML file not found!")
        print(f"  {HTML_FILE}")
        print("\nPlease run export_to_print_pdf.py first.")
        return False

    # Find browser
    browser_path, browser_name = find_browser()
    if not browser_path:
        print("ERROR: No compatible browser found!")
        print("Please install Chrome or Edge browser.")
        return False

    print(f"Using {browser_name}: {browser_path}")
    print(f"Input:  {HTML_FILE}")
    print(f"Output: {PDF_OUTPUT}")
    print()

    # Convert file path to file:// URL
    html_url = HTML_FILE.as_uri()

    # Chrome/Edge headless PDF command
    cmd = [
        browser_path,
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        '--disable-software-rasterizer',
        '--run-all-compositor-stages-before-draw',
        '--print-to-pdf-no-header',
        f'--print-to-pdf={PDF_OUTPUT}',
        html_url
    ]

    print("Generating PDF...")
    print()

    try:
        # Run Chrome headless
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )

        # Wait for file to be written
        time.sleep(2)

        if PDF_OUTPUT.exists():
            file_size = PDF_OUTPUT.stat().st_size / 1024 / 1024  # MB
            print("=" * 60)
            print("PDF GENERATED SUCCESSFULLY!")
            print("=" * 60)
            print()
            print(f"Output file:")
            print(f"  {PDF_OUTPUT}")
            print(f"  Size: {file_size:.2f} MB")
            print()
            print("Ready for printing and boss review!")
            return True
        else:
            print("ERROR: PDF file was not created.")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print("ERROR: PDF generation timed out.")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    success = generate_pdf()
    if success:
        # Open the PDF
        print("\nOpening PDF...")
        os.startfile(PDF_OUTPUT)
    else:
        print("\n" + "=" * 60)
        print("ALTERNATIVE: Manual PDF Generation")
        print("=" * 60)
        print()
        print("1. Open this file in Chrome/Edge:")
        print(f"   {HTML_FILE}")
        print()
        print("2. Press Ctrl+P")
        print("3. Select 'Save as PDF'")
        print("4. Enable 'Background graphics'")
        print("5. Click Save")
