import fitz  # PyMuPDF
import sys

# Fix encoding for Windows
sys.stdout.reconfigure(encoding='utf-8')

# Open the original GL PDF
input_pdf = sys.argv[1] if len(sys.argv) > 1 else "general_ledger.pdf"
output_pdf = sys.argv[2] if len(sys.argv) > 2 else "GL_Extract_Tax_Instalment.pdf"

doc = fitz.open(input_pdf)

# Define colors
RED = (1, 0, 0)
BLUE = (0, 0, 1)
GREEN = (0, 0.6, 0)
ORANGE = (1, 0.5, 0)
PURPLE = (0.5, 0, 0.5)

def add_tickmark(page, search_text, tickmark, color=RED, offset_x=30):
    """Search for text and add tickmark annotation next to it"""
    text_instances = page.search_for(search_text)
    if text_instances:
        rect = text_instances[0]
        # Position tickmark to the right of the found text
        x = rect.x1 + offset_x
        y = (rect.y0 + rect.y1) / 2

        # Draw circle with tickmark
        page.draw_circle(fitz.Point(x, y), 8, color=color, width=1.5)
        tick_rect = fitz.Rect(x-8, y-8, x+8, y+8)
        page.insert_textbox(tick_rect, tickmark, fontsize=9, color=color, align=1)
        return True
    return False

# Page 9 (index 8) - A/C 4600/0000 starts here
page9 = doc[8]

# Add title box
title_rect = fitz.Rect(380, 30, 580, 70)
page9.draw_rect(title_rect, color=BLUE, width=1.5, fill=(0.9, 0.9, 1))
page9.insert_textbox(title_rect, "GL EXTRACT - TAX INSTALMENT\nA/C 4600/0000\nCross-ref: TC_04, SW_09", fontsize=8, color=BLUE, align=1)

# Search and annotate CP204 payments on Page 9
annotations_p9 = [
    ("Balance B/F", "\u24d0", PURPLE, 280),  # ⓐ Balance B/F line
    ("CP204 TAX INSTL 12/2024", "\u2460", RED, 30),  # ①
    ("CP204 TAX INSTL 01/2025", "\u2461", RED, 30),  # ②
    ("CP204 TAX INSTL 02/2025", "\u2462", RED, 30),  # ③
    ("CP204 TAX INSTL 03/2025", "\u2463", RED, 30),  # ④
    ("CP204 TAX INSTL 04/2025", "\u2464", RED, 30),  # ⑤
    ("CP204 TAX INSTL 05/2025", "\u2465", RED, 30),  # ⑥
    ("CP204 TAX INSTL 06/2025", "\u2466", RED, 30),  # ⑦
    ("CP204 TAX INSTL 07/2025", "\u2467", RED, 30),  # ⑧
    ("CP204 TAX INSTL 08/2025", "\u2468", RED, 30),  # ⑨
    ("CP204 TAX INSTL 09/2025", "\u2469", RED, 30),  # ⑩
]

print("Page 9 annotations:")
for search, tick, color, offset in annotations_p9:
    found = add_tickmark(page9, search, tick, color, offset)
    status = "Found" if found else "NOT FOUND"
    print(f"  {search}: {status}")

# Page 10 (index 9) - continuation
page10 = doc[9]

# Add title box
title_rect = fitz.Rect(380, 30, 580, 70)
page10.draw_rect(title_rect, color=BLUE, width=1.5, fill=(0.9, 0.9, 1))
page10.insert_textbox(title_rect, "GL EXTRACT - TAX INSTALMENT\nA/C 4600/0000 (cont'd)\nCross-ref: TC_04, SW_09", fontsize=8, color=BLUE, align=1)

# Search and annotate on Page 10
annotations_p10 = [
    ("CP204 TAX INSTL 10/2025", "\u246a", RED, 30),  # ⑪
    ("CP204 TAX INSTL 11/2025", "\u246b", RED, 30),  # ⑫
]

print("\nPage 10 annotations:")
for search, tick, color, offset in annotations_p10:
    found = add_tickmark(page10, search, tick, color, offset)
    status = "Found" if found else "NOT FOUND"
    print(f"  {search}: {status}")

# Search for tax refunds
refund_searches = [
    ("4,266.72", "\u24e1", GREEN, 30),  # ⓡ
    ("884.64", "\u24e1", GREEN, 30),    # ⓡ
    ("197.52", "\u24e1", GREEN, 30),    # ⓡ
]

print("\nTax refund annotations:")
for search, tick, color, offset in refund_searches:
    found = add_tickmark(page10, search, tick, color, offset)
    status = "Found" if found else "NOT FOUND"
    print(f"  Refund {search}: {status}")

# Add comprehensive legend box at bottom of page 10
legend_rect = fitz.Rect(30, 650, 280, 800)
page10.draw_rect(legend_rect, color=BLUE, width=1.5, fill=(0.95, 0.95, 1))
legend_text = """TICKMARK LEGEND - A/C 4600/0000

(a) = Balance B/F (RM 2,409.88)
(1)-(12) = CP204 Instalments @ RM540/mth
(r) = Tax Refund received from LHDN

SUMMARY:
Total CP204 Paid YA2025: RM 6,480.00
Less: Tax Refunds:      (RM 5,348.88)
Balance C/F:             RM 3,541.00

Cross-referenced to:
- TC_04_CP204_Comparison.md
- SW_09_CP204_Tax_Instalment.md

Verified by: _________ Date: _________"""
page10.insert_textbox(legend_rect, legend_text, fontsize=7, color=BLUE)

# Add summary box on right side
summary_rect = fitz.Rect(320, 650, 570, 800)
page10.draw_rect(summary_rect, color=RED, width=1.5, fill=(1, 0.95, 0.95))
summary_text = """CP204 INSTALMENT SCHEDULE YA2025

(1) 01/07/2024 PBB204724  RM540
(2) 01/08/2024 PBB204727  RM540
(3) 01/09/2024 PBB204729  RM540
(4) 01/10/2024 PBB204731  RM540
(5) 01/11/2024 PBB204733  RM540
(6) 02/12/2024 PBB204736  RM540
(7) 02/01/2025 PBB204740  RM540
(8) 01/02/2025 PBB204743  RM540
(9) 01/03/2025 PBB204745  RM540
(10) 01/04/2025 PBB204749 RM540
(11) 02/05/2025 PBB204750 RM540
(12) 03/06/2025 PBB384353 RM540
-------------------------------
TOTAL PAID:       RM 6,480.00"""
page10.insert_textbox(summary_rect, summary_text, fontsize=6.5, color=RED)

# Save the annotated PDF
doc.save(output_pdf)
doc.close()

print(f"\nAnnotated PDF saved to:")
print(f"  {output_pdf}")
print("\nAnnotations added:")
print("  - Title boxes on pages 9-10")
print("  - Tickmarks for CP204 payments")
print("  - Tickmarks for tax refunds")
print("  - Legend box with summary")
print("  - CP204 schedule summary box")
