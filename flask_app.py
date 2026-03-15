from flask import Flask, request
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive():
    try:
        data = request.get_json()
        if not data:
            return "no data", 200
        
        folder = f"logs/{datetime.now().strftime('%Y-%m-%d')}"
        os.makedirs(folder, exist_ok=True)
        
        filename = f"{folder}/{int(datetime.now().timestamp())}_{request.remote_addr}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        
        return "ok", 200
    except:
        return "error", 200

if __name__ == '__main__':
    app.run()
