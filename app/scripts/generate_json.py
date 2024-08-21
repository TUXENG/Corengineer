"""
Generador de JSON
"""
import os
import json
import logging

# Configuración del archivo de log
log_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ruta de la carpeta de datos
base_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'json')

# Nombres de los archivos JSON
json_files = [
    'course_card.json',
    'service_card.json',
    'profile_card.json'
]


for json_file in json_files:
    file_path = os.path.join(base_path, json_file)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="utf-8") as f:
            if 'course' in json_file:
                json.dump({"courses": []}, f, indent=4)
            elif 'service' in json_file:
                json.dump({"services": []}, f, indent=4)
            elif 'profile' in json_file:
                json.dump({"profiles": []}, f, indent=4)
        logging.info("Archivo %s creado con contenido vacío.", json_file)

# Confirmar que todos los archivos están presentes
for json_file in json_files:
    file_path = os.path.join(base_path, json_file)
    if os.path.exists(file_path):
        logging.info("Archivo %s ya existe.", json_file)
    else:
        logging.error("Archivo %s no encontrado y no fue creado.", json_file)
