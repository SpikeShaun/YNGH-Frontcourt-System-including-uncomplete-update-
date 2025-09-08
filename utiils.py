# -*- coding=utf-8 -*-
# @Time:18/4/2025 下午 3:41
# @Author:席灏铖
# @File:utiils.PY
# @Software:PyCharm
# utils.py
from datetime import datetime, time
import re
from config import Config

# =============== 当前时间格式字符串 ===============
def now_string():
    """
    返回当前时间的字符串表示，格式：2025年4月20日15时23分
    """
    return datetime.now().strftime("%Y年%m月%d日%H时%M分")


# =============== 判断是否在营业时间内 ===============
def is_within_business_hours():
    """
    判断当前系统时间是否在配置的营业时间段内
    """
    now = datetime.now().time()
    start_hour, start_minute = Config.BUSINESS_START
    end_hour, end_minute = Config.BUSINESS_END
    return time(start_hour, start_minute) <= now <= time(end_hour, end_minute)


# =============== 模糊匹配项目编号 ===============
def fuzzy_match_project(projects, query_code):
    """
    从项目列表中查找包含某段编号的项目（如输入 0001 可匹配 YNGH[2024]-0001）
    返回匹配列表（可选取第一个）
    """
    query_code = query_code.strip().lower()
    matches = []
    for project in projects:
        if query_code in project.code.lower():
            matches.append(project)
    return matches


# =============== 保证金金额合法性检查 ===============
def is_valid_deposit(deposit_str):
    """
    校验保证金金额是否为合法正数
    """
    try:
        val = float(deposit_str)
        return val >= 0
    except:
        return False


# =============== 格式化项目编号（防止非法字符） ===============
def sanitize_code(code):
    """
    清理项目编号中非法字符（用于创建网盘目录等）
    """
    return re.sub(r'[^A-Za-z0-9\[\]\-_]', '_', code)



