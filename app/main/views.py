from flask import render_template, url_for 
from . import main

@main.route('/')
@main.route('/home/')
def index():
    return render_template('index.html')

@main.route('/blog/')
def blog():
    return render_template('blog.html')

@main.route('/post/')
def post():
    return render_template('post.html')
