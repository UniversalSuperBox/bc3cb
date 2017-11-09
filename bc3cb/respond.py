"""This is in a separate file so that bot creators can call the respond function"""

import requests

def respond(response, callback_url):
    """POSTs our response back to Basecamp.
    
    :param response: The message that we should POST. Format it in Basecamp's version of html as described in the chatbot docs.
    :param callback_url: The URL where we should POST
    """
    
    # Basecamp requires the message to be 'content=stuff'
    requestbody = "".join(["content=", response])
    
    r = requests.post(callback_url, data = requestbody.encode('utf-8'))
    
    #TODO: Maybe replace this with a Try: statement?
    if r.status_code == 200:
        result=True
    else:
        result=False
        
    return result
