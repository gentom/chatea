#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def render():
    return render_template('./chatty.html')

@socketio.on('message')
def handle_msg(msg):
    print('Message: '+ msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)