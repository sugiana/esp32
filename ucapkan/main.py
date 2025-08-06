from common import base_main
from play import ucapkan


TOPIC = 'pengucapan'


def on_response(request):
    ucapkan(request['message'])
    return dict(
        code=0, message='OK', id=request['id'])


def on_broker_failure(durasi):
    pass
    #ucapkan(f'gagal terhubung ke sistem {TOPIC}')


base_main(TOPIC, on_response, on_broker_failure=on_broker_failure)
