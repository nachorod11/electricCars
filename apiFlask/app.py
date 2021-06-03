from flask import Flask, jsonify, request
from rutas import rutas
from decouple import config as config_decouple

app = Flask(__name__)
app.config["DEBUG"] = True
enviroment = config['development']
app.config.from_object(enviroment)
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

@app.route('/')
def home():
    return "<h1>Viajar en coche eléctrico.</h1><p>Esta API nos permite obtener posibles rutas para viajar en coche eléctrico.</p>"

@app.route('/api/v1/resources/rutas/all', methods=['GET'])
def get_all():
    return jsonify(rutas)

@app.route('/api/v1/resources/rutas/<id>', methods=['GET'])
def valor_id(id):
    for diccionario in rutas:
        if str(diccionario['id']) == id:
            return jsonify(diccionario)
    return "El elemento no existe"

app.run()