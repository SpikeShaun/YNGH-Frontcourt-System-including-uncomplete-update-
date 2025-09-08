# -*- coding=utf-8 -*-
# @Time:18/4/2025 下午 3:38
# @Author:席灏铖
# @File:baidu_pan.PY
# @Software:PyCharm
# baidu_pan.py
import os
import json
import requests
from config import Config
from datetime import datetime

# ================== 通用函数 ==================

def get_headers():
    return {
        "Authorization": f"Bearer {Config.BDP_ACCESS_TOKEN}"
    }

def ensure_remote_dir(path):
    """
    尝试创建远程目录，如果已存在则跳过
    """
    url = f"https://pan.baidu.com/rest/2.0/xpan/file?method=create&access_token={Config.BDP_ACCESS_TOKEN}"
    params = {
        "path": path,
        "isdir": "1"
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        print(f"✅ 远程目录已存在/创建成功：{path}")
    else:
        print(f"⚠️ 创建目录失败（可能已存在）：{path}")

# ================== 上传 JSON 数据 ==================

def upload_json_to_pan(data: dict, project_code: str):
    """
    将客户填写信息以JSON格式上传到指定项目目录中
    """
    folder_path = os.path.join(Config.BDP_ROOT_DIR, "客户登记表", project_code)
    ensure_remote_dir(folder_path)

    # 文件名按时间戳命名
    filename = f"{data.get('supplier_name', '未命名')}_{datetime.now().strftime('%Y%m%d%H%M')}.json"
    local_path = os.path.join("temp_uploads", filename)
    os.makedirs("temp_uploads", exist_ok=True)

    with open(local_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    remote_path = f"{folder_path}/{filename}"
    upload_file_to_pan(local_path, remote_path)
    os.remove(local_path)

# ================== 上传任意文件（如磋商文件） ==================

def upload_file_to_pan(local_path: str, remote_path: str):
    """
    使用百度PCS（超级简单上传）API 上传文件
    """
    print(f"⬆️ 正在上传文件：{local_path} 到 {remote_path}")

    upload_url = "https://d.pcs.baidu.com/rest/2.0/pcs/file"
    params = {
        "method": "upload",
        "access_token": Config.BDP_ACCESS_TOKEN,
        "path": remote_path,
        "ondup": "overwrite"
    }
    try:
        with open(local_path, "rb") as f:
            response = requests.post(upload_url, params=params, files={"file": f})
        if response.status_code == 200:
            print(f"✅ 上传成功：{remote_path}")
            return True
        else:
            print(f"❌ 上传失败：{response.status_code} | {response.text}")
            return False
    except Exception as e:
        print(f"❌ 上传异常：{e}")
        return False
