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

import logging
from logging.config import fileConfig
import os
import configparser
import bc3cb
from bc3cb import receiver

if os.path.isfile('bc3cb.ini'):
    logging.config.fileConfig('bc3cb.ini', disable_existing_loggers=False)
    logger = logging.getLogger('bc3cbCore')

MY_BOT = bc3cb.basecampbot(logger)

# Add commands here

@MY_BOT.command("testcommand")
def testcommand(commandline, commandinfo):
    """
    Usage: !bot testcommand some stuff

    A command used for testing. Returns some of the info you send, formatted as a string
    """

    try:
        __t = commandline[1]
    except IndexError:
        return 'This command requires at least one argument'
    else:
        return '|'.join([commandline[1], commandinfo['command'], commandinfo['creator']['name']])

@MY_BOT.command("ping")
def ping(commandline, commandinfo):
    """
    Usage: !bot ping
    Returns 'pong'.
    """

    return '<b>pong</b>'

if __name__ == '__main__':
    bc3cb.receiver.BOT_INSTANCE = MY_BOT
    bc3cb.receiver.run(debug=False)
