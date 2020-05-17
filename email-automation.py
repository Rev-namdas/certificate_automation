import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()

sender          = 'sadmanahmedsadman@gmail.com'
receiver        = 'ahmedsadman22@gmail.com'

msg['From']     = sender
msg['To']       = receiver
msg['Subject']  = 'Python SMTP'

body            = 'This is sent from python'

filename        = 'Mubasshir.pdf'
pdf             = open(filename, 'rb')

msg.attach(MIMEText(body, 'plain'))
attachment = MIMEBase('application', 'octet-stream')
attachment.set_payload((pdf).read())
encoders.encode_base64(attachment)

attachment.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(attachment)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login('sadmanahmedsadman@gmail.com', 'asdawd786512349')

text = msg.as_string()

session.sendmail(sender, receiver, text)
session.quit()