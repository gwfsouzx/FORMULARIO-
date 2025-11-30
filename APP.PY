from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "chave_secreta_segura"
app.permanent_session_lifetime = timedelta(minutes=30)

usuarios = []

@app.route("/")
def index():
    return redirect(url_for("formulario"))

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        session.permanent = True  
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        novo_usuario = {
            "username": username,
            "email": email,
            "password": password
        }

        usuarios.append(novo_usuario)
        session["usuario"] = novo_usuario

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("formulario"))

    return render_template("formulario.html", usuarios=usuarios)
    
if __name__ == "__main__":
    app.run(debug=True)
