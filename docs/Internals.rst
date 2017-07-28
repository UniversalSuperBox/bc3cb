Internals
*********

Core
----

Core is the 

Internal Errors
---------------

Check out :ref:`writing-behavior` to learn about returning errors from your behavior.

Internal errors are thrown back and forth inside of bc3cb. While it's valid for the bot creator to return these exceptions, it is not recommended. bc3cb will return different errors depending on the exception.

More will be added when the need arises.

bc3cbCommNotFound
^^^^^^^^^^^^^^^^^

Used when the bot user requests a command that hasn't been defined by the user. For example, they called the bot with `!bot weqyasdrvjklase`, but you don't have a `weqyasdrvjklase` function in `usercommands.py`.
