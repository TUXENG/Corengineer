"""init principal"""
import os
import subprocess

from flask import Flask

from config  import Config
from .main.routes import bp as main_bp

def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.

    Este método realiza las siguientes tareas:
    1. Inicializa la aplicación Flask con la configuración definida en `Config`.
    2. Ejecuta un script para generar archivos JSON necesarios si no existen.
    3. Registra los blueprints necesarios, que definen las rutas y vistas de la aplicación.
    4. Devuelve la instancia de la aplicación Flask configurada y lista para ejecutarse.

    Returns:
        Flask: La instancia de la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    script_path = os.path.join(os.path.dirname(__file__), 'scripts', 'generate_json.py')
    subprocess.call(['python', script_path])
    
    with app.app_context():
        app.register_blueprint(main_bp)
        
    return app
