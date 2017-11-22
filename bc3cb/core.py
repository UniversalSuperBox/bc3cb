"""The nuts and bolts of bc3cb"""

import shlex
from . import usercommands
import requests

class basecampbot:

    def __init__(self, logger):
        self.__logger__ = logger

    def commandworker(self, request):
        """Called by the Flask app when a command comes in. Glues together the behavior of bc3cb.

        :param request: The blob of json that Basecamp POSTS to the webapp, parsed into a dictionary
        """

        commandinfo = request
        commandline = shlex.split(commandinfo['command'])
        userfunc_torun = commandline[0]

        self.__logger__.debug(commandinfo)

        try:
            usercommandresponse = self.executeuserfunction(userfunc_torun, commandline, commandinfo)
        except Exception as error:
            # Build our logging string
            user_name = commandinfo['creator']['name']
            user_command = commandinfo['command']
            self.__logger__.error(' '.join(['"', user_name, '"', 'caused:', error.args[0],
                                            'with the command:', user_command]))

            try:
                errordescription = error.args[1]
            except IndexError:
                errordescription = ("Something happened internally. "
                                    "For more information, contact the bot author.")

            # Make response
            finalresponse = " ".join(["<details><summary>Error:", errordescription,
                                      "</summary>", error.args[0], "</details>"])
        else:
            finalresponse = usercommandresponse

        self.respond(finalresponse, commandinfo['callback_url'])

        return True

    def executeuserfunction(self, func, commandline, post_json_blob):
        """Runs the bot user's specified command if it exists"""

        try:
            functiontoexecute = getattr(usercommands, func.lower())
        except AttributeError:
            raise Exception('BC3CBCommandNotFound', 'Command not found. Maybe try "help"?')
        else:
            return functiontoexecute(commandline, post_json_blob)

    def respond(self, response, callback_url):
        """POSTs our response back to Basecamp.

        :param response: Basecamp-HTML formatted string to send
        :param callback_url: The URL where we should POST
        """

        # Basecamp requires the message to be 'content=stuff'
        requestbody = "".join(["content=", response])

        response_post = requests.post(callback_url, data=requestbody.encode('utf-8'))

        if response_post.status_code == 200:
            result = True
        else:
            result = False

        return result
