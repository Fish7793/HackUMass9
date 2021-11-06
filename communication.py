from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('com_test.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    # send(msg, broadcast = True)

@socketio.on('my_event')
def handle_event(arg):
    print("event: ", arg)

if __name__ == '__main__':
    socketio.run(app)

