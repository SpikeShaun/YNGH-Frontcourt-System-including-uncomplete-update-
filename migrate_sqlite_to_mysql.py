# -*- coding=utf-8 -*-
# @Time:9/5/2025 上午 10:10
# @Author:席灏铖
# @File:migrate_sqlite_to_mysql.PY
# @Software:PyCharm
# -*- coding: utf-8 -*-
# migrate_sqlite_to_mysql.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import app, db  # 引入你的 Flask 应用和 SQLAlchemy 实例
from models import Project, Bid, Leader, Admin, MailLog

# 创建 SQLite 连接
sqlite_engine = create_engine('sqlite:///data/sqlite.db')
SqliteSession = sessionmaker(bind=sqlite_engine)
sqlite_session = SqliteSession()


def clean(obj):
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}


# ✅ 使用 Flask 应用上下文执行迁移
with app.app_context():
    print("🚀 正在迁移 Project 表...")
    for item in sqlite_session.query(Project).all():
        db.session.add(Project(**clean(item)))

    print("🚀 正在迁移 Leader 表...")
    for item in sqlite_session.query(Leader).all():
        db.session.add(Leader(**clean(item)))

    print("🚀 正在迁移 Admin 表...")
    for item in sqlite_session.query(Admin).all():
        db.session.add(Admin(**clean(item)))

    print("🚀 正在迁移 Bid 表（自动去重）...")
    seen_keys = set()  # 用于记录已插入的唯一键组合
    skip_count = 0

    for item in sqlite_session.query(Bid).all():
        cleaned = clean(item)
        key = (cleaned['project_id'], cleaned['supplier_name'], cleaned['credit_code'])

        if key in seen_keys:
            skip_count += 1
            print(f"⚠️ 已跳过重复 Bid：项目ID={key[0]}，供应商={key[1]}，信用代码={key[2]}")
            continue

        seen_keys.add(key)
        db.session.add(Bid(**cleaned))

    try:
        db.session.commit()
        print(f"✅ Bid 表迁移完成（共跳过重复记录 {skip_count} 条）")
    except Exception as e:
        db.session.rollback()
        print(f"❌ Bid 表迁移失败：{e}")

    print("🚀 正在迁移 MailLog 表...")
    for item in sqlite_session.query(MailLog).all():
        db.session.add(MailLog(**clean(item)))

    try:
        db.session.commit()
        print("✅ 全部迁移完成！")
    except Exception as e:
        db.session.rollback()
        print(f"❌ 迁移失败：{e}")
