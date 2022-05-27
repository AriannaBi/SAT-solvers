import inspect
import os
import sys

from flask import Flask, render_template, request, jsonify
import pandas as pd

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from solver import solve

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        df = pd.DataFrame(request.json, columns=['cloth', 'color'])
        result = solve(df)

        if result:
            return jsonify('Your outfit is okay!')
        else:
            return jsonify("Your outfit isn't okay!")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
