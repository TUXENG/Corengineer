import json
import os
from flask import current_app as app
from flask import render_template, redirect, url_for, flash
from app.scripts.validate_scheme import validate_course_json, validate_service_json, validate_profile_json


@app.route('/')
def home():
    json_path = os.path.join(app.root_path, 'data/json/course_card.json')
    courses, error = validate_course_json(json_path)
    if error:
        flash(f"Error validating courses JSON: {error}", 'error')
        return redirect(url_for('error'))
    return render_template('index.html', courses=courses['courses'])

@app.route('/services')
def services():
    json_path = os.path.join(app.root_path, 'data/json/services_card.json')
    services, error = validate_service_json(json_path)

    if error:
        flash(f"Error validation services JSON:  {error}", 'error')
        return redirect(url_for('error'))
    return render_template('services.html', services=services['services'])

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

@app.route('/error')
def error():
    return render_template('error.html')