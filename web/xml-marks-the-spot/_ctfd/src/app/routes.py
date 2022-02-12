from flask import request, render_template, send_from_directory
from app import app

@app.route('/', methods=['GET'])
def index():
    location = request.args.get('location')

    if location == 'the secsoc stall opposite red center':
        return 'OWEEK{y@Y_y0u_foUnD_mE}'
    elif location:
        return f'''
        <h1>The flag isn't here :(</h1>
        <form action="/">
            <input type="submit" value="Back" />
        </form>
        '''
    else:
        return render_template('index.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
