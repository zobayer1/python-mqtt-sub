# -*- coding: utf-8 -*-
"""
Sample processing method. You can, for example, add a process pool to handle them concurrently.
"""
import click


def on_message(_client, _userdata, message):
    decode_data = str(message.payload.decode("utf-8", "ignore"))
    click.echo('Topic: "{}", Client: "{}", Message: {}'.format(message.topic, _userdata["client"], decode_data))
