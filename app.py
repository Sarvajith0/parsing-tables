from flask import Flask, render_template, request, jsonify
from processor import process_pdf
from pathlib import Path
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)

    # Generate the markdown file
    md_path = process_pdf(pdf_path)

    # Read the generated markdown
    markdown = Path(md_path).read_text()

    return jsonify({
        "markdown": markdown
    })


if __name__ == "__main__":
    app.run(debug=True)