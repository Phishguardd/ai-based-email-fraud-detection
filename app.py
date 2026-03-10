from flask import Flask, request, jsonify
from backend.detection_engine import analyze_email
from flask import render_template
from backend.ocr_engine import extract_text_from_image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    data = request.get_json()
    email_text = data.get("email_text", "")
    result = analyze_email(email_text)
    return jsonify(result)


@app.route("/analyze-image", methods=["POST"])
def analyze_image():
    if "image" not in request.files:
        return {"error": "No image file provided"}, 400

    image_file = request.files["image"]
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
    image_file.save(image_path)

    extracted_text = extract_text_from_image(image_path)
    result = analyze_email(extracted_text)

    return jsonify(result)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)