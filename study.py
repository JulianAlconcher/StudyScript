import sys
import os
import json
import subprocess

config_path = "C://Users//julia//Documents//studyfilesbot//materias_config.json"
chrome_path = "C://Program Files//Google//Chrome//Application//chrome.exe"
moodle_url = "https://moodle.uns.edu.ar/moodle/my/"
chatgpt_url = "https://chat.openai.com/" 

if os.path.exists(config_path):
    with open(config_path, "r") as file:
        materias_config = json.load(file)
else:
    materias_config = {}
    
def mostrar_ayuda():
    """Displays available commands and how to use them."""
    print("\nStudy Script Help")
    print("-" * 50)
    print("Usage:")
    print("  study <subject>           Opens the files associated with the subject.")
    print("  study list                Lists all available subjects.")
    print("  study <subject> files     Displays files associated with a subject.")
    print("  study <subject> add       Adds a new file to the specified subject.")
    print("  study help                Shows this help message.")
    print("\nExamples:")
    print("  study 'pss'               Opens all files for 'pss'.")
    print("  study list                Shows all registered subjects.")
    print("  study 'pss' files         Lists all files associated with 'pss' and allows modification.")
    print("  study 'pss' add           Prompts to add a new file or URL for 'pss'.")
    print("-" * 50)

def listar_materias():
    """Lists all available subjects in the configuration file."""
    if materias_config:
        print("Available subjects:")
        for materia in materias_config.keys():
            print(f"- {materia}")
    else:
        print("No subjects registered.")

def abrir_materia(materia):
    """Opens the files and links associated with a specific subject in the browser."""
    if materia in materias_config:
        archivos = materias_config[materia]
        docs_files = [moodle_url, chatgpt_url]
        other_files = []

        for archivo in archivos:
            if "docs.google.com" in archivo:
                docs_files.append(archivo)
            else:
                other_files.append(archivo)

        subprocess.Popen([chrome_path, "--new-window", "--window-position=800,0"] + docs_files)

        if other_files:
            other_files_urls = [
                f"file:///{archivo.replace(' ', '%20')}" if not archivo.startswith("http") else archivo
                for archivo in other_files
            ]
            subprocess.Popen([chrome_path, "--new-window", "--window-position=0,0"] + other_files_urls)
    else:
        print(f"No files found for '{materia}'.")
        print("Please enter the files separated by commas (can be local path or URL):")
        try:
            archivos_input = input().split(",")
            archivos = [archivo.strip() for archivo in archivos_input]

            materias_config[materia] = archivos
            with open(config_path, "w") as file:
                json.dump(materias_config, file)

            docs_files = [moodle_url, chatgpt_url] + [archivo for archivo in archivos if "docs.google.com" in archivo]
            other_files = [archivo for archivo in archivos if "docs.google.com" not in archivo]

            subprocess.Popen([chrome_path, "--new-window", "--window-position=800,0"] + docs_files)

            if other_files:
                other_files_urls = [
                    f"file:///{archivo.replace(' ', '%20')}" if not archivo.startswith("http") else archivo
                    for archivo in other_files
                ]
                subprocess.Popen([chrome_path, "--new-window", "--window-position=0,0"] + other_files_urls)
        except KeyboardInterrupt:
            print("\nOperation canceled. Exiting...")

