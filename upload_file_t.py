# -*- coding=utf-8 -*-
# @Time:6/5/2025 下午 5:27
# @Author:席灏铖
# @File:test_upload_file.PY
# @Software:PyCharm
# upload_file_t.py
from oss import upload_file_to_oss

# 指定本地文件路径和 OSS 中的目标路径
local_file = "static/downloads/Statistics/YNGH[2025]-425 文件获取统计表.xlsx"
oss_path = "测试文件/YNGH[2025]-425 文件获取统计表.xlsx"

try:
    upload_file_to_oss(local_file, oss_path)
    print("✅ 文件上传成功！")
except Exception as e:
    print(f"❌ 上传失败：{e}")