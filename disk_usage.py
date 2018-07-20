import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


mount_usage = {}
du = os.popen("df -h").readlines()

for line in du[1:]:
     mount_usage[line.split()[8]] = line.split()[7]
print(mount_usage)
over_80 = []
for disk in mount_usage:
    percent = int(mount_usage[disk].replace("%", ""))
    print(percent)
    if percent > 80:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        msg = MIMEMultipart()
        msg['From'] = 'sender @ gmail.com'
        msg['To'] = 'receiver @ gmail.com'
        msg['Subject'] = 'Disk usage above 80%'
        message = ""
        msg.attach(MIMEText(message))