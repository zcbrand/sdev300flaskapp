from flask import Flask, render_template

app = Flask('sdev300flaskapp')


@app.route('/')
def index():
    return render_template('index.html')
