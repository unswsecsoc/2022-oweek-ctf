from flask import request, render_template, send_from_directory, make_response
from app import app

COOKIE_KEY = '2fa'
COOKIE_VALUE = 'what\'s 1 + 1'
COOKIE_CORRECT_VALUE = '2'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        resp = make_response(render_template('index.html'))
        resp.set_cookie(COOKIE_KEY, COOKIE_VALUE)
        return resp
    elif request.method == 'POST':
        if request.form.get('password') == 'omNoMnOmNOM123':
            if request.cookies.get(COOKIE_KEY) == COOKIE_CORRECT_VALUE:
                resp = make_response(render_template('flag.html'))
            else:
                resp = make_response(render_template('index.html', error='Access Denied: missing 2fa method'))
                resp.set_cookie(COOKIE_KEY, COOKIE_VALUE)
        else:
            resp = make_response(render_template('index.html', error='Access Denied: incorrect password'))
            resp.set_cookie(COOKIE_KEY, COOKIE_VALUE)

        return resp

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
