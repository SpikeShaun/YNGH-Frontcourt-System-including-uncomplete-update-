# -*- coding=utf-8 -*-
# @Time:18/4/2025 下午 3:39
# @Author:席灏铖
# @File:email_utils.PY
# @Software:PyCharm
# email_utils.py





import smtplib
import os
import glob
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr
from config import Config
from oss import download_file_from_oss, oss_file_exists  # 确保你有这两个函数
MAX_ATTACHMENT_SIZE = 50 * 1024 * 1024  # 附件最大 50MB

def find_real_file(base_name: str, folder: str = "static/uploads") -> str:
    """
    在 static/uploads 中查找真实文件名（支持中括号等特殊符号）
    """
    safe_base = glob.escape(base_name)
    search_pattern = os.path.join(Config.BASE_DIR, folder, f"{safe_base}.*")
    matches = glob.glob(search_pattern)
    return matches[0] if matches else None


def send_email_with_attachment(
    recipient_email: str,
    subject: str,
    body: str,
    base_filename: str = None  # 不含扩展名的文件名（用于匹配附件）
) -> dict:
    """
    发送带附件的邮件（自动查找实际扩展名），返回 dict 表示结果。
    """
    try:
        absolute_path = None

        # 自动查找真实文件
        if base_filename:
            absolute_path = find_real_file(base_filename)

            # ✅ 如果本地没找到，尝试从 OSS 下载
            if not absolute_path:
                print(f"⚠️ 本地未找到 {base_filename}.*，尝试从 OSS 下载")
                uploads_dir = os.path.join(Config.BASE_DIR, 'static', 'uploads')
                os.makedirs(uploads_dir, exist_ok=True)
                for ext in ['.pdf', '.docx', '.doc', '.zip', '.rar']:
                    oss_key = f"项目附件/{base_filename}{ext}"
                    absolute_path_candidate = os.path.join(uploads_dir, f"{base_filename}{ext}")
                    if oss_file_exists(oss_key):  # ✅ 你自己实现的检查函数
                        download_file_from_oss(oss_key, absolute_path_candidate)
                        absolute_path = absolute_path_candidate
                        break

            if not absolute_path:
                raise FileNotFoundError(f"未找到附件文件：{base_filename}.*（本地和 OSS 均缺失）")

            # print(f"📎 附件的绝对路径: {absolute_path}")
            file_size = os.path.getsize(absolute_path)
            # print(f"📎 附件大小: {file_size / 1024:.2f} KB")

            if file_size == 0:
                raise Exception("附件大小为 0，无法发送空文件")
            if file_size > MAX_ATTACHMENT_SIZE:
                raise Exception(f"附件大小超过限制（最大 {MAX_ATTACHMENT_SIZE / 1024 / 1024}MB）")

        # 构建邮件内容
        msg = MIMEMultipart()
        msg['From'] = formataddr(("云南国合", Config.MAIL_USERNAME))
        msg['To'] = formataddr(("客户", recipient_email))
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # 添加附件
        if absolute_path:
            with open(absolute_path, 'rb') as f:
                part = MIMEApplication(f.read())
                part.add_header(
                    'Content-Disposition',
                    'attachment',
                    filename=os.path.basename(absolute_path)
                )
                msg.attach(part)

        # 连接 SMTP 并发送邮件
        with smtplib.SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT) as server:
            server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            server.sendmail(Config.MAIL_USERNAME, [recipient_email], msg.as_string())

        print(f"✅ 邮件发送成功 → {recipient_email}")
        return {"status": "success"}

    except Exception as e:
        print(f"❌ 邮件发送失败 → {recipient_email}")
        traceback.print_exc()
        return {"status": "failed", "error": str(e)}


