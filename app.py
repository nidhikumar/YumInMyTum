from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

with open('json/fastfood.json') as json_file: 
    menu = json.load(json_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-random-dish', methods=['POST'])
def get_random_dish():
    random_restaurant = random.choice(menu)
    random_dish = random.choice(random_restaurant['foodItems'])
    return jsonify(random_dish)

if __name__ == "__main__":
    app.run(debug=True)