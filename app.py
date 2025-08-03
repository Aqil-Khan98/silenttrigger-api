from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_logs():
    data = request.json
    now = datetime.datetime.now().isoformat()
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{now} - {data}\n")
    return jsonify({"status": "received", "timestamp": now}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
