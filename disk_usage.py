import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


threshold = 80
mount_usage = {}
du = os.popen("df -h").readlines()
fromaddr = 'sender@test.com'
rcptaddr = 'recipient@test.com'
passwd = 'yourpassword'
smtp_server = 'your_smtp_server'


for line in du[1:]:
     mount_usage[line.split()[-1]] = line.split()[-2]
over_thresh = []
for disk in mount_usage:
    percent = int(mount_usage[disk].replace("%", ""))
    if percent >= threshold:
        over_thresh.append(disk)

if over_thresh:
        server = smtplib.SMTP(smtp_server, 587)
        server.connect(smtp_server, 587)
        server.starttls()
        server.ehlo()
        server.login(fromaddr, passwd)
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = rcptaddr
        msg['Subject'] = 'Disk usage above {}%'.format(threshold)
        message = "The following disks are above the threshold:\n"
        for disk in over_thresh:
            message += " - {} : {}\n".format(disk, mount_usage[disk])
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()
        server.sendmail(fromaddr, rcptaddr, text)
        server.quit()