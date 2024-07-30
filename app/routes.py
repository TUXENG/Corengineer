from flask import render_template, request, redirect, url_for
from . import app

@app.route('/')
def home():
    return "Hola, Mundo!"
