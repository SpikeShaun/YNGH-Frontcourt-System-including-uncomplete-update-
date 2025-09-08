# -*- coding=utf-8 -*-
# @Time:9/5/2025 上午 10:54
# @Author:席灏铖
# @File:export_mysql_backup.PY
# @Software:PyCharm
import os

def export_mysql_backup():
    output_path = "data/database_mysql.sql"
    os.makedirs("data", exist_ok=True)

    mysql_user = "root"
    # mysql_user = "admin"
    mysql_password = "gaojingyue813!@"
    database_name = "toubiao_db"

    command = f'mysqldump -u {mysql_user} -p"{mysql_password}" --databases {database_name} > {output_path}'
    # command = f'/usr/bin/mysqldump -u {mysql_user} -p"{mysql_password}" --databases {database_name} > {output_path}'

    exit_code = os.system(command)

    if exit_code == 0:
        print(f"✅ 备份成功，文件保存在 {output_path}")
        return output_path
    else:
        print("❌ 备份失败，请检查 MySQL 配置和路径")
        return None
