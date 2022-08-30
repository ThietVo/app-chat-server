from src import app, socketio

from flask_cors import CORS
CORS(app)

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)