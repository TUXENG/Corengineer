import json
import jsonschema
from jsonschema import validate
from .scheme import *


def load_json(file_path):
    """Carga un archivo JSON desde el disco."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        raise Exception(f"Error loading JSON file: {e}")

def validate_json(schema, data):
    """Valida los datos JSON contra el esquema proporcionado."""
    try:
        validate(instance=data, schema=schema)
        return True, None
    except jsonschema.exceptions.ValidationError as err:
        return False, str(err)

def validate_and_load_json(file_path, schema):
    """Valida y carga datos JSON, retorna datos si válidos, o error si no lo son."""
    data = load_json(file_path)
    is_valid, error_message = validate_json(schema, data)
    if not is_valid:
        return None, error_message
    return data, None

def validate_course_json(file_path):
    """Valida el archivo JSON de cursos."""
    return validate_and_load_json(file_path, course_scheme)

def validate_service_json(file_path):
    """Valida el archivo JSON de servicios."""
    return validate_and_load_json(file_path, service_scheme)

def validate_profile_json(file_path):
    """Valida el archivo JSON de perfiles."""
    return validate_and_load_json(file_path, profile_scheme)
