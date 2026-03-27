from fpdf import FPDF
import uuid
from datetime import datetime

def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    pdf.set_margins(left=10, top=10, right=10)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 6, content.strip())
    filename = f"rti_{uuid.uuid4().hex}.pdf"
    pdf.output(filename)
    return filename