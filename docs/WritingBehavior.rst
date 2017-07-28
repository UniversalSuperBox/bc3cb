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

    def ping(commDict, json):
        """
        Usage: !bot ping
        Returns 'pong'.
        """
        
        return 'pong'
    
When someone says `!bot ping` or directly messages the bot saying `ping`, the bot replies with `pong`.

Easy. Just like you've always wanted.


Creating Behavior
-----------------



Returning Errors
----------------

Sometimes things go wrong in your code. Sometimes the user requests something impossible. In this case, you should return one of the following error strings and bc3cb will respond to the user accordingly.

bc3cb will also try to catch exceptions raised by your code and log them to stdout without crashing completely. It will respond to the user asking them to 'contact the bot author for more information'.

Some Notes
----------

* You can't call anything within bc3cb from your commands as `core.py` imports `usercommands.py` and most of bc3cb imports `core.py`. Attempting to import anything from bc3cb would cause a circular dependency and will make you very sad.
