import json
import jsonschema
from jsonschema import validate
from scheme import course_scheme, service_scheme, profile_scheme

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_json(schema, data):
    try:
        validate(instance=data, schema=schema)
        print(f"Validation succeeded for {schema['title']}")
    except jsonschema.exceptions.ValidationError as err:
        print(f"Validation error for {schema['title']}: {err.message}")

def main():
    # Validar cursos
    course_data = load_json('course_card.json')
    validate_json(course_scheme, course_data)

    # Validar servicios
    service_data = load_json('service_card.json')
    validate_json(service_scheme, service_data)

    # Validar perfil
    profile_data = load_json('profile_card.json')
    validate_json(profile_scheme, profile_data)

if __name__ == '__main__':
    main()
