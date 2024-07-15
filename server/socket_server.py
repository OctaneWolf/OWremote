from flask import Flask
from flask_socketio import SocketIO, send
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('command')
def handle_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        #send({"output": result.stdout, "error": result.stderr})
        send(str({"output": result.stdout, "error": result.stderr}).encode())
    except Exception as e:
        #send({"error": str(e)})
        send(str({"error": str(e)}).encode())


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
