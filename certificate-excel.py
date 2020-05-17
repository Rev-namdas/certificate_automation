from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.utils import ImageReader
import pandas as pd

excel = pd.read_excel('data.xlsx')

details = zip(excel['Name'].values, excel['Course'].values)

for name, subject in details:
    pdf_file = name.title() + '.pdf'
    logo = ImageReader('certificate.jpg')

    can = canvas.Canvas(pdf_file, pagesize=landscape(letter))
    can.drawImage(logo, 10, 10, width=770, height=590)
    can.setFontSize(18)
    can.drawCentredString(395, 350, name.title())
    can.drawCentredString(395, 245, subject)
    can.drawCentredString(520, 180, subject)
    can.drawCentredString(520, 110, "S A D M A N")
    can.save()