from flask import Flask, request, abort ,render_template

import os

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug = True)
