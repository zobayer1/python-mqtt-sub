# Python Paho MQTT Subscriber Template

Paho MQTT based CLI template for subscribers. Users must add message processors. Program handles auto reconnect and
allows subscriptions to multiple topics.

## Pre-requisites

1. Python 3.11+
2. Poetry
3. Git

## Installation

### From source

1. Change directory to the root of source folder
2. Run `poetry install`
3. Generate distribution packages: `poetry build`

### From wheel

1. Activate a venv with python 3.11+
2. Install using pip: `pip install mqttlistener-{version_tag}.whl`

## Execution

Installation will make `mqttlistener` command available. Run `mqttlistener --help` for help menu.

Example: `mqttlistener`

This will block the running terminal, use with tools like `screen` or `nohup` for background execution.

## Configurations

The program reads various configuration parameters from the environment:

    MQTT_HOST=mqtt
    MQTT_PORT=1883
    MQTT_USERNAME=username
    MQTT_PASSWORD=pasword
    MQTT_CLIENT=someclientid
    MQTT_KEEP_ALIVE=30
    MQTT_SUB_TOPICS='["topics/a1","topics/a2"]'
    MQTT_SUB_QOS=1
    MQTT_CLEAN_SESSION=false
    MQTT_DEBUG=true

Currently all parameters must be present, you can modify the code to make some of them optional according to your
application.

You can add these in a `.env` file for setting environment variables easily. An example `.env` file:

    #!/usr/bin/env sh
    export MQTT_HOST=mqtt
    export MQTT_PORT=1883
    export MQTT_USERNAME=username
    export MQTT_PASSWORD=password
    export MQTT_CLIENT=someclientid
    export MQTT_KEEP_ALIVE=30
    export MQTT_SUB_TOPICS='["topics/a1","topics/a2"]'
    export MQTT_SUB_QOS=1
    export MQTT_CLEAN_SESSION=false
    export MQTT_DEBUG=true

**Note**: `MQTT_SUB_TOPICS` must be a valid parsable JSON encoded string.

## Development

### Code Formatting

Install `pre-commit`:

    poetry install --with dev
    pre-commit install
    pre-commit autoupdate
    pre-commit run --all-files  # First time only

From the next commits, pre-commit hooks will be executed automatically.

### Message Processing

When creating the MQTT client in `mqttlistener/cli:main`, you can pass a function reference to process message.
Processor function will be called with three parameters:

1. client: Paho MQTT client,
2. userdata: Client userdata,
3. message: Paho MQTT message object.

Example:

    def on_message(client, userdata, message):
        print(f"Message Topic: {message.topic}")
        print(f"Message ID: {message.mid}")
        print(f"Message Payload: {message.payload.decode('utf-8')}")

Register in `cli` module:

    client = MQTTClient(message_processor=on_message)


### Test Subscription

With mosquitto installed in your system, you can run following command to quickly publish message to a topic:

    mosquitto_pub -h localhost -p 1883 -u mqtt-sub-username -P mqtt-sub-password -t topics/a1 -d -q 1 -l


## License:

[MIT License](./LICENSE)
