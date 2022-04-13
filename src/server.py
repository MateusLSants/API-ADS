from flask import Flask, request, json
from schema.schema import *


app = Flask(__name__)


@app.route('/adduser', methods=['POST'])
def add_user():

    body_usuario = request.get_json()

    usuario = user(body_usuario["nome"], 
                   body_usuario["email"], 
                   body_usuario["senha"])

    return body_usuario

app.run()