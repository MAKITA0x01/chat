from flask import Flask, request, abort ,render_template

import os
from src import get_info

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('test.html')

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
