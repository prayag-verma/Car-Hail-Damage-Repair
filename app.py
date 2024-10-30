import os
from flask import Flask, render_template, request, jsonify, url_for, redirect, send_from_directory
import cv2
import numpy as np
from utils.image_processing import detect_damage, analyze_damage
from utils.force_calculation import calculate_force, get_device_adjustment
from utils.database import init_db, insert_result, get_all_results

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            image = cv2.imread(filename)
            damage_probability = detect_damage(image)
            damage_area = analyze_damage(image)
            force = calculate_force(damage_area)
            adjustment = get_device_adjustment(force)

            insert_result(file.filename, float(damage_probability), float(damage_area), float(force), adjustment)

            return jsonify({
                'damage_detected': True,
                'damage_probability': float(damage_probability),
                'calculated_force': float(force),
                'device_adjustment': adjustment,
                'image_url': url_for('uploaded_file', filename=file.filename)
            })
    return render_template('index.html')


@app.route('/results')
def results():
    all_results = get_all_results()
    return render_template('results.html', results=all_results)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)