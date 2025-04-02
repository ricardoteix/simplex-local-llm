import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify, render_template
from embed import embed
from query import query
import markdown

TEMP_FOLDER = os.getenv('TEMP_FOLDER', './_temp')
os.makedirs(TEMP_FOLDER, exist_ok=True)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/embed_form')
def embed_form():
    return render_template('embed_form.html')


@app.route('/query_form')
def query_form():
    return render_template('query_form.html')


@app.route('/embed', methods=['POST'])
def route_embed():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    embedded = embed(file)

    if embedded:
        return jsonify({"message": "File embedded successfully"}), 200

    return jsonify({"error": "File embedded unsuccessfully"}), 400

@app.route('/query', methods=['POST'])
def route_query():
    data = request.get_json()
    response = query(data.get('query'))

    if response:
        # Converter Markdown para HTML
        html_response = markdown.markdown(response)
        return jsonify({"message": html_response}), 200

    return jsonify({"error": "Something went wrong"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)