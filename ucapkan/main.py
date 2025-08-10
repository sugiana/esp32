from time import time
from common import base_main
from play import ucapkan


TOPIC = 'pengucapan'
registry = dict(low_batt_voice_time=None)


def on_response(request):
    ucapkan(request['message'])
    return dict(
        code=0, message='OK', id=request['id'])


def on_broker_failure(durasi):
    print(f'gagal terhubung ke sistem {TOPIC}')


def on_batt(voltage, level):
    print(f'Baterai {voltage}V, {level}%')
    if level > 20:
        return
    print('Baterai perlu diisi')
    if registry['low_batt_voice_time']:
        if time() - registry['low_batt_voice_time'] < 300:
            return
    registry['low_batt_voice_time'] = time()
    ucapkan('baterai perlu di isi')


base_main(
    TOPIC, on_response, on_broker_failure=on_broker_failure, on_batt=on_batt)
