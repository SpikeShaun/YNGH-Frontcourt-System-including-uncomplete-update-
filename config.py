# -*- coding=utf-8 -*-
# @Time: 18/4/2025 下午 3:32
# @Author: 席灏铖
# @File: config.py
# @Software: PyCharm

import os
from werkzeug.security import generate_password_hash, check_password_hash

class Config:
    # ============ 系统核心 ============
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # ============ 数据库配置（MySQL缓存） ============
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data', 'sqlite.db')
    # 本地
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gaojingyue813!%40@localhost:3306/toubiao_db?charset=utf8mb4'
    # todo： 在这里创建你的MySQL数据库连接，我使用的是navicat，你随意
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gaojingyue813!%40@localhost:3306/yngh_new?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ecs上的mysql
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:gaojingyue813!@47.108.137.36:3306/toubiao_db?charset=utf8mb4'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:gaojingyue813!@localhost:3306/toubiao_db?charset=utf8mb4'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ============ 管理员信息 ============
    # 使用generate_password_hash()加密管理员密码
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "yngh")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", generate_password_hash("yngh123"))  # 默认密码加密
    ADMIN_EMAIL = "shaun7565@163.com"  # 可用于邮件回执或通知抄送

    # ============ 企业邮箱配置 ============
    # 企业邮箱配置（此处为163邮箱）
    MAIL_SERVER = "smtp.163.com"  # 163邮箱的SMTP服务器地址
    MAIL_PORT = 465  # 163 邮箱使用 SSL 时，端口是 465
    MAIL_USE_SSL = True  # 开启 SSL 加密
    MAIL_USERNAME = "ghzb2006@163.com"  # 你的163邮箱地址
    MAIL_PASSWORD = "KYevz4u4UbksQ6yD"  # 163邮箱的授权码
    MAIL_DEFAULT_SENDER = MAIL_USERNAME  # 默认发件人（这里通常和 MAIL_USERNAME 相同）    MAIL_SERVER = "smtp.163.com"  # 163邮箱的SMTP服务器地址

    # MAIL_SERVER = "smtp.qq.com"  # 邮箱服务商
    # MAIL_PORT = 465  # SSL端口
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = "1753379509@qq.com"  # 你的邮箱地址
    # MAIL_PASSWORD = "mashpgosfmkdeabj"  # 邮箱授权码（不是邮箱密码）
    # MAIL_DEFAULT_SENDER = MAIL_USERNAME  # 默认发件人

    # ============ 百度网盘 API 相关 ============
    BDP_APP_ID = "your_baidu_app_id"
    BDP_CLIENT_ID = "your_client_id"
    BDP_CLIENT_SECRET = "your_client_secret"
    BDP_ACCESS_TOKEN = "your_access_token"
    BDP_ROOT_DIR = "/开标系统数据/"  # 主文件存储目录
    BDP_UPLOAD_TEMP_DIR = "temp_uploads"  # 本地临时缓存目录（安全上传中转）

    # ============ 阿里云网盘oss API 相关 ============
    # config.py 中新增
    OSS_ACCESS_KEY_ID = os.getenv("OSS_ACCESS_KEY_ID", "LTAI5tKGX7wvPkqPYEdqSnDA")
    OSS_ACCESS_KEY_SECRET = os.getenv("OSS_ACCESS_KEY_SECRET", "F0A6Sr45gaN0itvIMWV5hftOoqiVvP")
    OSS_ENDPOINT = "https://oss-cn-chengdu.aliyuncs.com"  # 替换为你的 Endpoint
    OSS_BUCKET_NAME = "yunnanguoheft-oss"  # 替换为你的 Bucket 名称

    # ============ 文件上传限制 ============
    MAX_FILE_SIZE_MB = 50
    ALLOWED_EXTENSIONS = {'.pdf', '.doc', '.docx', '.zip', '.rar'}

    # ============ 文件上传路径 ============
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')  # 设置上传文件的目录

    # ============ 营业时间控制 ============
    BUSINESS_START = (9, 0)   # 09:00
    BUSINESS_END = (17, 0)    # 17:00

    # ============ 定时任务（保留项） ============
    CLEANUP_INTERVAL_DAYS = 30  # 每30天上传一次数据备份并清理本地缓存
