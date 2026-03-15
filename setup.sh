#!/usr/bin/env bash

# Установка зависимостей (Railway сам делает pip install -r requirements.txt, но на всякий случай)
pip install --no-cache-dir -r requirements.txt

# Запуск приложения (Railway смотрит на PORT из env)
python flask_app.py
