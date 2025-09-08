# 云南国合开标前台系统（Bidding Front Desk System）

本项目旨在替代传统开标公司前台的人工登记流程，提供一个全流程电子化的投标信息管理系统。系统支持客户信息填写、项目发布、财务缴费标记、邮件分发磋商文件等核心业务流程。

## 🔧 技术栈

- 后端框架：Python + Flask
- 数据存储：百度网盘（主）、SQLite（缓存）
- 前端页面：Jinja2 + Bootstrap5
- 文件处理：PDF / Word 附件上传与邮件发送
- 云服务：支持部署到阿里云 / 腾讯云

## 📂 项目结构

```bash
├── app.py              # 主程序
├── models.py           # 数据模型定义
├── baidu_pan.py        # 百度网盘上传模块
├── email_utils.py      # 邮件发送模块
├── utils.py            # 通用工具函数
├── templates/          # 所有页面模板（index, admin, success等）
├── static/             # 静态资源（样式、JS、背景图）
├── data/sqlite.db      # 本地缓存数据库
├── docs/               # 文档（你正在看的这份）
├── requirements.txt    # Python依赖列表


