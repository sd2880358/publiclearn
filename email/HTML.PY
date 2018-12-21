from email.mime.text import MIMEText
import smtplib

mail_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Email</title>
</head>
<body>
<h1>This is a test</h1>

</body>
</html>
                '''

msg = MIMEText(mail_content,'html','utf8')

addr = 'leedonhom@gmail.com'

password = '73143177Da'

to_addr = 'leedonhom@gmail.com'

smtp_addr = 'smtp.gmail.com'

try:
    sry = smtplib.SMTP_SSL(smtp_addr.encode(),465)
    sry.login(addr,password)
    sry.sendmail(addr,[to_addr],msg.as_string())
except Exception as e:
    print(e)
