from email.mime.text import MIMEText
import smtplib


message = MIMEText('this is a test email','plain','utf-8')

account = 'leedonhom@gmail.com'

password = '73143177Da'

to_account = '1490159765@qq.com'

smtp_srv = 'smtp.gmail.com'

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(account,password)
    srv.sendmail(account, [to_account],message.as_string())
    srv.quit()
except Exception as e:
    print(e)