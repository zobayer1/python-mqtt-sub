# -*- coding: utf-8 -*-
import os

import click

from mqttlistener.config import Config
from mqttlistener.client import MQTTClient
from mqttlistener.process import on_message


@click.command()
@click.option(
    "--config-path",
    default=f"{os.path.join(os.getcwd(), 'config.cfg')}",
    help="Configuration file path",
)
def main(config_path):
    click.echo(f"Loading configuration file: {config_path}")
    config = Config.load_from(config_path)
    client = MQTTClient(config, message_processor=on_message)
    click.echo("Starting client loop")
    client.listen()
    click.echo("Exiting...")