def mostrar_archivos_materia(materia):
    """Displays the files and links associated with a subject in the console, allowing them to be modified or deleted."""
    if materia in materias_config:
        print(f"Files associated with the subject '{materia}':")
        print("")
        print(f"{'Number':<6} | {'FileType':<15} | {'File':<50}")
        print("-" * 76)

        for index, archivo in enumerate(materias_config[materia], start=1):
            tipo_archivo = "URL" if archivo.startswith("http://") or archivo.startswith("https://") else "Local File"
            
            if "docs" not in archivo:
                archivo_nombre = os.path.basename(archivo) 
            else:
                if len(archivo) > 50:  
                    archivo_nombre = f"{archivo[:24]}...{archivo[-22:]}" 
                else:
                    archivo_nombre = archivo 
            
            print(f"{index:<6} | {tipo_archivo:<15} | {archivo_nombre:<50}")
        
        print("\n" + "-" * 76)  
        print("Select the number of the file you want to modify or delete (or type 'add' to add a new file, or 'exit' to quit):")
        
        try:
            seleccion = input().strip()
        except KeyboardInterrupt:
            print("\nOperation canceled. Exiting...")
            return  

        if seleccion.lower() == 'exit':
            return
        elif seleccion.lower() == 'add':
            nuevo_archivo = input("Enter the new file or URL to add: ").strip()
            materias_config[materia].append(nuevo_archivo)

            with open(config_path, "w") as file:
                json.dump(materias_config, file)

            print(f"File successfully added to '{materia}': {nuevo_archivo}")
            return

        try:
            seleccion_index = int(seleccion) - 1  
            if 0 <= seleccion_index < len(materias_config[materia]):
                print("Choose an option:")
                print("1. Modify the file")
                print("2. Delete the file")
                try:
                    opcion = input("Enter 1 or 2: ").strip()
                except KeyboardInterrupt:
                    print("\nOperation canceled. Exiting...")
                    return  

                if opcion == '1':
                    nuevo_archivo = input("Enter the new file or URL: ").strip()
                    materias_config[materia][seleccion_index] = nuevo_archivo  

                    with open(config_path, "w") as file:
                        json.dump(materias_config, file)

                    print(f"File successfully modified: {nuevo_archivo}")
                elif opcion == '2':
                    confirmado = input(f"Are you sure you want to delete '{materias_config[materia][seleccion_index]}'? (yes/no): ").strip().lower()
                    if confirmado in ['yes', 'y']:
                        eliminado = materias_config[materia].pop(seleccion_index) 

                        with open(config_path, "w") as file:
                            json.dump(materias_config, file)

                        print(f"File successfully deleted: {eliminado}")
                    else:
                        print("Delete operation canceled.")
                else:
                    print("Invalid option. Please enter 1 or 2.")
            else:
                print("Invalid selection. Please select a valid number.")
        except ValueError:
            print("Invalid input. You must enter a number.")
    else:
        print(f"No files found for '{materia}'.")

def agregar_archivo_materia(materia):
    """Adds a file to the specified subject."""
    if materia in materias_config:
        try:
            nuevo_archivo = input("Enter the file or URL to add: ").strip()
            materias_config[materia].append(nuevo_archivo)

            with open(config_path, "w") as file:
                json.dump(materias_config, file)

            print(f"File successfully added to '{materia}': {nuevo_archivo}")
        except KeyboardInterrupt:
            print("\nOperation canceled. Exiting...")
    else:
        print(f"No subject found for '{materia}'. Please add the subject first.")

def agregar_carpeta_materia(materia, folder_path):
    """Adds all files in a folder to the specified subject."""
    if not os.path.isdir(folder_path):
        print("The specified path is not a valid folder.")
        return
    
    archivos_en_carpeta = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if materia not in materias_config:
        materias_config[materia] = []
    
    materias_config[materia].extend(archivos_en_carpeta)

    with open(config_path, "w") as file:
        json.dump(materias_config, file)
    
    print(f"Files from '{folder_path}' successfully added to '{materia}'.")
    sys.exit(0)  # Stop execution after adding the folder

if len(sys.argv) > 1:
    command = sys.argv[1].strip().lower()
    
    if command == "help":
        mostrar_ayuda()
    
    elif command == "list":
        listar_materias()
    
    elif len(sys.argv) > 2 and sys.argv[2].strip().lower() == "files":
        materia = command
        mostrar_archivos_materia(materia)

    elif len(sys.argv) > 2 and sys.argv[2].strip().lower() == "add" and len(sys.argv) > 3 and sys.argv[3].strip().lower() == "-f":
            # Add folder to the subject
            materia = command
            try:
                folder_path = input("Enter the full path of the folder: ").strip()
                agregar_carpeta_materia(materia, folder_path)
            except KeyboardInterrupt:
                print("\nFinishing process")
                sys.exit(0)

    else:
        abrir_materia(command)
else:
    print("Please specify the subject. Example: study 'pss', 'study list' to see all subjects or 'study help' for a list of commands.")