import fitz  # PyMuPDF

# Open the original GL PDF
input_pdf = r"C:\Users\khjan\Downloads\Demo - YYC - Calude\ACC_TEMP\ACC\general ledger.pdf"
output_pdf = r"C:\Users\khjan\Downloads\Demo - YYC - Calude\JATI KIRANA SDN BHD YA 2025\08_SUPPORTING_WORKINGS\GL_Extract_Tax_Instalment.pdf"

doc = fitz.open(input_pdf)

# Define colors
RED = (1, 0, 0)
BLUE = (0, 0, 1)
GREEN = (0, 0.5, 0)
ORANGE = (1, 0.5, 0)

# Tickmark annotations for Page 9 (index 8) - A/C 4600/0000 PROVISION FOR TAXATION
# The CP204 payments are on this page

page9 = doc[8]  # Page 9 (0-indexed = 8)

# Add header annotation
rect = fitz.Rect(400, 50, 580, 80)
page9.draw_rect(rect, color=BLUE, width=1)
page9.insert_textbox(rect, "TAX INSTALMENT EXTRACT\nA/C 4600/0000", fontsize=8, color=BLUE, align=1)

# Annotations for CP204 payments on Page 9
# These are approximate positions - the actual positions depend on the PDF layout
annotations_page9 = [
    # (y_position, tickmark, description)
    (178, "ⓐ", "Balance B/F"),
    (195, "①", "CP204 12/2024"),
    (218, "②", "CP204 01/2025"),
    (241, "③", "CP204 02/2025"),
    (264, "④", "CP204 03/2025"),
    (287, "⑤", "CP204 04/2025"),
    (310, "⑥", "CP204 05/2025"),
    (333, "⑦", "CP204 06/2025"),
    (356, "⑧", "CP204 07/2025"),
    (379, "⑨", "CP204 08/2025"),
    (402, "⑩", "CP204 09/2025"),
]

for y, tick, desc in annotations_page9:
    # Add tickmark circle on the right side
    rect = fitz.Rect(545, y-8, 565, y+8)
    page9.draw_circle(fitz.Point(555, y), 8, color=RED, width=1.5)
    page9.insert_textbox(rect, tick, fontsize=10, color=RED, align=1)

# Page 10 (index 9) - continuation of A/C 4600/0000
page10 = doc[9]

# Add header annotation
rect = fitz.Rect(400, 50, 580, 80)
page10.draw_rect(rect, color=BLUE, width=1)
page10.insert_textbox(rect, "TAX INSTALMENT EXTRACT\nA/C 4600/0000 (cont'd)", fontsize=8, color=BLUE, align=1)

# Annotations for Page 10
annotations_page10 = [
    (115, "⑪", "CP204 10/2025"),
    (138, "ⓡ", "Tax Refund 1"),
    (153, "ⓡ", "Tax Refund 2"),
    (168, "ⓡ", "Tax Refund 3"),
    (191, "⑫", "CP204 11/2025"),
]

for y, tick, desc in annotations_page10:
    rect = fitz.Rect(545, y-8, 565, y+8)
    if tick == "ⓡ":
        page10.draw_circle(fitz.Point(555, y), 8, color=GREEN, width=1.5)
        page10.insert_textbox(rect, tick, fontsize=10, color=GREEN, align=1)
    else:
        page10.draw_circle(fitz.Point(555, y), 8, color=RED, width=1.5)
        page10.insert_textbox(rect, tick, fontsize=10, color=RED, align=1)

# Add legend box at bottom of page 10
legend_rect = fitz.Rect(350, 700, 580, 800)
page10.draw_rect(legend_rect, color=BLUE, width=1, fill=(0.95, 0.95, 1))
legend_text = """TICKMARK LEGEND:
ⓐ = Balance B/F
①-⑫ = CP204 Instalments (RM540 each)
ⓡ = Tax Refund from LHDN

Total CP204 YA2025: RM 6,480.00
Tax Refunds: RM 5,348.88
Balance C/F: RM 3,541.00

Cross-ref: TC_04, SW_09"""
page10.insert_textbox(legend_rect, legend_text, fontsize=8, color=BLUE)

# Save the annotated PDF
doc.save(output_pdf)
doc.close()

print(f"Annotated PDF saved to: {output_pdf}")
print("Annotations added to pages 9-10 (A/C 4600/0000 - Provision for Taxation)")
