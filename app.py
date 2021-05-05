"""
 Author: Zachary Brandenburg
"""
import secrets
from datetime import datetime

from flask import Flask, render_template, request, flash, redirect, session

from auth.login import valid_login, user_exists, register_user, complexity

app = Flask('sdev300flaskapp',
            template_folder='templates',
            static_folder='static')
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/')
def index():
    """Landing page HOME"""
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        """Routes to the main page"""
        nav = [
            {'name': 'SlevinLabs', 'url': 'https://www.slevinlabs.com'},
            {'name': 'Register', 'url': '/register'},
            {'name': 'Login', 'url': '/login'}
        ]

        description = '''SlevinLabs is a leading provider of cutting-edge technologies and
                      services, offering scalable solutions for companies of all sizes. Founded
                      by a group of friends who started by scribbling their ideas on a piece of
                      paper, today we offer smart, innovative services to dozens of clients
                      worldwide. We built our solutions by closely listening to our potential
                      clientele and understanding their expectations with our product. We know how
                      to analyze this information and customize our offering to changing market
                      needs. Why not join our fast growing customer base? Get in touch today to
                      learn more about the SlevinLabs story.'''

        items = [
            'Provide software solutions in an ordered timely manner',
            'Consult teams to align goals with Agile methodologies',
            'Set upt you business for success'
        ]

        services = [
            {'service': 'Platinum', 'contents': 'Custom seminar for you\'re entire org',
             'price': 'Contact'},
            {'service': 'Gold', 'contents': 'Private Seminar for team of 15, Silver, Bronze',
             'price': '$10,000'},
            {'service': 'Silver', 'contents': 'Private seminar for one individual, Bronze',
             'price': '$1,000'},
            {'service': 'Bronze', 'contents': 'Access to our video library', 'price': '$100'}
        ]

        time = datetime.now().isoformat(' ')

        return render_template(
            'home.html',
            user=session['username'],
            nav=nav,
            services=services,
            title='SlevinLabs',
            description=description,
            subtitle='WHAT WE DO',
            subsub='Easy. Fast. Secure.',
            items=items,
            time=time
        )


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login Page"""
    if request.method == 'POST':
        if valid_login(request.form.get('username'), request.form.get('password')):
            session['logged_in'] = True
            session['username'] = request.form.get('username')
            return redirect('/')
        else:
            flash('Incorrect Username or Password')
            return redirect('/login')

    if request.method == 'GET':
        return render_template(
            'login.html',
            title='Login'
        )


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Registration Page"""
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'Please enter a Username.'
        elif not request.form['password']:
            error = 'Please enter a Password.'
        elif user_exists(request.form.get('username')):
            error = 'You are already registered'
        elif not complexity(request.form.get('password')):
            error = 'Make your password more complex'

        if error is None:
            register_user(request.form.get('username'), request.form.get('password'))
            flash('You are registered')
            return redirect('/login')
        else:
            flash(error)
            return redirect('/register')
    if request.method == 'GET':
        return render_template(
            'register.html',
            title='Register'
        )
