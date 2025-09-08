# -*- coding=utf-8 -*-
# @Time:23/4/2025 下午 3:25
# @Author:席灏铖
# @File:run_model.PY
# @Software:PyCharm
# init_db_once.py
from app import app
from models import init_db

with app.app_context():
    init_db()  # 自动创建数据库文件和所有表
    print("✅ 所有表格创建成功！")

# from app import app, db
# from models import Leader
#
# with app.app_context():
#     db.create_all()  # 自动在数据库中添加缺失的表
#     print("✅ Leader 表创建成功（如果还不存在）")
