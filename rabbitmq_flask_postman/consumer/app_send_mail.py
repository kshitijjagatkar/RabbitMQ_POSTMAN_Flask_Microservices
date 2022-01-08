import pika
from datetime import datetime
import smtplib 


def callback(ch, method, properties, body):
    print(" [x] %r" % body)

    global data
    encoding = 'utf-8'
    data = str(body, encoding)
    data = data.split(';')
    print(data)

    to = data[0]
    sub = data[1]
    mail_body = data[2]

    message = 'Subject: {}\n\n{}'.format(sub, mail_body)

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("kshitijjagatkar@gmail.com","ewxacodmgvzrhdeb")
    server.sendmail("kshitijjagatkar@gmail.com", to, message)

    global p_send_mail 
    p_send_mail = str(datetime.now())


def send_logs(data,log_data):


    channel.queue_declare(queue='send_mail_app_logs')

    channel.basic_publish(
        exchange='',
        routing_key='send_mail_app_logs',
        body="{};{}".format(data,log_data),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))

    connection.close()
    
    return p_end


if __name__ == '__main__':

    print(' [*] Connecting to server ...')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs', queue=queue_name)
    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

    p_halt = "no_hulting occured"
    try:
        p_start = str(datetime.now())
        channel.start_consuming()

    except KeyboardInterrupt:
        p_halt = str(datetime.now())
        print("KeyboardInterrupt.")

    p_end = str(datetime.now())
    log_data = "process starts at:{};Mail sent at:{};process halts/ends by inturrupt:{}; \
                process ends at:{}".format(p_start,p_send_mail,p_halt,p_end)

    send_logs(data,log_data)
    


    #######################################################





