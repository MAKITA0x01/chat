from flask import Flask, request, abort ,render_template

import os

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/list")
def list():
    return render_template('list.html')

if __name__ == "__main__":
#    app.run(debug = True)
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
