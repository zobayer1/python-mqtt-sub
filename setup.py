# -*- coding: utf-8 -*-
from os import path
from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name='python-mqtt-sub',
    url="https://github.com/zobayer1/python-mqtt-sub",
    author="Zobayer Hasan",
    author_email="zobayer1@gmail.com",
    license="MIT",
    description="Paho MQTT based CLI template",
    keywords="python paho cli mqtt client subscriber publisher pubsub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    use_scm_version=True,
    packages=find_packages(exclude=["docs", "tests"]),
    platforms=["any"],
    entry_points={
        "console_scripts": [
            "mqttlistener = mqttlistener.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
