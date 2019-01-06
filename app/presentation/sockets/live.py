from appfly.app import app

def event(message):
    """Video stream reader."""
    print('PUT IMAGES: {}'.format(app.images.qsize()))
    app.images.put(message['data'])

