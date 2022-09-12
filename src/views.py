from flask import request, jsonify, Blueprint
from . import db
from src.models import Messages, Users
from sqlalchemy.sql import func

views = Blueprint('views', __name__)

@views.route('/users/', methods=['POST'])
def createUser():
    data = request.get_json()
    if not data:
        return {
            'error': 'No data provided',
        }
    user = Users(
        username=data['username'],
        password=data['password'],
        created_at=func.now(),
        updated_at=func.now()
    )
    db.session.add(user)
    db.session.commit()
    db.session.flush()
    db.session.refresh(user)

    return {
        "success": "create user succesfully",
        "userAdded": {
            'id': user.id,
            "username": user.username
        }
    }

@views.route('/users/login', methods=['POST'])
def userLogin():
    data = request.get_json()
    if not data:
        return {
            'type': 'error',
            'error': 'No data provided',
        }
    user = Users.query.filter_by(
        username=data['username']
    ).filter_by(
        password=data['password']
    ).first()
    if user is None:
        return {
            'type': 'error',
            'error': 'No such user',
        }
    return {
        'type': 'success',
        'userLogged': {
            'id': user.id,
            'username': user.username
        },
    }

@views.route('/messages/<type>', methods=['GET'])
def getMessages(type):
    messages = db.session.query(
        Messages, Users
        ).join(
            Users
        ).filter(
            Messages.type == type
        ).all() 

    rt = []
    for mess in messages:
        (m, u) = mess
        rt.append({
            'id': m.id,
            'message': m.message,
            'type': m.type,
            'created_at': m.created_at,
            'updated_at': m.updated_at,
            'userId': u.id,
            'username': u.username
        })
    return jsonify(rt)

@views.route('/messages/', methods=['POST'])
def insertMessage():
    data = request.get_json();
    if not data:
        return {
            'type': 'error',
            'error': 'No data provided',
        }
    message = Messages(
        message=data['message'],
        type=data['type'],
        created_at=func.now(),
        updated_at=func.now(),
        userId=data['userId']
    )
    db.session.add(message)
    db.session.commit()
    db.session.flush()
    db.session.refresh(message)

    return {
        "success": "create user succesfully",
        "messageAdded": {
            'id': message.id,
            'message': message.message,
            'created_at': message.created_at,
            'updated_at': message.updated_at,
            "userId": message.userId
        }
    }

@views.route('/messages/<int:id>', methods=['DELETE'])
def deleteMessage(id):
    mess = Messages.query.filter_by(id=id).first_or_404()

    db.session.delete(mess)
    db.session.commit()

    return {
        'success': 'Delete message successfully'
    }