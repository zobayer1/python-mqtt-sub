# -*- coding: utf-8 -*-
import click
from paho.mqtt.client import Client

from mqttlistener.settings import get_settings


class MQTTClient:
    """Manages Paho MQTT client lifecycle and callbacks"""

    def __init__(self, message_processor=None):
        self.settings = get_settings()

        self.client = Client(
            client_id=self.settings.mqtt_client,
            transport=self.settings.mqtt_transport,
            clean_session=self.settings.mqtt_clean_session,
            userdata={"client": self.settings.mqtt_client},
        )

        self.client.username_pw_set(self.settings.mqtt_username, self.settings.mqtt_password)

        if self.settings.mqtt_debug:
            self.client.on_log = self._on_log

        self.client.on_connect = self._on_connect
        self.client.on_subscribe = self._on_subscribe
        self.client.on_message = self._on_message
        self.client.on_publish = self._on_publish
        self.client.on_disconnect = self._on_disconnect

        self.client.connect(self.settings.mqtt_host, self.settings.mqtt_port, 30)

        if message_processor:
            self.message_processor = message_processor

    def _on_log(self, client, userdata, level, buf):
        click.echo(f"{buf}, origin: {userdata['client']}")

    def _on_connect(self, client, userdata, flags, rc):
        click.echo(f"Connected {userdata['client']}, result code: {str(rc)} {str(flags)}")
        click.echo("Subscribing to all topics...")
        self.client.subscribe([(topic, self.settings.mqtt_sub_qos) for topic in self.settings.mqtt_sub_topics])

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        click.echo(f"Subscribed {userdata['client']}, mid: {mid}, granted qos: {granted_qos}")
        click.echo(f"Listening for {userdata['client']} messages...")

    def _on_disconnect(self, client, userdata, rc):
        click.echo(f"Disconnected {userdata['client']}, result code: {str(rc)}")

    def _on_message(self, client, userdata, msg):
        if hasattr(self, "message_processor"):
            self.message_processor(client, userdata, msg)
        else:
            click.echo(f"Topic: {msg.topic}, Mid: {msg.mid}, Payload: {msg.payload.decode('utf-8')}")

    def _on_publish(self, client, userdata, mid):
        click.echo(f"Published by {userdata['client']}, mid: {mid}")

    def listen(self):
        try:
            self.client.loop_forever()
        except KeyboardInterrupt:
            click.echo(f"\nReceived KeyboardInterrupt, disconnecting {self.settings.mqtt_client}")
            self.client.disconnect()
            click.echo(f"{self.settings.mqtt_client} disconnected")
