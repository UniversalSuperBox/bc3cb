import flask
from flask import Flask
from flask import request
from flask import abort
import multiprocessing
from multiprocessing import Process
from . import core

receiver = Flask(__name__)

@receiver.route('/')
def index():
    return "You're not supposed to be here!"

@receiver.route('/basecamp3receiver', methods=['POST'])
def call_core():
    if not request.json or not 'command' in request.json:
        abort(400)
        
    requestdata = request.get_json()
    
    worker = Process(target=core.commandworker, args=(requestdata,))
    worker.start()
    
    return "", 204
