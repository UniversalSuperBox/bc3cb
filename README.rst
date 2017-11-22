bc3cb
========

bc3cb makes it easy to create your own chatbot for Basecamp 3.

It provides a low barrier to entry:

#. ``git clone git@github.com:UniversalSuperBox/bc3cb.git``
#. ``pip install bottle requests``
#. Put your behavior in usercommands.py
#. Set up a reverse proxy that provides HTTPS (nginx and Let's Encrypt make it 
   easy)
#. Start ``run.py``
    

Features
--------

- Some Assembly Required: bc3cb doesn't handle HTTPS or proxying. Use what 
  **you** want for that.
- Complete Flexibility: Import whatever. Do whatever. Your mind is the limit 
  to the behavior you can create


Contribute
----------

- Issue Tracker: github.com/UniversalSuperBox/bc3cb/issues

Support
-------

If you experience issues with bc3cb, please visit the issue tracker.

License
-------

The project is licensed under the Apache-2.0 license.


Less brevity below
==================

This will be moved to the documentation in short order.


A super simple framework for Basecamp 3 interactive chat bots, written in Python3.

Getting Set Up
--------------

Setting up the example bot
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create yourself a virtualenv
1. Install `flask requests | pytest mock httpretty` with Pip. Items after the bar (`|`) are only used for testing and may be omitted if you will not be running tests. [TODO: figure out what else]
1. Run run.py with Python

Setting up for developing bc3cb
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create a virtualenv
1. Install `flask requests pytest mock httpretty sphinx sphinx-autobuild` with Pip.
1. Remember to run pytest before you commit!

Goals
-----

bc3cb is meant to be as simple as possible. It handles all these things for you:

* Receiving commands from BC3
* Processing command data into a handy object 
* Passing this object to any function you want

bc3cb has one of its two required batteries included. It provides the API abstraction, you write the behavior for commands.

Architecture
------------

User types in chat: ``!bot do argument1 "argument2 is cool"``

What we do::

    (1) Message Receive
      Flask receives message from Basecamp
      quickly return 200 OK
      kick off separate process (2) with the message from Basecamp
      return to receiving messages
    (2) Process message
      Process the JSON into a keyworded dictionary
      Parse the "Command" field with something like Shlex to ease taking commands
      Note the callback URL
      See what the command is (do)
      If there is something to execute for this command:
        Call the provided function, pass it the JSON dictionary and shlex'd commdand
        Send the data that the function provides back to the Callback URL
      If there is nothing to execute for this command:
        Tell the user to use "Help"
    
As the bot writer, here's what you'll provide:

* The behavior for `do`

The bot framework will check if you have a function set up for `do`. If you do, it'll call that function and pass you everything it knows. Simply return your desired response (in Unicode, of course) and the framework will handle sending it back.

The framework will call your function like this:

`do(commandline, commandinfo)`

Where commandline is a dictionary created by shlex (so you can make your syntax more like a shell program) and commandinfo is the dictionary created by loading the information that Basecamp sends us. More information is available in [TODO]



bc3cb is in no way affiliated with Basecamp, the makers of Basecamp 3. All trademarks used within are property of their respective owners.

Please see the LICENSE file for more license details.
