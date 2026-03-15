#!/usr/bin/env bash

# Railpack сам устанавливает requirements.txt перед запуском, но на всякий случай
pip install --no-cache-dir -r requirements.txt || true

# Запуск Flask-сервера
exec python flask_app.py
