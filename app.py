from flask import Flask, render_template, request, redirect, url_for
import os
import time

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


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
    else:
        filename = "default.png"

    with open("registros.txt", "a", encoding="utf-8") as f:
        f.write(f"{nombre},{genero},{whatsapp},{edad},{filename}\n")

    return redirect(url_for("pase", nombre=nombre, edad=edad, foto=filename))


@app.route("/pase")
def pase():

    nombre = request.args.get("nombre")
    edad = request.args.get("edad")
    foto = request.args.get("foto")

    return render_template("pase.html", nombre=nombre,edad=edad, foto=foto)


if __name__ == "__main__":
    app.run(debug=True)