
# --------------------------------------------
# send mail start

import os, sys
import smtplib, time
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mailInfo = {
    "from": "spbeen@foxmail.com",
    "to": "**************",
    "hostname": "smtp.qq.com",
    "username": "spbeen@foxmail.com",
    "password": "*************",
    "mailsubject": "脚本发送邮件",
    "mailtext": "<h1>邮件正文</h1>",
    "mailencoding": "utf-8"
}


def send_mail(from_mail, to_email, subject, mailtext):
    smtp = SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"], mailInfo["password"])

    msg = MIMEText(mailtext, "html", mailInfo["mailencoding"])
    msg["Subject"] = Header(subject, mailInfo["mailencoding"])
    msg["from"] = from_mail
    msg["to"] = to_email
    smtp.sendmail(from_mail, to_email, msg.as_string())
    smtp.quit()

# send mail end
# --------------------------------------------
