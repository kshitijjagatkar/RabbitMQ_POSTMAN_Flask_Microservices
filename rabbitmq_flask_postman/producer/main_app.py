from flask import Flask, url_for, render_template, request, redirect
import pika

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

def producer(data):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='logs', exchange_type= 'fanout')

    channel.basic_publish(
        exchange='logs',
        routing_key='',
        body="{};{};{}".format(data[0],data[1],data[2]),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    
    connection.close()

    return " [x] Sent: {};{};{} ".format(data[0],data[1],data[2])


@app.route('/email_form', methods=["POST","GET"])
def email_form():
    

    if request.method == 'POST':

        to = request.form["email"]
        sub = request.form["mail_sub"]
        mail_body = request.form["mail_body"]

        global data 
        data = [to,sub,mail_body]

        return render_template("logger.html",data=data)

    else:
        return render_template("email_form.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5001)
    producer(data)
    