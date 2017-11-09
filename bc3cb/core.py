"""The nuts and bolts of bc3cb"""

import json
import os
import shlex
from . import usercommands
from . import log
from . import respond

def commandworker(request):
    """Called by the Flask app when a command comes in. Glues together the behavior of bc3cb.
    
    :param request: The blob of json that Basecamp POSTS to the webapp, parsed into a dictionary"""
    
    commandinfo = request
    commandline = shlex.split(commandinfo['command'])
    userfunc_torun = commandline[0]
    
    log.logger.debug(commandinfo)
    
    try:
        usercommandresponse = executeuserfunction(userfunc_torun, commandline, commandinfo)
    except Exception as error:
        # Build our logging string
        user_name = commandinfo['creator']['name']
        user_command = commandinfo['command']
        log.logger.error(' '.join(['"', user_name, '"', 'caused:', error.args[0], 'with the command:', user_command]))
        
        try:
            errordescription = error.args[1]
        except IndexError as indexerror:
            errordescription = "Something happened internally. For more information, contact the bot author."
    
        # Make response
        finalresponse = " ".join(["<details><summary>Error:", errordescription, "</summary>", error.args[0], "</details>"])
    else:
        finalresponse = usercommandresponse
    
    respond.respond(finalresponse, commandinfo['callback_url'])
    
    return True
    
def executeuserfunction(func, commandline, post_json_blob):
    """Runs the bot user's specified command if it exists"""
    try:
        functiontoexecute = getattr(usercommands, func.lower())
    except AttributeError:
        raise Exception('BC3CBCommandNotFound', 'Command not found. Maybe try "help"?')
    else:
        return functiontoexecute(commandline, post_json_blob)
    

