from flask import Flask
from modelo.Sucursal import Sucursal

app = Flask(__name__)


sucursal = Sucursal(1, "Sucursal Ejemplo", "Buenos Aires", "Capital", "Corrientes", 222, "2222-2222")

@app.route("/")
def hello_world():
    return f"La altura de la sucursal es: {sucursal.get_altura()}"
