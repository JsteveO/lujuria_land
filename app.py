from flask import Flask, render_template, request, redirect
import os
import re
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
REGISTRO_FILE = "registros.txt"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def limpiar_nombre(nombre):
    nombre = nombre.lower()
    nombre = re.sub(r'\s+', '_', nombre)
    nombre = re.sub(r'[^a-z0-9_]', '', nombre)
    return nombre


@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        genero = request.form.get("genero")
        whatsapp = request.form.get("whatsapp")

        if not whatsapp.isdigit():
            return redirect("/")

        nombre_limpio = limpiar_nombre(nombre)

        foto = request.files.get("foto")
        nombre_imagen = ""

        if foto and foto.filename != "":
            extension = foto.filename.split(".")[-1]
            nombre_imagen = f"{nombre_limpio}{whatsapp}.{extension}"
            path = os.path.join(app.config["UPLOAD_FOLDER"], nombre_imagen)
            foto.save(path)

        registro = f"{nombre},{genero},{whatsapp},{nombre_imagen}\n"

        with open(REGISTRO_FILE,"a",encoding="utf-8") as f:
            f.write(registro)

        return redirect("/")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)