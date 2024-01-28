# -*- coding: utf-8 -*-
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "mqttlistener"
    mqtt_host: str
    mqtt_port: int = 1883
    mqtt_transport: str = "tcp"
    mqtt_username: str
    mqtt_password: str
    mqtt_client: str
    mqtt_keep_alive: int = 30
    mqtt_sub_topics: list[str]
    mqtt_sub_qos: int = 1
    mqtt_clean_session: bool = False
    mqtt_debug: bool = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
