"""
 Author: Zachary Brandenburg
"""

from datetime import datetime
from flask import Flask, render_template, request
from auth.login import valid_login

app = Flask('sdev300flaskapp',
            template_folder='templates')


@app.route('/')
def index(user='User'):
    """Routes to the main page"""
    nav = [
        {'name': 'SlevinLabs', 'url': 'https://www.slevinlabs.com'},
        {'name': 'Google', 'url': 'https://www.google.com'},
        {'name': 'Twitter', 'url': 'https://www.twitter.com'}
    ]

    description = 'SlevinLabs is a leading provider of cutting-edge technologies and services,' \
                  'offering scalable solutions for companies of all sizes. Founded by a group of ' \
                  'friends who started by scribbling their ideas on a piece of paper, today we ' \
                  'offer smart, innovative services to dozens of clients worldwide. We built our ' \
                  'solutions by closely listening to our potential clientele and understanding ' \
                  'their expectations with our product. We know how to analyze this information ' \
                  'and customize our offering to changing market needs. Why not join our fast ' \
                  'growing customer base? Get in touch today to learn more about the SlevinLabs ' \
                  'story.'

    items = [
        'Provide software solutions in an ordered timely manner',
        'Consult teams to align goals with Agile methodologies',
        'Set upt you business for success'
    ]

    time = datetime.now().isoformat(' ')

    return render_template(
        'home.html',
        user=user,
        nav=nav,
        title='SlevinLabs',
        description=description,
        subtitle='WHAT WE DO',
        subsub='Easy. Fast. Secure.',
        items=items,
        time=time
    )


@app.route('/login', methods=['GET', 'POST'])
def register_user():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return index(request.form['username'])
    else:
        return render_template('login.html')
