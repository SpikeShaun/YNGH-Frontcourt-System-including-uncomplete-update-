# -*- coding=utf-8 -*-
# @Time:30/4/2025 下午 3:46
# @Author:席灏铖
# @File:insert_leaders.PY
# @Software:PyCharm

from app import app, db
from models import Leader

# 项目组长数据（姓名 + 邮箱）
leader_data = [
    {"name": "苏雪冬", "email": "361077078@qq.com"},
    {"name": "马爱佳", "email": "851502638@qq.com"},
    {"name": "蒋立", "email": "1193988365@qq.com"},
    {"name": "张育玮", "email": "549839908@qq.com"},
    {"name": "李昂", "email": "1215774156@qq.com"},
    {"name": "何云艳", "email": "740211471@qq.com"},
    {"name": "张杰", "email": "645231114@qq.com"},
    {"name": "袁思猛", "email": "1023207130@qq.com"},
    {"name": "朱大洲", "email": "2113800357@qq.com"},
    {"name": "高铭", "email": "1812651346@qq.com"},
    {"name": "施江艳", "email": "2822611109@qq.com"},
    {"name": "赵津仪", "email": "122841989@qq.com"},
    {"name": "林艳平", "email": "920167135@qq.com"},
    {"name": "何甜甜", "email": "2419801535@qq.com"},
    {"name": "房雨雷", "email": "1430684282@qq.com"},
    {"name": "张国辉", "email": "3330807194@qq.com"},
    {"name": "李锦香", "email": "839029321@qq.com"},
    {"name": "陈学敏", "email": "450077893@qq.com"},
    {"name": "王云文", "email": "2039479437@qq.com"},
    {"name": "张凤阳", "email": "2624654686@qq.com"},
    {"name": "杨云鹏", "email": "420031465@qq.com"},
    {"name": "武江艳", "email": "693549110@qq.com"},
    {"name": "张静楠", "email": "1525053382@qq.com"},
    {"name": "郭琼", "email": "1730394096@qq.com"},
    {"name": "常焱茗", "email": "1162193179@qq.com"},
    {"name": "周翔丽", "email": "20909691@qq.com"},
    {"name": "杨天秀", "email": "251400160@qq.com"},
    {"name": "蒋翔", "email": "648504278@qq.com"},
    {"name": "王林伟", "email": "1457454721@qq.com"},
    {"name": "李灿辉", "email": "306626194@qq.com"},
    {"name": "冯丽", "email": "763455921@qq.com"},
]

with app.app_context():
    added, skipped = 0, 0
    for item in leader_data:
        if not Leader.query.filter_by(name=item["name"]).first():
            db.session.add(Leader(name=item["name"], email=item["email"]))
            added += 1
        else:
            skipped += 1
    db.session.commit()
    print(f"✅ 导入完成：新增 {added} 条，跳过 {skipped} 条（已存在）")
