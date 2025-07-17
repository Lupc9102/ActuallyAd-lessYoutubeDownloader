from flask import Flask, request, send_file, jsonify
from downloader import download_video
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")
    format = data.get("format")

    if not url or format not in ["mp3", "mp4"]:
        return jsonify({"error": "Invalid input"}), 400

    try:
        filepath = download_video(url, format)
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    app.run(debug=True)