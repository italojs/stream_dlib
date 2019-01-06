from appfly import response

def event():
    """Connect event."""
    # print('Client wants to connect.')
    response.emit_event('response', {'data': 'OK'})