# import smtplib
# import os
# import traceback
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email.utils import formataddr
# from config import Config
#
# MAX_ATTACHMENT_SIZE = 20 * 1024 * 1024  # 20MB 限制
#
# def send_email_with_attachment(
#     recipient_email: str,
#     subject: str,
#     body: str,
#     attachment_path: str = None,
#     attachment_name: str = None
# ) -> dict:
#     """
#     发送带附件的邮件，成功返回 {"status": "success"}，失败返回 {"status": "failed", "error": err_msg}
#     """
#
#     try:
#         # 如果附件路径是相对路径，需要转换为绝对路径
#         if attachment_path:
#             absolute_path = os.path.join(Config.BASE_DIR, attachment_path)
#             print(f"📎 附件的绝对路径: {absolute_path}")
#
#             # 检查附件大小
#             file_size = os.path.getsize(absolute_path)
#             print(f"📎 附件大小: {file_size / 1024:.2f} KB")
#
#             if file_size == 0:
#                 raise Exception("附件大小为 0，无法发送空文件")
#
#             if file_size > MAX_ATTACHMENT_SIZE:
#                 raise Exception(f"附件大小超过限制（最大 {MAX_ATTACHMENT_SIZE / 1024 / 1024}MB）")
#
#         # 邮件内容构建
#         msg = MIMEMultipart()
#         msg['From'] = formataddr(("云南国合开标系统", Config.MAIL_USERNAME))
#         msg['To'] = formataddr(("客户", recipient_email))
#         msg['Subject'] = subject
#
#         # 添加正文
#         msg.attach(MIMEText(body, 'plain', 'utf-8'))
#
#         # 添加附件
#         if attachment_path:
#             with open(absolute_path, 'rb') as f:
#                 part = MIMEApplication(f.read())
#                 part.add_header(
#                     'Content-Disposition',
#                     'attachment',
#                     filename=(attachment_name or os.path.basename(absolute_path))
#                 )
#                 msg.attach(part)
#
#         # 连接 SMTP 并发送
#         with smtplib.SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT) as server:
#             server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
#             server.sendmail(Config.MAIL_USERNAME, [recipient_email], msg.as_string())
#
#         print(f"✅ 邮件发送成功 → {recipient_email}")
#         return {"status": "success"}
#
#     except Exception as e:
#         print(f"❌ 邮件发送失败 → {recipient_email}")
#         traceback.print_exc()  # 打印详细错误信息，帮助定位问题
#         return {"status": "failed", "error": str(e)}




# -*- coding=utf-8 -*-
# @Time: 2025-04-22
# @Author: 席灏铖
# @File: email_utils.py

# import smtplib
# import os
# import traceback
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email.utils import formataddr
# from config import Config
#
# MAX_ATTACHMENT_SIZE = 20 * 1024 * 1024  # 20MB 限制
#
# def send_email_with_attachment(
#     recipient_email: str,
#     subject: str,
#     body: str,
#     attachment_path: str = None,
#     attachment_name: str = None
# ) -> dict:
#     try:
#         # ========== 附件检查 ==========
#         if attachment_path:
#             absolute_path = os.path.abspath(attachment_path)
#             print(f"\n📎 [邮件调试] 附件路径: {absolute_path}")
#
#             if not os.path.exists(absolute_path):
#                 raise FileNotFoundError(f"找不到附件文件：{absolute_path}")
#
#             file_size = os.path.getsize(absolute_path)
#             print(f"📎 [邮件调试] 附件大小: {file_size / 1024:.2f} KB")
#
#             if file_size == 0:
#                 raise Exception("附件大小为 0，无法发送空文件")
#
#             if file_size > MAX_ATTACHMENT_SIZE:
#                 raise Exception(f"附件大小超过限制（最大 {MAX_ATTACHMENT_SIZE / 1024 / 1024}MB）")
#
#         # ========== 邮件构建 ==========
#         msg = MIMEMultipart()
#         msg['From'] = formataddr(("云南国合开标系统", Config.MAIL_USERNAME))
#         msg['To'] = formataddr(("客户", recipient_email))
#         msg['Subject'] = subject
#
#         # 正文
#         msg.attach(MIMEText(body, 'plain', 'utf-8'))
#
#         # 附件添加
#         if attachment_path:
#             with open(absolute_path, 'rb') as f:
#                 part = MIMEApplication(f.read())
#                 part.add_header(
#                     'Content-Disposition',
#                     'attachment',
#                     filename=(attachment_name or os.path.basename(attachment_path))
#                 )
#                 msg.attach(part)
#
#         # ========== 邮件发送 ==========
#         with smtplib.SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT) as server:
#             server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
#             server.sendmail(Config.MAIL_USERNAME, [recipient_email], msg.as_string())
#
#         print(f"✅ 邮件发送成功 → {recipient_email}")
#         return {"status": "success"}
#
#     except Exception as e:
#         print(f"❌ 邮件发送失败 → {recipient_email}")
#         traceback.print_exc()
#         return {"status": "failed", "error": str(e)}
