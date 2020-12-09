# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='python-mqtt-sub',
    version='1.0.0',
    license="MIT",
    py_modules=['mqttlistener'],
    install_requires=[
        'click',
        'paho-mqtt'
    ],
    entry_points={
        "console_scripts": [
            "mqttlistener = mqttlistener.cli:main",
        ],
    },
)
