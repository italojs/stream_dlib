from app.domain.live_stream import gen_livestream
from flask import Response

def route():
    return Response(
        response=gen_livestream(),
        content_type="text/event-stream")