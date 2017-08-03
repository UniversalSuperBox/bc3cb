.. _writing-behavior:

Writing Behavior
****************

The Bot Creator defines the behavior for all commands that users can run in usercommands.py. 

Introduction
------------

Creating new behavior:

#. Think about what word you want the user to call to invoke the behavior
#. Define a function with that word as its name. From that function, return whatever you want to reply to the user with. bc3cb will handle the rest.

Consider the default `ping` command::

    def ping(commandline, commandinfo):
        """
        Usage: !bot ping
        Returns 'pong'.
        """
        
        return 'pong'
    
When someone says ``!bot ping`` or directly messages the bot saying ping, the bot replies with pong.

Easy. Just like you've always wanted.


Writing your First Command
--------------------------

Replying Before Returning
-------------------------

bc3cb passes Basecamp's "Callback URL" to you as part of commandinfo. You can also import bc3cb.respond in your behavior. Together, this means that you can send a response to your caller before your command has completed.

For example, you can tell them that you're processing their long-running request::

    def reallylongcommand(commandline, commandinfo):
        from . import respond
        
        interimresponse = ' '.join(["I'm working on it!"])
        respond.respond(interimresponse, commandinfo['callback_url'])
        
        # Do some more stuff that'll take a while
        
        return "All done!"

The important lines are these::

    from . import respond
    respond.respond(string, commandinfo['callback_url'])


Raising Errors
--------------



Some Notes
----------

* You can't call anything within bc3cb from your commands as `core.py` imports `usercommands.py`.
