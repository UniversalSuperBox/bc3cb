'''
Copyright 2017 Dalton Durst

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import logging
from logging.config import fileConfig
from multiprocessing import Process
import os
import configparser
import bc3cb
from bc3cb import core
from flask import Flask, request, abort

if os.path.isfile('bc3cb.ini'):
    logging.config.fileConfig('bc3cb.ini', disable_existing_loggers=False)
    logger = logging.getLogger('bc3cbCore')

MY_BOT = bc3cb.core.basecampbot(logger)

RECEIVER = Flask(__name__)

@RECEIVER.route('/')
def index():
    """Helps to test that bc3cb is running"""

    return "You're not supposed to be here!"

@RECEIVER.route('/basecamp3receiver', methods=['POST'])
def call_core():
    """The receiver function that kicks off the rest of bc3cb"""

    if not request.json or not 'command' in request.json:
        abort(400)

    requestdata = request.get_json()

    #TODO: Add multiprocessing back
    # worker = Process(target=MY_BOT.commandworker, args=(requestdata,))
    # worker.start()

    MY_BOT.commandworker(requestdata)

    return "", 204

if __name__ == '__main__':
    RECEIVER.run(debug=False)
