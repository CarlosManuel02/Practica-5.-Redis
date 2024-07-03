import redis
import json

def consume_messages():
    # Conexión a Redis
    redis_client =  redis.Redis(
        host='redis-17315.c270.us-east-1-3.ec2.redns.redis-cloud.com',
        port=17315,
        password='7XKzDRuIvlTKP0iALwsux61DArrj8uJb')

    
    # Suscribirse al canal 'data_channel'
    pubsub = redis_client.pubsub()
    pubsub.subscribe('data_channel')

    print("Esperando mensajes...")

    # Procesar los mensajes en tiempo real
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            print(f"Mensaje recibido: {data}")

if __name__ == "__main__":
    consume_messages()
