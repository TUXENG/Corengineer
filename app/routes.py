""" Importaciones """
import os
from flask import render_template, redirect, url_for, flash, Blueprint
from app.scripts.validate_scheme import validate_course_json
from app.scripts.validate_scheme import validate_service_json, validate_profile_json

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    """
    Ruta principal de la aplicación.

    Carga y valida los datos de los cursos desde un archivo JSON.
    Si hay un error en la validación, redirige a una página de error.
    De lo contrario, renderiza la página principal con los datos de los cursos.
    """
    courses_path = os.path.join(bp.root_path, 'data/json/course_card.json')
    courses, error_course = validate_course_json(courses_path)
    if error_course:
        flash(f"Error validating courses JSON: {error_course}", 'error')
        return redirect(url_for('main.error'))
    return render_template('index.html', courses=courses['courses'])

@bp.route('/services')
def services():
    """
    Ruta para la página de servicios.

    Carga y valida los datos de los servicios y perfiles desde archivos JSON.
    Si hay un error en la validación de cualquiera de los archivos, muestra un mensaje de error y redirige a la página de error.
    De lo contrario, renderiza la página de servicios con los datos validados.
    """
    services_path = os.path.join(bp.root_path, 'data/json/services_card.json')
    profile_path = os.path.join(bp.root_path, 'data/json/profile_card.json')
    
    offerings, error_services = validate_service_json(services_path)
    profiles, error_profiles = validate_profile_json(profile_path)

    if error_services:
        flash(f"Error validating services JSON: {error_services}", 'error')
        return redirect(url_for('main.error'))
    if error_profiles:
        flash(f"Error validating profiles JSON: {error_profiles}", 'error')

    return render_template('services.html', services=offerings['services'], profiles=profiles['profiles'])

@bp.route('/portfolio')
def portfolio():
    """
    Ruta para la página del portafolio.

    Renderiza la página del portafolio que muestra los proyectos realizados.
    """
    return render_template('portfolio.html')

@bp.route('/team')
def team():
    """
    Ruta para la página del equipo.

    Renderiza la página del equipo que presenta a los miembros del equipo.
    """
    return render_template('team.html')

@bp.route('/contact')
def contact():
    """
    Ruta para la página de contacto.

    Renderiza la página de contacto donde los usuarios pueden obtener información de contacto.
    """
    return render_template('contact.html')

@bp.route('/about_us')
def about():
    """
    Ruta para la página de 'Sobre Nosotros'.

    Renderiza la página 'Sobre Nosotros' que proporciona información sobre la empresa u organización.
    """
    return render_template('about.html')

@bp.route('/error')
def error():
    """
    Ruta para la página de error.

    Renderiza una página genérica de error cuando ocurre algún problema en la aplicación.
    """
    return render_template('error.html')
