"""Init dentro del main"""
from flask import Blueprint

# Definición del Blueprint 'main'
bp = Blueprint('main', __name__, template_folder='templates')

# Importar las rutas para registrarlas con el Blueprint
from app.main import routes
