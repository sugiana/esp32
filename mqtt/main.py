from ubinascii import hexlify
import usocket as socket
import json
from time import sleep
from umqtt.simple import MQTTClient
from wifimgr import (
    get_connection,
    wlan_sta,
    )
import led


messages = dict(ids=[])


def main():
    wlan = get_connection()
    if wlan is None:
        print('Gagal terhubung ke jaringan.')
        return

    def sub_cb(topic, msg):
        request_payload = msg.decode()
        request_payload = json.loads(request_payload)
        print(f'Diterima {request_payload} dari topik {topic.decode()}')
        msg_id = request_payload.get('message_id')
        if msg_id in messages:
            response_payload = messages[msg_id]
        else:
            s = request_payload.get('message')
            if s in ('on', 'off', 'status'):
                code = 0
                if s == 'on':
                    led.on()
                elif s == 'off':
                    led.off()
                if led.is_on():
                    msg = 'on'
                else:
                    msg = 'off'
            else:
                code = 1
                msg = f'Perintah {s} tidak dipahami'
            response_payload = dict(code=code, message=msg, message_id=msg_id)
            messages[msg_id] = response_payload
            messages['ids'].append(msg_id)
        message = json.dumps(response_payload)
        print(f'Publish {response_payload} ke topik {topic_publish.decode()}')
        client.publish(topic_publish, message.encode())
        if messages['ids'][1:]:
            # Hapus sebelumnya untuk menghemat memory
            msg_id = messages['ids'][0]
            del messages[msg_id]
            messages['ids'] = messages['ids'][1:]

    def connect():
        try:
            client.connect()
            print('Sudah terhubung ke MQTT broker.')
        except Exception as e:
            print(f'Gagal terhubung ke MQTT broker: {e}')
            return
        client.subscribe(topic_subscribe)
        print(f'Subscribe ke topik {topic_subscribe.decode()}')

    with open('broker.dat') as f:
        s = f.read().strip()
    host, port = s.split(':')
    client_id = hexlify(wlan_sta.config('mac'))
    topic_subscribe = b'lampu/' + client_id
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
            print(e)
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
            print('Menunggu ' + titik)
            sleep(1)  # Agar CPU lebih nyaman
    # client.disconnect()


main()
