from flask import Flask, request, jsonify

app = Flask(__name__)
last_speech = "..."

@app.route("/")
def home():
    return jsonify({"message": "Speech API is running", "endpoints": {"/speech": "GET/POST"}})

@app.route("/speech", methods=["GET", "POST"])
def handle_speech():
    global last_speech

    if request.method == "POST":
        try:
            data = request.get_json()
            if data and "speech" in data:
                last_speech = data["speech"]
                return jsonify({"status": "ok", "received": last_speech})
            return jsonify({"status": "error", "message": "No speech found"}), 400
        except:
            return jsonify({"status": "error", "message": "Invalid JSON"}), 400

    return jsonify({"speech": last_speech})
