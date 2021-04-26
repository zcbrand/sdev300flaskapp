from flask import Flask, render_template

app = Flask('sdev300flaskapp',
            template_folder='templates')


@app.route('/')
def index():
    return render_template('home.html')

