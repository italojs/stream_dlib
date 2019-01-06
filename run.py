import argparse
from app import config
from appfly.app import app, socketio
from appfly.server import Server

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="Start your API in debug mode. [true/false]")
args = parser.parse_args()

debug = False
if args.debug:
    if args.debug.lower() == 'true':
        debug = True
    elif args.debug.lower() == 'false': 
        pass
    else:
        raise Exception('Invalid parameter to debug args, please, set "true" or "false"')

if __name__ == '__main__':
    srv = Server(app, socketio)
    srv.start(config)
    