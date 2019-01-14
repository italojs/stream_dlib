import os
import json
import appfly
from queue import Queue
from appfly.app import factory

def fn(appfly_app):
    appfly_app.images = Queue()

    # Routes files
    from app.presentation.routes import video_feed as rVideo_feed

    # Views
    from app.presentation.views import page as vPage

    # Routes rules
    appfly.add_url('/video_feed', rVideo_feed.route, 'GET')
    appfly.add_url('/', vPage.view, 'GET')

    # Sockets
    from app.presentation.sockets import live
    from app.presentation.sockets import connect
    from app.presentation.sockets import message
    from app.presentation.sockets import disconnect

    appfly.add_event('event', message.event, '/live')
    appfly.add_event('livevideo', live.event, '/live')
    appfly.add_event('connect', connect.event, '/live')
    appfly.add_event('disconnect', disconnect.event, '/live')

# Config
config = json.load(open('./app/config.json'))
factory(fn, __name__, config["cors"], template_folder=os.environ.get('FULL_TEMPLATE_PATH'), has_socket=True)