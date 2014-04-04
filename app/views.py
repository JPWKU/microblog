from flask import render_template
from app import app 


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'JP' }
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in BG!'
        },
        {
            'author':{ 'nickname': 'Susan' },
            'body': 'The movie was good!'
        }
    ]

    return render_template("index.html",
        title = 'Home',
        posts = posts,
        user = user)

