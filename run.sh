#!/bin/bash

echo "✅ 正在激活虚拟环境..."
source venv/bin/activate

echo "✅ 启动 Flask 服务..."
export FLASK_APP=app.py
export FLASK_ENV=development  # 或 production
flask run --host=0.0.0.0 --port=8000
