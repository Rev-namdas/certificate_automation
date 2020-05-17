from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.utils import ImageReader
import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders

excel = pd.read_excel('data.xlsx')

details = zip(excel['Name'].values, excel['Course'].values, excel['Email'].values)

for name, subject, mail in details:
    pdf_file = name.title() + '.pdf'
    certificate = ImageReader('certificate.jpg')

    can = canvas.Canvas(pdf_file, pagesize=landscape(letter))
    can.drawImage(certificate, 10, 10, width=770, height=590)
    can.setFontSize(18)
    can.drawCentredString(395, 350, name.title())
    can.drawCentredString(395, 245, subject)
    can.drawCentredString(520, 180, subject)
    can.drawCentredString(520, 110, "S A D M A N")
    can.save()

    msg = MIMEMultipart()

    sender          = 'sadmanahmedsadman@gmail.com'
    receiver        = mail
    loginuser       = 'sadmanahmedsadman@gmail.com'
    loginpass       = 'asdawd786512349'

    msg['From']     = sender
    msg['To']       = receiver
    msg['Subject']  = 'Certificate - ' + name.title()

    body            = 'This is sent from python'

    filename        = pdf_file
    pdf             = open(filename, 'rb')

    msg.attach(MIMEText(body, 'plain'))
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload((pdf).read())
    encoders.encode_base64(attachment)

    attachment.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(attachment)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(loginuser, loginpass)

    text = msg.as_string()

    session.sendmail(sender, receiver, text)
    session.quit()