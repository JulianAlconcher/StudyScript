import sys
import os
import json
import subprocess

# Ruta al archivo donde se guardarán las rutas de cada materia
config_path = "C://Users//julia//Documents//studyfilesbot//materias_config.json"

# Ruta de Chrome (ajusta si es necesario)
chrome_path = "C://Program Files//Google//Chrome//Application//chrome.exe"

# URLs que se abrirán siempre
moodle_url = "https://moodle.uns.edu.ar/moodle/my/"
chatgpt_url = "https://chat.openai.com/"  # Asegúrate de que esta URL sea correcta

# Cargar o crear el archivo de configuración
if os.path.exists(config_path):
    with open(config_path, "r") as file:
        materias_config = json.load(file)
else:
    materias_config = {}

# Obtener la materia desde el argumento
if len(sys.argv) > 1:
    materia = sys.argv[1].strip().lower()
else:
    print("Por favor, especifica la materia. Ejemplo: study 'pss'")
    sys.exit()

if materia in materias_config:
    archivos = materias_config[materia]
    docs_files = [moodle_url, chatgpt_url]  # Incluye Moodle y ChatGPT en docs_files
    other_files = []

    # Clasifica los archivos en docs_files y other_files
    for archivo in archivos:
        if "docs.google.com" in archivo:
            docs_files.append(archivo)
        else:
            other_files.append(archivo)

    # Abre los archivos de Google Docs, Moodle y ChatGPT en una ventana de Chrome a la derecha
    subprocess.Popen([chrome_path, "--new-window", "--window-position=800,0"] + docs_files)

    # Abre el resto de los archivos en una sola instancia de Chrome a la izquierda
    if other_files:
        other_files_urls = [
            f"file:///{archivo.replace(' ', '%20')}" if not archivo.startswith("http") else archivo
            for archivo in other_files
        ]
        subprocess.Popen([chrome_path, "--new-window", "--window-position=0,0"] + other_files_urls)
else:
    print(f"No se encontraron archivos para '{materia}'.")
    print("Por favor, ingresa los archivos separados por coma (puede ser ruta local o URL):")
    archivos_input = input().split(",")
    archivos = [archivo.strip() for archivo in archivos_input]

    # Guardar la configuración para la próxima vez
    materias_config[materia] = archivos
    with open(config_path, "w") as file:
        json.dump(materias_config, file)

    # Clasificar y abrir los archivos ingresados en ventanas separadas
    docs_files = [moodle_url, chatgpt_url] + [archivo for archivo in archivos if "docs.google.com" in archivo]
    other_files = [archivo for archivo in archivos if "docs.google.com" not in archivo]

    subprocess.Popen([chrome_path, "--new-window", "--window-position=800,0"] + docs_files)

    if other_files:
        other_files_urls = [
            f"file:///{archivo.replace(' ', '%20')}" if not archivo.startswith("http") else archivo
            for archivo in other_files
        ]
        subprocess.Popen([chrome_path, "--new-window", "--window-position=0,0"] + other_files_urls)
