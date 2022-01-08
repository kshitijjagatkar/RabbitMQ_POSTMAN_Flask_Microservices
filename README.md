# RabbitMQ_POSTMAN_Flask_Microservices
This is an Exercise on implementing Microservicecs which communicates through RabbitMQ which is  s a messaging broker - an intermediary for messaging using POSTMAN API call.


1. Project Summary
2. Project Components
3. File Descriptions
4. Installation & Run
5. Results


## 1. Project Summary
 This is an exercise which covers the concepts of the RabbitMQ using microservice & to send an email by calling an api through POSTMAN. RabbitMQ RabbitMQ is a message broker: it accepts and forwards messages using it's queue.
 
## 3. Project Components
This has two main components: 1. Producer 2. Consumer

1.   Producer
     * this section/folder has initiasation of the RabbitMQ in the flask app.
     * we will establish the connection using Pika client to rabbitmq server.
     * declare our exchange or queue for communicating
     * Then we will assemble our message & send/publish it.
2.  Consumer : we have two consumer 1.send_mail 2.logger
    * send_mail 
         * here, we again extablishing the connection to RabbitMQ server.
         * We then bind our queue to the exchange & starts consuming message
         * After taking taking message we first converts it into normal as it's raw form is binary.
         * we seperate our data which will be our email content: mail_id, subject, mail_body & sends a mail using SMTP library
    * Logeer
         *  this process is responsible for consuming data from send_mail process & stores/logs those data into text file.
         *  first we connect to RabbitMQ server, consume using our queue & again convert the data from binary to string.
         *  stroes the data into text file.
     
## 3. File Structure & Description
* Producer
  
  |- main_app.py # Flask app which initialise the rabbitmq producer.
  
  | - template
  
  | |- email_form.html  # form that takes email params
  
  | |- home.html # home page
  
  | |- index.html # main page
  
  | |- logger.html # shows user's i/p data/

* Consumer

  |- send_mail_app.py  # process that consumes data sends an email & again send data to logger process. 
  
  |- logger.py   # consumes the data & saves logs to text file.
  
  |- logs.txt  # log data
 

## 4. Installation & Run

This assignment requires pika, flask to run. you can install pika lib using python -m pip install pika --upgrade this command. Also create an environment using python3 -m venv venv this activate using this . venv/bin/activate & install flask using this pip install flask. Also install POSTMAN so that we can call through an API.
note: first we need to start from consumer first, so first run the consumer processes so that they can ready to consume the message.
  * Step1: run logger.py using python3 logger.py
  * Step2: run send_mail_app.py 
  * Step3: start the flask app python3 main_app.py which initiates the producer & create an exchange.
  * Step4 postman: start the postman use this request/url http://localhost:15672/api/exchanges/%2F/your_exchange/publish. note:exchange you created(logs in my case) or if no exhchange the use default(amq:default).
  * Step5 postman: In authorization choose basic authorization & login with rabbitmq credentials(default:gues:guest)
  * step6 postman: In body choose raw & provide necessary properties. {"properties": {},"routing_key": "", "payload": "recipient_mailID@gmail.com;this is sub; & this is mail body","payload_encoding": "string"} you can beatify this.
  * Step7: send this request as POST request. as soon as you sends this send_mail will consume this message & sends an email. you can stop this so send the data
  to the log process.
   

## 5. Results
It sends an email to the recipient address with subjest & mail body. also result of the logs & mail content can be seen in logs.txt file in the consumer folder.



    
