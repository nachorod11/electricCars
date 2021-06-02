from flask import Flask, jsonify, request
from rutas import rutas


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return "<h1>Viajar en coche eléctrico.</h1><p>Esta API nos permite obtener posibles rutas para viajar en coche eléctrico.</p>"

@app.route('/api/v1/resources/rutas/all', methods=['GET'])
def get_all():
    return jsonify(rutas)

@app.route('/api/v1/resources/rutas/<id>', methods=['GET'])
def get_ruta(id):
    return jsonify(rutas[0])

app.run()