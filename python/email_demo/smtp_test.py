# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = '1825847xxxx@163.com'
receiver = '101238xxxx@qq.com'
receiver = '1825847xxxx@163.com'
subject = '555555'
smtpserver = 'smtp.163.com'
username = '1825847xxxx@163.com'
password = 'password'

msg = MIMEText('zheshiwode shoujihao', 'text', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')

# smtp.ehlo()
# smtp.starttls()
# smtp.ehlo()
# smtp.set_debuglevel(1)

smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

sender = 'cuidingyu@163.com'
smtpObj = smtplib.SMTP(host="smtp.163.com")

