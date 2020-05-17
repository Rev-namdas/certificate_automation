from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.utils import ImageReader


name    = input('Enter Name: ')
subject = input('Enter Subject: ')

pdf_file = name + '.pdf'
logo = ImageReader('certificate.jpg')

can = canvas.Canvas(pdf_file, pagesize=landscape(letter))
can.drawImage(logo, 10, 10, width=770, height=590)
can.setFontSize(18)
can.drawCentredString(395, 350, name)
can.drawCentredString(395, 245, subject)
can.drawCentredString(520, 180, subject)
can.drawCentredString(520, 110, "S A D M A N")
can.save()



# from PyPDF2 import PdfFileWriter, PdfFileReader
# from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4

# buffer = BytesIO()

# # create a new PDF with Reportlab
# p = canvas.Canvas(buffer, pagesize=A4)
# p.drawCentredString(350, 350, "holaaaaaaaaaaaa")
# p.showPage()
# p.save()

# #move to the beginning of the StringIO buffer
# buffer.seek(0)
# newPdf = PdfFileReader(buffer)

# #######DEBUG NEW PDF created#############
# pdf1 = buffer.getvalue()
# open('new.pdf', 'wb').write(pdf1)
# #########################################
# # read your existing PDF
# existingPdf = PdfFileReader(open('certificate-converted.pdf', 'rb'))
# output = PdfFileWriter()
# # add the "watermark" (which is the new pdf) on the existing page
# page = existingPdf.getPage(0)
# page.mergePage(newPdf.getPage(0))
# output.addPage(page)
# # finally, write "output" to a real file
# outputStream = open('output.pdf', 'wb')
# output.write(outputStream)
# outputStream.close()