from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#função de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

#criação da página(1° rota)
@app.route("/")
def homepage():
    return render_template("index.html")


socketio.run(app, host="192.168.15.47")
