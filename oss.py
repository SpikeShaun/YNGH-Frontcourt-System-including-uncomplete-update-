# -*- coding=utf-8 -*-
# @Time:30/4/2025 上午 9:42
# @Author:席灏铖
# @File:oss.py
# @Software:PyCharm

import oss2
import os
import json
from config import Config

# ========== 初始化 OSS 客户端 ==========
auth = oss2.Auth(Config.OSS_ACCESS_KEY_ID, Config.OSS_ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, Config.OSS_ENDPOINT, Config.OSS_BUCKET_NAME)

# ========== 上传本地文件 ==========
def upload_file_to_oss(local_path, remote_path):
    """
    将本地文件上传到 OSS
    :param local_path: 本地文件路径
    :param remote_path: OSS 目标路径，如 '项目附件/xxx.docx'
    """
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"本地文件不存在：{local_path}")

    with open(local_path, 'rb') as file_obj:
        bucket.put_object(remote_path, file_obj)
        print(f"✅ 上传成功 → OSS路径: {remote_path}")

# ========== 上传 dict 为 JSON ==========
def upload_json_to_oss(data: dict, remote_path: str):
    """
    将 dict 数据作为 JSON 字符串上传到 OSS
    :param data: Python 字典
    :param remote_path: OSS 路径，例如 '项目JSON/xxx.json'
    """
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    bucket.put_object(remote_path, json_str.encode('utf-8'))
    print(f"✅ JSON 上传成功 → OSS路径: {remote_path}")

# ========== 获取文件访问地址 ==========
def get_oss_url(oss_key):
    """
    根据上传路径生成 OSS 公网访问 URL
    :param oss_key: OSS 中的对象路径，如 '项目附件/xxx.docx'
    :return: 完整的访问 URL
    """
    endpoint = Config.OSS_ENDPOINT.replace('https://', '')
    return f"https://{Config.OSS_BUCKET_NAME}.{endpoint}/{oss_key}"


# 删除 OSS 上的旧文件
def delete_file_from_oss(remote_path):
    """
    删除 OSS 上的指定文件
    :param remote_path: OSS 路径，如 '项目附件/xxx.docx'
    """
    try:
        bucket.delete_object(remote_path)
        print(f"🗑 已删除 OSS 文件 → {remote_path}")
    except oss2.exceptions.NoSuchKey:
        print(f"⚠️ OSS 上找不到该文件：{remote_path}")

# # 一键从 OSS 拉取 data/sqlite.db 并替换当前本地文件，适用于灾难恢复。
# def restore_db_from_oss():
#     """
#     从 OSS 下载最新数据库文件，恢复本地 sqlite.db。
#     注意：这将覆盖当前本地数据库！
#     """
#     remote_path = "数据库/sqlite.db"
#     local_path = os.path.join("data", "sqlite.db")
#
#     try:
#         result = bucket.get_object(remote_path)
#         os.makedirs(os.path.dirname(local_path), exist_ok=True)
#         with open(local_path, 'wb') as f:
#             f.write(result.read())
#         print(f"✅ 成功恢复数据库 → 本地路径: {local_path}")
#     except oss2.exceptions.NoSuchKey:
#         print("❌ OSS中不存在数据库备份文件！")
#     except Exception as e:
#         print(f"❌ 数据库恢复失败: {e}")

def oss_file_exists(oss_key: str) -> bool:
    """
    判断 OSS 中是否存在指定文件
    :param oss_key: OSS 路径，如 '项目附件/xxx.docx'
    :return: True 表示存在，False 表示不存在
    """
    try:
        return bucket.object_exists(oss_key)
    except Exception as e:
        print(f"❌ 检查 OSS 文件是否存在失败: {e}")
        return False

def download_file_from_oss(oss_key: str, local_path: str):
    """
    从 OSS 下载指定文件保存到本地
    :param oss_key: OSS 文件路径，如 '项目附件/xxx.docx'
    :param local_path: 本地保存路径，如 'static/uploads/xxx.docx'
    """
    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        bucket.get_object_to_file(oss_key, local_path)
        print(f"✅ 已从 OSS 下载 → 本地: {local_path}")
    except oss2.exceptions.NoSuchKey:
        raise FileNotFoundError(f"OSS 上未找到文件: {oss_key}")
    except Exception as e:
        raise RuntimeError(f"❌ 从 OSS 下载失败: {e}")

# ========== 测试入口（可选） ==========
if __name__ == "__main__":
    # 测试上传本地文件
    local_test_file = "test.txt"
    with open(local_test_file, "w", encoding="utf-8") as f:
        f.write("这是 OSS 文件上传测试内容。")

    remote_file_path = "测试文件/test.txt"
    upload_file_to_oss(local_test_file, remote_file_path)
    print("🌐 文件访问链接:", get_oss_url(remote_file_path))

    # 测试上传 JSON
    data = {"项目": "OSS上传测试", "状态": "成功"}
    remote_json_path = "测试文件/test.json"
    upload_json_to_oss(data, remote_json_path)
    print("🌐 JSON 访问链接:", get_oss_url(remote_json_path))
