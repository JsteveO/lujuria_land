from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import time
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

credenciales_json = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(credenciales_json, scope)
#creds = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scope)
client = gspread.authorize(creds)

sheet = client.open("data_lujuria").sheet1

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    nombre = request.form["nombre"]
    genero = request.form["genero"]
    whatsapp = request.form["whatsapp"]
    edad = request.form["edad"]

    foto = request.files["foto"]

    filename = ""

    if foto and foto.filename != "":
        nombre_archivo = nombre.lower().replace(" ", "_")
        filename = f"{nombre_archivo}{whatsapp}.jpg"
        ruta = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        foto.save(ruta)

        limpiar_uploads(app.config["UPLOAD_FOLDER"], limite=10)

        foto = f"uploads/{filename}"
    else:
        foto = "images/todos.jpeg"

    with open("registros.txt", "a", encoding="utf-8") as f:
        f.write(f"{nombre},{genero},{whatsapp},{edad},{filename}\n")

    try:
        sheet.append_row([
            nombre,
            genero,
            whatsapp,
            edad,
            foto,
            time.strftime("%Y-%m-%d %H:%M:%S")
        ])
    except Exception as e:
        print("Error guardando en Sheets:", e)

    return redirect(url_for("pase", nombre=nombre, edad=edad, foto=foto, genero=genero))


@app.route("/pase")
def pase():

    nombre = request.args.get("nombre")
    edad = request.args.get("edad")
    foto = request.args.get("foto")
    genero = request.args.get("genero")

    return render_template("pase.html", nombre=nombre,edad=edad, foto=foto, genero=genero)




def limpiar_uploads(carpeta, limite=10):
    archivos = [
        os.path.join(carpeta, f)
        for f in os.listdir(carpeta)
        if os.path.isfile(os.path.join(carpeta, f))
    ]

    # Ordenar por fecha de creación (más antiguos primero)
    archivos.sort(key=os.path.getctime)

    # Si hay más del límite → borrar los más viejos
    while len(archivos) > limite:
        archivo_a_borrar = archivos.pop(0)
        os.remove(archivo_a_borrar)

@app.route("/descargar")
def descargar():
    return send_file("registros.txt", as_attachment=True)

@app.route("/search")
def search():
    nombre = request.args.get("Nombre")
    whatsapp = request.args.get("telefono")

    if not nombre and not whatsapp:
        return render_template("search.html", resultados=None)

    try:
        datos = sheet.get_all_records()  # trae todo como lista de diccionarios
        
        resultados = []

        for fila in datos:
            if nombre and nombre.lower() in fila["Nombre"].lower():
                resultados.append(fila)
            elif whatsapp and str(fila["telefono"]) == whatsapp:
                resultados.append(fila)

        return render_template("search.html", resultados=resultados)

    except Exception as e:
        return {"error": str(e)}


'''if __name__ == "__main__":
    app.run(debug=True)'''
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)