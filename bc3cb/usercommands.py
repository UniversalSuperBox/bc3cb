"""Bot Creator-defined commands. See docs/usercommands/usercommands.py for more."""

def handle_errors():
    """ TODO: Allow the user to handle their own defined errors"""
    return True
    
def ping(commandline, commandinfo):
    """
    Usage: !bot ping
    Returns 'pong'.
    """
    
    return '<b>pong</b>'
    
def testcommand(commandline, commandinfo):
    """
    Usage: !bot testcommand some stuff
    
    A command used for testing. Returns some of the info you send, formatted as a string
    """
    
    try:
        __t = commandline[1]
    except IndexError:
        return 'This command requires at least one argument'
    else:
        return '|'.join([commandline[1], commandinfo['command'], commandinfo['creator']['name']])
    
    
