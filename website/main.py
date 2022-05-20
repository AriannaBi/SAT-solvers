from flask import Flask, render_template, request, jsonify
from solver import solve
import pandas as pd

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
