from flask import Flask, render_template, request
from app.models.Sucursal import Sucursal


app = Flask(__name__)


@app.route("/",  methods=["GET", "POST"])
def hello_world():
        

    sucursales = [
            Sucursal(1, "Sucursal Centro", "Buenos Aires", "Capital", "Calle 1", 100, "011-1234-5678"),
            Sucursal(2, "Sucursal Norte", "Buenos Aires", "San Martín", "Calle 2", 200, "011-2345-6789"),
            Sucursal(3, "Sucursal Sur", "Buenos Aires", "Avellaneda", "Calle 3", 300, "011-3456-7890"),
            Sucursal(4, "Sucursal Oeste", "Buenos Aires", "Morón", "Calle 4", 400, "011-4567-8901"),
            Sucursal(5, "Sucursal Este", "Buenos Aires", "La Plata", "Calle 5", 500, "011-5678-9012"),
        ]
    
    message = ""
    if request.method == "POST":
        message = "Has iniciado sesión"

    return render_template("index.html", sucursales=sucursales, message=message)


    
@app.route("/login")
def formulario():
    return render_template('login.html')

    

if __name__ == "__main__":
    app.run(debug=True)
