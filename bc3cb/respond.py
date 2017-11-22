"""This is in a separate file so that bot creators can call the respond function"""

import requests

def respond(response, callback_url):
    """POSTs our response back to Basecamp.

    :param response: Basecamp-HTML formatted string to send
    :param callback_url: The URL where we should POST
    """

    # Basecamp requires the message to be 'content=stuff'
    requestbody = "".join(["content=", response])

    responsePost = requests.post(callback_url, data=requestbody.encode('utf-8'))

    if responsePost.status_code == 200:
        result = True
    else:
        result = False

    return result
