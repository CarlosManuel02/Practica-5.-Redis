import redis
import time
import json
from random import randint

def produce_messages():
    # Conexión a Redis
    redis_client = redis.Redis(
        host='redis-17315.c270.us-east-1-3.ec2.redns.redis-cloud.com',
        port=17315,
        password='7XKzDRuIvlTKP0iALwsux61DArrj8uJb')

    while True:
        # Crear un mensaje de ejemplo
        message = {
            'id': randint(1, 100),
            'value': randint(1, 1000)
        }
        
        # Publicar el mensaje en el canal 'data_channel'
        redis_client.publish('data_channel', json.dumps(message))
        
        print(f"Mensaje producido: {message}")
        
        # Esperar un segundo antes de enviar el siguiente mensaje
        time.sleep(1)

if __name__ == "__main__":
    produce_messages()
