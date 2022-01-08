import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='send_mail_app_logs')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

        encoding = 'utf-8'
        data = str(body, encoding)
        data = data.split(';')
        #user_mail_data = data[0]
        #p_start = data[1]
        #p_mail_sent = data[2]
        #p_halt = data[3]
        #p_end = data[4]
        file1 = open('logs.txt', 'a')
        file1.writelines(data)
        file1.close

    channel.basic_consume(queue='send_mail_app_logs', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)