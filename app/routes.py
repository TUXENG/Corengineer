import json
import os
from flask import current_app as app
from flask import render_template



@app.route('/')
def home():
    json_path = os.path.join(app.root_path, 'data/json/cards.json')
    with open(json_path) as f:
        cards = json.load(f)
        
    return render_template('index.html', cards=cards)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about_us')
def about():
    return render_template('about.html')