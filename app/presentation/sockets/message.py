
from appfly import response

def event(message):
    """Simple websocket echo."""
    # print( message['data'])
    response.emit_event('response',
         {'data': message['data']})