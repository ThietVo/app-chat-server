from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

#config database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'appChatDb.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#route
from .views import views
app.register_blueprint(views)

usersConnected = []
@socketio.on('connect')
def connected():
    print(request.sid)
    emit("connect",{"data":f"id: {request.sid} is connected"})


@socketio.on('data')
def joinx(data):
    print("data from the front end: ",str(data))
    emit("data",{'data':data,'id':request.sid},broadcast=True)

@socketio.on('users')
def user(user):
    print("data from the front end: ",str(user))
    if user is not None:
        usersConnected.append(user)

    res_list = []
    for i in range(len(usersConnected)):
        if usersConnected[i] not in usersConnected[i + 1:]:
            res_list.append(usersConnected[i])

    emit("users", res_list,broadcast=True)

@socketio.on('dis_connect')
def disconnect(user):
    print("data from the front end: ",str(user))
    rs = []
    if user is not None:
        for u in usersConnected:
            if u['username'] == user['username']:
                usersConnected.remove(u)
    

    print("user disconnected")
    emit("dis_connect",f"user {request.sid} disconnected",broadcast=True)

# @socketio.on('join')
# def onJoin(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     emit('join',username + ' has entered the room ' + room, room=room)

# @socketio.on('leave')
# def onLeave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     emit('leave',username + ' has left the room.', room=room)