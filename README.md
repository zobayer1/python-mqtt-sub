# Python Paho MQTT Subscriber Template

Paho MQTT based CLI template for subscribers. Users must add message processors. Program handles auto reconnect and
allows subscriptions to multiple topics.


## Installation

1. Change directory to the root of source folder
2. Start a venv with Python 3.6+
2. Run `pip install -e .`


## Execution

Installation will make `mqttlistener` command available. Run `mqttlistener --help` for help menu.

Example: `mqttlistener --config-path=/path/to/config.cfg`

This will block the running terminal, use with tools like screen or nohup.


## Configurations

Following keys must be provided in a configuration file:

    [mqtt]
    mqtt_host = localhost
    mqtt_port = 1883
    mqtt_username = mqtt-sub-username
    mqtt_password = mqtt-sub-password
    mqtt_client = mqtt-client-id-01
    mqtt_topics = (test-topic/0,1),(test-topic/1,1)
    mqtt_clean_session = False
    mqtt_debug = True

Currently all parameters must be present, you can modify the code to make some of them optional according to your
application.

Topic list is given as a comma separated list of tuples. First item of each tuple is topic name, and second item is
associated qos value. I'll leave it to the user to maintain proper formatting, no validation rules were added.

Program looks for default configuration file `config.cfg` in current working directory. You can pass in a configuration
file path using the `--config-path` parameter.

## Message Processing

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

## Test Subscription

With mosquitto installed in your system, you can run following command to quickly publish message to a topic:

    mosquitto_pub -h localhost -p 1883 -u mqtt-sub-username -P mqtt-sub-password -t test-topic/1 -d -q 1 -l


### Author: Zobayer Hasan (zobayer1@gmail.com)

### License: MIT
