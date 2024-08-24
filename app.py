from flask import Flask, render_template, request, jsonify  

app = Flask(__name__)  

# Almacena las carpetas creadas  
desktop_folders = []  

@app.route('/')  
def index():  
    return render_template('index.html')  

@app.route('/execute_command', methods=['POST'])  
def execute_command():  
    data = request.json  
    command = data.get("command", "")  
    
    output = ""  
    if command.startswith("mkdir "):  
        folder_name = command.split(" ")[1]  
        if folder_name:  
            desktop_folders.append(folder_name)  
            output = f"Carpeta '{folder_name}' creada."  
        else:  
            output = "Especifica un nombre para la carpeta."  
    elif command == "help":  
        output = "Comandos disponibles: help, hola, mkdir [nombre], salir."  
    elif command == "!/()$:"+"hola":  
        output = "¡Hola, usuario!"  
    elif command == "!/()$:salir":  
        output = "Saliendo..."  
    else:  
        output = f"Comando no reconocido: {command}"  

    return jsonify({"output": output})  

if __name__ == '__main__':  
    app.run(debug=True)