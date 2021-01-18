# -*- coding: utf-8 -*-
import os
import re
import json
from configparser import SafeConfigParser

import click


class Config(object):
    """Manages configuration parameters"""

    def __init__(
        self,
        mqtt_host: str,
        mqtt_port: int,
        mqtt_username: str,
        mqtt_password: str,
        mqtt_client: str,
        mqtt_topics: list,
        mqtt_clean_session: bool,
        mqtt_debug: bool,
    ):
        self.mqtt_host = mqtt_host
        self.mqtt_port = mqtt_port
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.mqtt_client = mqtt_client
        self.mqtt_topics = [(tt[0].strip(), int(tt[1].strip())) for tt in mqtt_topics]
        self.mqtt_clean_session = mqtt_clean_session
        self.mqtt_debug = mqtt_debug

    @classmethod
    def load_from(cls, filename: str):
        parser = SafeConfigParser()
        try:
            with open(filename, encoding="utf-8") as config_file:
                parser.read_file(config_file)
                return cls(
                    parser["mqtt"]["mqtt_host"],
                    int(parser["mqtt"]["mqtt_port"]),
                    parser["mqtt"]["mqtt_username"],
                    parser["mqtt"]["mqtt_password"],
                    parser["mqtt"]["mqtt_client"],
                    [
                        tuple(tt.split(","))
                        for tt in re.findall(r"\(([^\)]+)\)", parser["mqtt"]["mqtt_topics"])
                        if tt and len(tt) > 0
                    ],
                    parser["mqtt"]["mqtt_clean_session"].lower() == "true",
                    parser["mqtt"]["mqtt_debug"].lower() == "true",
                )
        except KeyError as err:
            click.echo(f"Missing configuration key: {str(err)}")
        except (IOError, OSError) as err:
            click.echo(f"Error reading configuration file. {str(err)}")

    def __repr__(self):
        return json.dumps(self.__dict__, indent=2, sort_keys=True)
