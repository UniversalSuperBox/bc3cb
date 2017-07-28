import bc3cb
import shlex
import mock
from mock import patch
from bc3cb import core
from bc3cb import respond
import httpretty
from . import test_data
    
@patch('bc3cb.respond.respond')
def test_coreCommandworker(respond):
    
    bc3cb.core.commandworker(test_data.testdata)
    
    bc3cb.respond.respond.assert_called_with('testargument|testcommand testargument|Test User', 'https://localhost/callback')
    
@patch('bc3cb.respond.respond')
def test_coreCommandworker_notfounderror(respond):
    
    bc3cb.core.commandworker(test_data.testdata_notfound)
    
    bc3cb.respond.respond.assert_called_with('<details><summary>Error: Command not found. Maybe try "help"? </summary> BC3CBCommandNotFound </details>', 'https://localhost/callback')

@httpretty.activate
def test_coreRespond():
    httpretty.register_uri(httpretty.POST, 'https://localhost/callback', body="")
    
    bc3cb.respond.respond("I'm trying it! 🎉🎉", 'https://localhost/callback')
    
    # The response will be encoded when we get it back from httpretty.
    assert httpretty.last_request().body.decode('utf-8') == "content=I'm trying it! 🎉🎉"
    
def test_coreExecuteuserfunction():

    commandinfo = test_data.testdata
    testdata_commandline = shlex.split(commandinfo['command'])

    assert bc3cb.core.executeuserfunction('testcommand', testdata_commandline, commandinfo) == 'testargument|testcommand testargument|Test User'
    
def test_receiverIndex():
    """This is really just a sanity check"""
    from bc3cb import receiver
    assert receiver.index() == "You're not supposed to be here!"

