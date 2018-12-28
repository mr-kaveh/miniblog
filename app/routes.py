from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Hossein'}
    posts = [
        {
            'author': 'johnathan',
            'title': 'learning python'
        },
        {
            'author': 'larry',
            'title': 'learning flask'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
