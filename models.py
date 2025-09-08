# -*- coding=utf-8 -*-
# @Time:18/4/2025 下午 3:36
# @Author:席灏铖
# @File:models.PY
# @Software:PyCharm
# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()
# 组长-项目 多对多关系表（项目组成员）
project_members = db.Table('project_members',
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'), primary_key=True),
    db.Column('leader_id', db.Integer, db.ForeignKey('leaders.id'), primary_key=True)
)


# ================== 管理员表（可选） ==================
class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # 密码可加密
    email = db.Column(db.String(120), nullable=False)  # 企业邮箱

'''
Project 表只负责记录名字、编号；

所有招标信息（时间、成员、文件等）都放进 SubProject 表；

原来的 project_id 替换为 sub_project_id；

若某项目不分标段，就创建一个 SubProject，其 segment_name=None；

数据展示时判断：若该项目下只有一个标段，就默认展示它。

'''
# ================== 项目表 ==================
# 替换原来的 Project 表定义（精简：移除 start_time、deadline 等）
class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)  # 项目名称
    code = db.Column(db.String(50), nullable=False)   # 项目编号（允许重复）
    created_at = db.Column(db.DateTime, default=datetime.now)

    purchaser = db.Column(db.String(100), nullable=True)  # ✅ 新增：采购人
    budget_amount = db.Column(db.Float, nullable=True)    # ✅ 新增：采购金额

    leader_email = db.Column(db.String(120), nullable=False)

    is_segmented = db.Column(db.Boolean, default=False)  # ✅ 新增：是否为多标段项目

    # ✅ 成员：多对多关系
    members = db.relationship('Leader', secondary='project_members', backref='projects')

    # ✅ 标段列表：一对多关系
    sub_projects = db.relationship('SubProject', back_populates='project', cascade='all, delete-orphan')

    # ✅ 仅用于 is_segmented=False 的情况
    start_time = db.Column(db.DateTime, nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    deposit_amount = db.Column(db.Float, default=0.0)
    file_path = db.Column(db.String(255), nullable=True)

    __table_args__ = (
        db.Index('idx_code_created_at', 'code', 'created_at'),
    )

    def __repr__(self):
        return f"<Project {self.code} - {self.name}>"


# class Project(db.Model):
#     __tablename__ = 'projects'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)  # 项目名称
#     code = db.Column(db.String(50), unique=True, nullable=False)  # 项目编号
#     start_time = db.Column(db.DateTime, nullable=False)  # 文件获取开始时间
#     deadline = db.Column(db.DateTime, nullable=False)  # 文件获取截止时间
#     deposit_amount = db.Column(db.Float, default=0.0)  # 保证金金额
#     is_paid = db.Column(db.Boolean, default=False)  # 项目级别是否缴费（很少用，备用）
#     file_path = db.Column(db.String(255), nullable=False)
#     # 磋商文件路径（本地或百度网盘链接）
#
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
#
#     # 项目组长邮箱
#     leader_email = db.Column(db.String(120), nullable=False)
#     # ✅ 项目组成员多对多关系（基于 Leaders 表）
#     members = db.relationship('Leader', secondary=project_members, backref='member_projects')
#     # # 关系：一个项目下面有多个客户投标记录
#     # bids = db.relationship('Bid', backref='project', lazy=True)
#     # 反向关系：指定 Bid 表中关联字段是 project
#     bids = db.relationship('Bid', back_populates='project', cascade='all, delete-orphan')
#
#     def __repr__(self):
#         return f"<Project {self.code} - {self.name}>"


# ================== 标段表 ==================
class SubProject(db.Model):
    __tablename__ = 'sub_projects'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    round = db.Column(db.Integer, default=1)  # 第几次招标：默认1（初次）、2（二次）...
    segment_name = db.Column(db.String(100), nullable=True)  # “一标段”、“二标段”；若为 None 表示默认标段

    deposit_amount = db.Column(db.Float, default=0.0)
    file_path = db.Column(db.String(255), nullable=True)



    project = db.relationship('Project', back_populates='sub_projects')
    bids = db.relationship('Bid', back_populates='sub_project', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<SubProject #{self.id} P{self.project_id} - {self.segment_name or '默认标段'}>"





class Bid(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    sub_project_id = db.Column(db.Integer, db.ForeignKey('sub_projects.id'), nullable=False)

    supplier_name = db.Column(db.String(100), nullable=False)
    supplier_address = db.Column(db.String(200), nullable=False)
    legal_person = db.Column(db.String(50), nullable=False)
    credit_code = db.Column(db.String(50), nullable=False)
    agent = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    file_method = db.Column(db.String(100), nullable=True)
    file_time = db.Column(db.String(50), nullable=False)
    is_paid = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.now)

    sub_project = db.relationship('SubProject', back_populates='bids')

    __table_args__ = (
        UniqueConstraint('supplier_name', 'credit_code', 'sub_project_id', name='uq_supplier_subproject'),
    )

    def __repr__(self):
        return f"<Bid {self.id}, SubProject ID: {self.sub_project_id}, Supplier: {self.supplier_name}>"

# class Bid(db.Model):
#     __tablename__ = 'bids'
#
#     id = db.Column(db.Integer, primary_key=True)
#     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
#
#     supplier_name = db.Column(db.String(100), nullable=False)
#     supplier_address = db.Column(db.String(200), nullable=False)
#     legal_person = db.Column(db.String(50), nullable=False)
#     credit_code = db.Column(db.String(50), nullable=False)
#     agent = db.Column(db.String(50), nullable=True)
#     phone = db.Column(db.String(30), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     file_method = db.Column(db.String(100), nullable=True)
#     file_time = db.Column(db.String(50), nullable=False)
#     is_paid = db.Column(db.Boolean, default=False)
#     status = db.Column(db.String(20), default='pending')  # 投标记录状态，默认未确认提交
#     created_at = db.Column(db.DateTime, default=datetime.now)
#
#     # 关系字段：明确指定反向字段名为 project.bids
#     project = db.relationship('Project', back_populates='bids')
#
#     __table_args__ = (
#         UniqueConstraint('supplier_name', 'credit_code', 'project_id', name='uq_supplier_project'),
#     )
#
#     def __repr__(self):
#         return f"<Bid {self.id}, Project ID: {self.project_id}, Supplier: {self.supplier_name}>"
#

# class MailLog(db.Model):
#     __tablename__ = 'mail_logs'
#
#     id = db.Column(db.Integer, primary_key=True)
#     bid_id = db.Column(db.Integer, db.ForeignKey('bids.id'), nullable=True)  # ✅ 改成nullable=True
#     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)  # ✅ 也记录project_id
#     status = db.Column(db.String(20))
#     message = db.Column(db.Text)
#     sent_at = db.Column(db.DateTime, default=datetime.now)
#
#     # 外键关系（可选）
#     project = db.relationship('Project')
#     bid = db.relationship('Bid')
class MailLog(db.Model):
    __tablename__ = 'mail_logs'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)  # ✅ 新增字段
    bid_id = db.Column(db.Integer, db.ForeignKey('bids.id'), nullable=True)
    sub_project_id = db.Column(db.Integer, db.ForeignKey('sub_projects.id'), nullable=True)
    status = db.Column(db.String(20))
    message = db.Column(db.Text)
    sent_at = db.Column(db.DateTime, default=datetime.now)

    bid = db.relationship('Bid')
    sub_project = db.relationship('SubProject')
    project = db.relationship('Project')  # 如果你希望可以直接通过 .project 调用，也可以加

class Leader(db.Model):
    __tablename__ = 'leaders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Leader {self.name} - {self.email}>"


# ================== 数据库初始化函数 ==================
def init_db():
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
    # db.drop_all()
    db.create_all()
    print("✅ 数据库已初始化，包括 Project、Bid、Admin、MailLog 表")
