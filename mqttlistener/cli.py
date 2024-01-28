# -*- coding: utf-8 -*-
import click

from mqttlistener.client import MQTTClient
from mqttlistener.process import on_message


@click.command("Run MQTT listener")
@click.help_option(help="Show help index and exit")
@click.version_option(message="v%(version)s", package_name="mqttlistener", help="Show the version and exit")
def main():
    client = MQTTClient(message_processor=on_message)
    click.echo("Starting client loop")
    client.listen()
    click.echo("Exiting...")
