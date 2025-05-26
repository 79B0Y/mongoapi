#!/bin/bash
# MongoAPI systemd 安装脚本

SERVICE_NAME="mongoapi"
APP_DIR="/opt/mongoapi"
VENV_DIR="$APP_DIR/venv"
LOG_FILE="/var/log/mongoapi.log"

# 1. 拷贝程序目录（假设当前在 mongoapi_status_final 根目录）
mkdir -p "$APP_DIR"
cp -r mongoapi configuration.yaml requirements.txt setup.py "$APP_DIR"

# 2. 创建虚拟环境并安装依赖
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install .
deactivate

# 3. 创建 systemd 服务文件
cat <<EOF | sudo tee /etc/systemd/system/$SERVICE_NAME.service
[Unit]
Description=MongoAPI Service
After=network.target

[Service]
Type=simple
WorkingDirectory=$APP_DIR
ExecStart=$VENV_DIR/bin/mongoapi
Restart=always
StandardOutput=append:$LOG_FILE
StandardError=append:$LOG_FILE

[Install]
WantedBy=multi-user.target
EOF

# 4. 启用并启动服务
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

# 5. 显示服务状态
sudo systemctl status $SERVICE_NAME --no-pager
