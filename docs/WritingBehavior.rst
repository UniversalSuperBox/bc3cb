.. _writing-behavior:

Writing Behavior
****************

The Bot Creator defines the behavior for all commands that users can run in ``usercommands.py``. 

Introduction
------------

Creating new behavior consists of two easy steps:

#. Think about what word you want the user to call to invoke the behavior
#. Define a function with that word as its name. From that function, return whatever you want to reply to the user with. bc3cb will handle the rest.

Easy. Just like you've always wanted.


Writing your First Command
--------------------------

Consider the default `ping` command::

    # bc3cb/usercommands.py
    
    def ping(commandline, commandinfo):
        """
        Returns 'pong'.
        """
        
        return 'pong'
    
In Basecamp, when someone says '!bot ping' or directly messages the bot saying 'ping', the bot replies with 'pong'.

We're going to create a simple command that performs a dice roll.

Every command starts with your function header::

    # bc3cb/usercommands.py

    def diceroll(commandline, commandinfo):
        # statements go here!

Just like that, you've created a new command. If a user calls your bot by saying '!botname diceroll', it will be executed.

Note that all of your functions must take exactly two arguments. It is recommended to call them commandline and commandinfo, just like the example above. commandline and commandinfo will be discussed later on this page.

Now, let's add some code that generates a random number between 1 and 6.::

    # bc3cb/usercommands.py

    def diceroll(commandline, commandinfo):
        import random

        return random.randint(1, 6)

This will reply to the user with a random number between 1 and 6.

Notice that the ``import`` statement is inside of the function rather than at the top of the file. This is called lazy importing and is used because every invocation of the bot is started in a new process. Importing *everything* that *any* of your commands may require every time your bot is invoked is wasteful, whereas lazy importing takes less time.

What is 'commandline'?
----------------------

``commandline`` is always sent as the first argument of your functions. It is the message that the user sent to your bot, split into a token list using `shlex <https://docs.python.org/3.5/library/shlex.html>`_.

For example, if the user sends "this is a command", commandline will be the following list::

    ['this', 'is', 'a', 'command']

This gets more exciting, of course. Shlex also allows the use of quoted strings. The user may send "this is 'a command'" and you will see::

    ['this', 'is', 'a command']

This allows you to create command line-like syntaxes for your bot.

What is 'commandinfo'?
----------------------

``commandinfo`` is always sent as the second argument of your functions. It is a dictionary that represents the JSON payload sent by Basecamp. This includes important information such as the user's name and title. You can read more about this JSON payload on the `Basecamp 3 API Chatbots page <https://github.com/basecamp/bc3-api/blob/master/sections/chatbots.md>`_.

Raising Exceptions
------------------

bc3cb tries its hardest to always reply to the user that invokes it. This includes a statement that catches any exception and replies with an error message.

You can throw any type of exception you would like, including the base Exception::

    # bc3cb/usercommands.py

    def neverworks(commandline, commandinfo):
        raise Exception('ShortDescriptiveName', 'Long error message that will show as the summary of the error')

This will be caught by bc3cb. It will then send a message to the user saying "Long error message that will show as the summary of the error". The ShortDescriptiveName will be found by clicking to expand the message. It will also be logged to stdout as the following::

    bc3cbCore - ERROR - "Basecamp User Name" caused: ShortDescriptiveName with the command: [user message to bot]

Consider making the ShortDescriptiveName field different every time you write an exception. This will aid you in debugging.

Replying Before Returning
-------------------------

bc3cb passes Basecamp's "Callback URL" to you as part of commandinfo. This is the URL that you can use to create a new message with an HTTP POST. You can also import bc3cb.respond in your behavior, which handles the POST for you. Together, this means that you can easily send a response to the user before your command has completed.

For example, you can tell them that you're processing their long-running request::

    def reallylongcommand(commandline, commandinfo):
        from . import respond
        
        interimresponse = "I'm working on it!"
        respond.respond(interimresponse, commandinfo['callback_url'])
        
        # Do some more stuff that'll take a while
        
        return "All done!"

The important lines are these::

    from . import respond
    respond.respond(string, commandinfo['callback_url'])

Some Notes
----------

* You can't call anything within bc3cb.core from your commands as `core.py` imports `usercommands.py`.
