from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def connected():
    print(request.sid)
    emit("connect",{"data":f"id: {request.sid} is connected"})


if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)