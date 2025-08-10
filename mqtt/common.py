import json
from time import (
    sleep,
    time,
    )
from ubinascii import hexlify
from umqtt.simple import MQTTClient
from wifimgr import (
    wlan_sta,
    get_connection,
    )
from batt import (
    get_voltage,
    get_level,
    )


with open('broker.dat') as f:
    s = f.read().strip()
host, port = s.split(':')

client_id = hexlify(wlan_sta.config('mac'))

messages = dict(ids=[])
broker_connection = dict(waktu_gagal=None)


def base_main(
        topic, on_response, on_subscribed=None, on_broker_failure=None,
        on_batt=None):
    wlan = get_connection()
    if wlan is None:
        print('Gagal terhubung ke jaringan.')
        return

    def sub_cb(topic, msg):
        request = msg.decode()
        request = json.loads(request)
        print(f'Diterima {request} dari topik {topic.decode()}')
        msg_id = request['id']
        if msg_id in messages:
            response = messages[msg_id]
        else:
            try:
                response = on_response(request)
            except Exception as e:
                response = dict(code=99, message=str(e), id=msg_id)
            messages[msg_id] = response
            messages['ids'].append(msg_id)
        message = json.dumps(response)
        print(f'Publish {response} ke topik {topic_publish.decode()}')
        client.publish(topic_publish, message.encode())
        if messages['ids'][1:]:
            # Hapus sebelumnya untuk menghemat memory
            msg_id = messages['ids'][0]
            del messages[msg_id]
            messages['ids'] = messages['ids'][1:]

    def connect():
        try:
            client.connect()
            print(f'Sudah terhubung ke MQTT broker {host}:{port}.')
            broker_connection['waktu_gagal'] = None
        except Exception as e:
            print(f'Gagal terhubung ke MQTT broker: {e}')
            if broker_connection['waktu_gagal']:
                durasi = time() - broker_connection['waktu_gagal']
                on_broker_failure and on_broker_failure(durasi)
            else:
                broker_connection['waktu_gagal'] = time()
            return
        client.subscribe(topic_subscribe)
        print(f'Subscribe ke topik {topic_subscribe.decode()}')
        on_subscribed and on_subscribed(topic_subscribe)

    topic_subscribe = topic.encode() + b'/' + client_id
    topic_publish = topic_subscribe + b'/response'
    client = MQTTClient(
            client_id=client_id, server=host, port=port, keepalive=60)
    client.set_callback(sub_cb)
    flip = True
    connect()
    while True:
        try:
            client.check_msg()
        except Exception as e:
            print(f'Ada masalah saat check_msg(): {e}')
            if wlan_sta.isconnected():
                print('Connected. Network config: ', wlan_sta.ifconfig())
                connect()
        finally:
            if flip:
                titik = '...'
                flip = False
            else:
                titik = '..'
                flip = True
            voltage = get_voltage()
            level = get_level(voltage)
            on_batt and on_batt(voltage, level)
            print('Menunggu ' + titik)
            sleep(1)  # Agar CPU lebih nyaman
