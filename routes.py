from flask import Flask, render_template, request
from app.models.Sucursal import Sucursal


app = Flask(__name__)


@app.route("/",  methods=["GET", "POST"])
def hello_world():
    message = ""
    if request.method == "POST":
        message = "Has iniciado sesión"

    return render_template("index.html", message=message)


    
@app.route("/login")
def formulario():
    return render_template('login.html')

    

if __name__ == "__main__":
    app.run(debug=True)
