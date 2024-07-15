import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def message(data):
    print('message received with ', data)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')
#convert a string to bytes
sio.emit('command', 'dir'.encode())  # Example command

#sio.emit('command', 'dir')  # Example command
#sio.send('dir')  # Example command
sio.wait()
