from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "12345"

APP_NAME = "Agenda Semanal"

agenda = {
    "Lunes": [],
    "Martes": [],
    "Miércoles": [],
    "Jueves": [],
    "Viernes": [],
    "Sábado": [],
    "Domingo": []
}

@app.route("/")
def index():
    return render_template("index.html", agenda=agenda, app_name=APP_NAME)

@app.route("/agregar", methods=["POST"])
def agregar():
    dia = request.form["dia"]
    actividad = request.form["actividad"]
    hora = request.form["hora"]

    agenda[dia].append({
        "actividad": actividad,
        "hora": hora
    })

    return redirect("/")

@app.route("/eliminar/<dia>/<int:id>")
def eliminar(dia, id):
    if dia in agenda and 0 <= id < len(agenda[dia]):
        agenda[dia].pop(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)