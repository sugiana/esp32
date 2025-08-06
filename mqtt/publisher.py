import sys
import json
from time import (
    sleep,
    time,
    strftime,
    )
from argparse import ArgumentParser
import paho.mqtt.client as mqtt


def on_connect(client, user_data, flags, rc, properties):
    if rc == 0:
        print(f'Sudah terhubung ke MQTT broker {option.host}:{option.port}.')
        print(f'Subscribe ke topik {response_topic}')
        client.subscribe(response_topic)
    else:
        print(f'Gagal terhubung, return code {rc}')


def on_message(client, user_data, message):
    payload = message.payload.decode()
    payload = json.loads(payload)
    print(f'Diterima {payload} dari topik {message.topic}')
    if message_id != payload['id']:
        return
    latency = time() - registry['sent_time']
    print(f'Penantian {latency:.2f} detik')
    registry['stop'] = True


host = 'localhost'
help_host = f'default {host}'

port = 1883
help_port = f'default {port}'

client_id = 'laptop-sugiana'
help_client_id = f'default: {client_id}'

topic = 'lampu/cac20c5871dcc'
help_topic = f'default: {topic}'

wait_seconds = 30
help_wait_seconds = f'default {wait_seconds}'

message = 'on'
help_message = f'default: {message}'

pars = ArgumentParser()
pars.add_argument('--host', default=host, help=help_host)
pars.add_argument('--port', default=port, type=int, help=help_port)
pars.add_argument('--client-id', default=client_id, help=help_client_id)
pars.add_argument('--topic', default=topic, help=help_topic)
pars.add_argument('--message', default=message, help=help_message)
pars.add_argument(
    '--wait-seconds', default=wait_seconds, type=int, help=help_wait_seconds)
option = pars.parse_args(sys.argv[1:])

registry = dict(sent_time=None, stop=False)
response_topic = '/'.join([option.topic, 'response'])

client = mqtt.Client(
        client_id=client_id,
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(option.host, option.port)
client.loop_start()
message_id = strftime('%H%M%S')
payload = dict(message=option.message, id=message_id)
while True:
    sleep(2)
    if registry['stop']:
        break
    result = client.publish(option.topic, json.dumps(payload), qos=1)
    if result.rc != 0:
        print('Pengiriman pesan gagal.')
        break
    print(f'Publish {payload} dengan topik {option.topic}')
    if registry['sent_time']:
        latency = time() - registry['sent_time']
        if latency > option.wait_seconds:
            print(f'Ambang batas {latency:.2f} detik')
            break
    else:
        registry['sent_time'] = time()
