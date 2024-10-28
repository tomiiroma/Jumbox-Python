from flask import Flask, render_template, request
from app.models.Sucursal import Sucursal


app = Flask(__name__)


@app.route("/")
def hello_world():
    sucursales = [
            Sucursal(1, "Sucursal Centro", "Buenos Aires", "Capital", "Calle 1", 100, "011-1234-5678"),
            Sucursal(2, "Sucursal Norte", "Buenos Aires", "San Martín", "Calle 2", 200, "011-2345-6789"),
            Sucursal(3, "Sucursal Sur", "Buenos Aires", "Avellaneda", "Calle 3", 300, "011-3456-7890"),
            Sucursal(4, "Sucursal Oeste", "Buenos Aires", "Morón", "Calle 4", 400, "011-4567-8901"),
            Sucursal(5, "Sucursal Este", "Buenos Aires", "La Plata", "Calle 5", 500, "011-5678-9012"),
        ]
    return render_template("index.html", sucursales=sucursales)


    
@app.route("/formulario")
def formulario():
    return render_template('login.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template("success.html")
    

if __name__ == "__main__":
    app.run(debug=True)
