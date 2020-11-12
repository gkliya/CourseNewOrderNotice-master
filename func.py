import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import os
import conf

log_filepath = f'{conf.log_dir}{os.sep}course.new.order.notice.log'
log_file = open(log_filepath, 'a+')


def end():
    log_file.close()


def log(msg, print_end='\n'):
    print(msg, end=print_end)
    log_file.write(msg + print_end)


def send_email1(course, platform, url, num, last_num):
    """发送邮件"""
    sender = '1345325190@qq.com' # 发送者邮件
    password = 'hlugbxacqrpsgfji' # 发送者授权码
    receiver = '442540777@qq.com' # 接收者邮件
    subject = f'[{course}][{platform}]学习人数增加{num - last_num}'
    content = f'学习人数 {num}\n上次记录学习人数 {last_num}\n课程链接 {url}\n'
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(['李远香', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["周华健", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = subject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        log('邮件发送成功')
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        log('无法发送邮件')


def get_platform_last_order_num(platform):
    log_path = f'{conf.log_dir}{os.sep}{platform}.order_num'
    try:
        platform_last_order_num = open(log_path, 'r').read()
        platform_last_order_num = int(platform_last_order_num)
    except FileNotFoundError:
        platform_last_order_num = None
    return platform_last_order_num


def record_platform_order_num(platform, order_num):
    log_path = f'{conf.log_dir}{os.sep}{platform}.order_num'
    f = open(log_path, 'w')
    f.write(str(order_num))
    f.close()


def send_email(subject, content):
    """发送邮件"""
    sender = '1345325190@qq.com' # 发送者邮件
    password = 'hlugbxacqrpsgfji' # 发送者授权码
    receiver = 'zhou.huajian@foxmail.com' # 接收者邮件

    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(['李远香', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["周华健", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = subject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
        log('邮件发送成功')
    except Exception:
        log('邮件发送失败')
