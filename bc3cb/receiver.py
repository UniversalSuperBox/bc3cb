# Copyright 2017 Dalton Durst
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from threading import Thread
import bottle
from bottle import request, run

BOT_INSTANCE = None

def __init__(BOT_INSTANCE):
    BOT_INSTANCE = BOT_INSTANCE

@bottle.post('/basecamp3receiver')
def call_core():
    """The receiver function that kicks off the rest of bc3cb"""

    if not request.json:
        return bottle.HTTPResponse(status=400, body="Missing command")

    requestdata = request.json

    bot_thread = Thread(target=BOT_INSTANCE.commandworker, args=(requestdata,))
    bot_thread.start()

    return bottle.HTTPResponse(status=204)