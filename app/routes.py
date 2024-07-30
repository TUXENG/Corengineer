import json
import os
from flask import current_app as app
from flask import render_template



@app.route('/')
def home():
    json_path = os.path.join(app.root_path, 'static/json', 'index_cards.json' )

    with open(json_path, 'r', encoding='utf-8') as f:
        cards =json.load(f)

    return render_template('index.html', cards=cards)


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')