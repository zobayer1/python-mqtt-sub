# -*- coding: utf-8 -*-
"""
Sample processing method. You can, for example, add a process pool to handle them concurrently.
"""
from mqttlistener.config import Config


def on_message(_client, _userdata, message):
    decode_data = str(message.payload.decode("utf-8", "ignore"))
    print('New message received on topic: "{}" Message: {}'.format(message.topic, decode_data))
