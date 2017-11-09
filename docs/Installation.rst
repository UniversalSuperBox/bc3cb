Installation
************

I used Ubuntu 16.04 to install bc3cb for the first time. It'll probably work with any other OS.

Requirements
------------

1. A URL for BC3CB. Basecamp will call the bot at this URL. It must be HTTPS.
2. Admin rights on your Basecamp 3 account
3. A server with pip and virtualenv installed

Procedure
---------

#. Create a new user for bc3cb. Its password can be anything, we'll be disabling remote login anyway. ``adduser bc3cb``
#. Remove the new user's login rights by editing /etc/passwd and switching the login shell to one that doesn't allow login.
#. Switch to the user with ``su -s /bin/bash bc3cb``
#. Create a virtualenv named bc3cbEnv in its home folder ``python3 -m virtualenv ~/bc3cbEnv``
#. Enter the virtualenv to install software ``. ~/bc3cbEnv/bin/activate``
#. Install the required packages to run bc3cb ``pip install flask requests``
#. Set up a reverse proxy to ``[hostname]:5000/basecamp3receiver``. It doesn't matter how you do it or with what software, it just needs to provide a valid HTTPS session (that means you need a valid TLS certificate). I set up nginx to proxy the URL to /receive
#. Set up Basecamp

    #. Open a project on Basecamp and select "Settings" in the upper right corner. 
    #. Select "Chatbots"
    #. Pick "Add a new chatbot"
    #. Give your bot a fun name and set its command URL to your proxy URL

Now all you'll need to do is run ``run.py`` and your bot will be ready to rock!.

TODO: Setting up nginx for reverse proxying
TODO: Automatic start

Good proxy configuration, if you have a proxy in front::

    server {
        listen 80
        server_name [DOMAIN]
        root /var/www/default
        location / {
                proxy_pass http://localhost:5000/;
        }
    }
