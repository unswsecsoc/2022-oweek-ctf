from flask import request, render_template, send_from_directory
from app import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
