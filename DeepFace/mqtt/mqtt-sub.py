# #Bibliotecas
# #import paho.mqtt.client as mqtt
# from paho.mqtt import client as mqtt_client
# import random

# #Daros del broker
# broker = '3.122.69.139'
# port = 1883
# topic = "codigoIoT/mqtt/python"
# client_id = f'python-mqtt-{random.randint(0,1000)}'
# # username = 'emqx'
# #password = 'topic'

# #Conexion del broker
# def connect_mqtt():
#     def on_connect(client, username, userdata, flags, rc):
#         if rc == 0:
#             print("Connected to MQTT Broker!")
#         else:
#             print("Failed to connect, return code %d\n", rc)
#     #Set connecting client ID
#     client = mqtt_client.Client(client_id)
#     #client.username_pw_set(username, password)
#     client.on_connect = on_connect
#     client.connect(broker, port)
#     return client

# #Suscripcion 
# def subscribe(client: mqtt_client):
#     def on_message(client, userdata, msg):
#         print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

#     client.subscribe(topic)
#     client.on_message = on_message

# #Opcional A
# client = connect_mqtt()
# subscribe(client)
# client.loop_forever()

# # #Opcional B
# # def run():
# #     client = connect_mqtt()
# #     subscribe(client)
# #     client.loop_forever()

# # if __name__ == '__main__':
# #    run()

# # #Opcional C
# # if __name__ == '__main__':
# #     client = connect_mqtt()
# #     subscribe(client)
# #     client.loop_forever()


import random

from paho.mqtt import client as mqtt_client


broker = '3.122.69.139'
port = 1883
topic = "codigoIoT/mqtt/python"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


#def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


# if __name__ == '__main__':
#     run()