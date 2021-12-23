
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='resumen')
channel.queue_declare(queue='visitas')

ingreso = input("ingrese su palabra a buscar: ")

channel.basic_publish(exchange='',
                      routing_key='resumen',
                      body=ingreso)
channel.basic_publish(exchange='',
                      routing_key='visitas',
                      body=ingreso)


print(" [x] Sent 'consulta" + ingreso)

connection.close()

