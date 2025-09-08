# -*- coding=utf-8 -*-
# @Time:7/5/2025 上午 9:49
# @Author:席灏铖
# @File:sync_oss.PY
# @Software:PyCharm
import os
from oss import upload_file_to_oss
from export_mysql_backup import export_mysql_backup  # ✅ 导入你的备份逻辑

# def upload_db_to_oss():
#     """每天凌晨上传 sqlite.db 数据库"""
#     db_path = "data/sqlite.db"
#     if os.path.exists(db_path):
#         upload_file_to_oss(db_path, "数据库/sqlite.db")  # 👈 和本地一致的路径
def upload_db_to_oss():
    """每天凌晨覆盖上传最新 MySQL 数据库备份"""
    backup_path = export_mysql_backup()
    if backup_path and os.path.exists(backup_path):
        # ✅ 覆盖上传到固定路径
        upload_file_to_oss(backup_path, "数据库备份/database_mysql.sql")
    else:
        print("❌ 备份文件不存在，OSS 上传取消")

def sync_static_to_oss():
    """
    每天凌晨同步 static 中四个目录（Registrations、Statistics、uploads、Mail_logs）
    文件若存在则上传，同名则覆盖
    """
    target_dirs = {
        'static/downloads/Registrations': '登记表',
        'static/downloads/Statistics': '统计表',
        'static/uploads': '项目附件',
        'static/downloads/Mail_logs': '自动邮件发送记录',  # ✅ 新增
    }

    for local_root, remote_root in target_dirs.items():
        if not os.path.exists(local_root):
            continue
        for fname in os.listdir(local_root):
            local_path = os.path.join(local_root, fname)
            if os.path.isfile(local_path):
                remote_path = f"{remote_root}/{fname}"
                upload_file_to_oss(local_path, remote_path)
