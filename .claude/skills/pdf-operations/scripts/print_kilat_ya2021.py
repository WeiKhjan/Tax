"""
Set print layout and export Tax Computation 2021 - Kilat Sejadi.xlsx to PDF.
Uses Excel COM automation (win32com).
"""
import os, sys
import win32com.client as win32

EXCEL_PATH = r"C:\Users\khjan\Downloads\Demo - TAX- Calude\Tax Computation 2021 - Kilat Sejadi.xlsx"
PDF_PATH   = r"C:\Users\khjan\Downloads\Demo - TAX- Calude\Tax Computation 2021 - Kilat Sejadi.pdf"

# ── Excel constants ────────────────────────────────────────────────────────
xlLandscape  = 2
xlPortrait   = 1
xlPaperA4    = 9
xlEdgeBottom = 2   # PageSetup.LeftMargin etc uses Points (1 inch = 72 pt)

PT = 72  # points per inch

def cm_to_pt(cm):
    return cm * 28.3465

def setup_sheet(ws, orientation, fit_pages_wide=1, fit_pages_tall=0,
                hdr=None, ftr=None, margin_cm=1.5):
    ps = ws.PageSetup
    ps.PaperSize       = xlPaperA4
    ps.Orientation     = orientation
    ps.Zoom            = False          # must be False to use FitToPages
    ps.FitToPagesWide  = fit_pages_wide
    # False = no limit on pages tall (as many as needed); int = fixed page count
    ps.FitToPagesTall  = False if fit_pages_tall == 0 else fit_pages_tall
    ps.LeftMargin      = cm_to_pt(margin_cm)
    ps.RightMargin     = cm_to_pt(margin_cm)
    ps.TopMargin       = cm_to_pt(margin_cm + 0.5)
    ps.BottomMargin    = cm_to_pt(margin_cm)
    ps.HeaderMargin    = cm_to_pt(0.5)
    ps.FooterMargin    = cm_to_pt(0.5)
    ps.CenterHorizontally = True

    # Footer: sheet name left, page number right
    ps.LeftFooter   = "&A"                         # sheet tab name
    ps.CenterFooter = "KILAT SEJADI SDN. BHD."
    ps.RightFooter  = "Page &P of &N"

    if hdr:
        ps.CenterHeader = hdr

def main():
    xl = win32.Dispatch("Excel.Application")
    xl.Visible       = False
    xl.DisplayAlerts = False

    try:
        wb = xl.Workbooks.Open(EXCEL_PATH)

        # ── YA2021: Cover / Index ─────────────────────────────────────────
        ws = wb.Sheets("YA2021")
        setup_sheet(ws, xlPortrait, fit_pages_wide=1, fit_pages_tall=1,
                    hdr="FORM C TAX COMPUTATION  |  YA 2021  |  TAX REF: [TAX REF NO]")
        ws.PageSetup.PrintArea = "A1:H20"

        # ── St.A: Main Tax Computation ────────────────────────────────────
        ws = wb.Sheets("St.A")
        setup_sheet(ws, xlPortrait, fit_pages_wide=1, fit_pages_tall=0,
                    hdr="STATEMENT A  -  INCOME TAX COMPUTATION")
        ws.PageSetup.PrintArea = "A1:K58"

        # ── Sch.A: Supporting Schedule ────────────────────────────────────
        ws = wb.Sheets("Sch.A")
        setup_sheet(ws, xlPortrait, fit_pages_wide=1, fit_pages_tall=0,
                    hdr="SCHEDULE A  -  ANALYSIS OF NON-DEDUCTIBLE EXPENSES")
        ws.PageSetup.PrintArea = "A1:H35"

        # ── St.B: Capital Allowance ───────────────────────────────────────
        # Wide table (columns A-M) → Landscape
        ws = wb.Sheets("St.B")
        setup_sheet(ws, xlLandscape, fit_pages_wide=1, fit_pages_tall=0,
                    hdr="STATEMENT B  -  CAPITAL ALLOWANCE SCHEDULE",
                    margin_cm=1.0)
        ws.PageSetup.PrintArea = "A1:M58"

        # ── DF: Deferred Tax ──────────────────────────────────────────────
        ws = wb.Sheets("DF")
        setup_sheet(ws, xlPortrait, fit_pages_wide=1, fit_pages_tall=0,
                    hdr="DEFERRED TAX COMPUTATION")
        ws.PageSetup.PrintArea = "A1:H42"

        # ── Export all sheets as one PDF ──────────────────────────────────
        # ExportAsFixedFormat: Type=0 (PDF), Filename, Quality=0 (standard)
        wb.ExportAsFixedFormat(
            Type=0,
            Filename=PDF_PATH,
            Quality=0,
            IncludeDocProperties=True,
            IgnorePrintAreas=False,
            OpenAfterPublish=False
        )

        # Save updated print settings back to Excel
        wb.Save()
        wb.Close(False)

        print(f"[OK] PDF saved : {PDF_PATH}")
        print(f"     File size  : {os.path.getsize(PDF_PATH):,} bytes")

    except Exception as e:
        print(f"[ERROR] {e}")
        raise
    finally:
        xl.Quit()

if __name__ == "__main__":
    main()
