from flask import Flask, render_template, jsonify, request
from forms import LuckyForm
from random import randint
import requests
from helpers import check_for_errors, get_data, make_response

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
app.config["SECRET_KEY"] = "abc123"

# Numbers API
BASE_URL = 'http://numbersapi.com'


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route('/api/get-lucky-num', methods=['POST'])
def get_lucky_num():
    """ Gets lucky num and date info, returns """
    data = get_data()

    # Return errors if invalid data received
    form = LuckyForm(data=data)
    if not form.validate():
        return jsonify(errors=form.errors)

    # Generate response
    lucky_num = randint(0, 100)
    num_response = requests.get(f'{BASE_URL}/{lucky_num}')
    year_response = requests.get(f"{BASE_URL}/{data['year']}/year")

    response = make_response(num_response, year_response, lucky_num, data)
    return jsonify(response)
