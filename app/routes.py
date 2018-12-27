from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Hossein'}
    return '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hossein</title>
    </head>
    <body>
        <h1> Hello, ''' + user['name'] + '''</h1>
       </body>'''
