from flask import Flask
from flask import render_template
from flask import url_for 
from flask import current_app
from flask import redirect, request, jsonify, send_file
import subprocess
import os

app = Flask(__name__, template_folder='templates')
app.app_context()

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_file():
    data = request.json 
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    file_path = os.path.join(DOWNLOAD_DIR, "video.mp4")

    result = subprocess.run(f"yt-dlp -f 'bestvideo+bestaudio/best' --recode-video mp4 -o {file_path} {url}", shell=True, capture_output=True, text=True)

    return send_file(file_path, as_attachment=True);


@app.route('/')
def webpage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)

