#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def render():
    return render_template('./chatea.html')

def ack():
    print('message was received :D')

@socketio.on('event')
def event_handler(json):
    print('Recived event: '+str(json))
    socketio.emit('response', json, callback=ack)

@socketio.on('new')
def msg_handler(newusr):
    socketio.emit('joined',newusr, callback=ack)

if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True)