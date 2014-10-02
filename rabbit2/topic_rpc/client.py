#!/usr/bin/env python
import pika
import sys
import uuid
import time
queueName = 'all'
exchange_name = 'updator'
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.95.164'))
channel = connection.channel()

channel.exchange_declare(exchange=exchange_name,
                         type='topic')
result = channel.queue_declare(exclusive=True)
#result = channel.queue_declare(queue=queueName)
callback_queue = result.method.queue
global response
response = None
def on_response(ch, method, props, body):
    global response
    if corr_id == props.correlation_id:
        response = body
        print 'show response'
        print response
routing_key=sys.argv[1]
message = sys.argv[2]

message = ' '.join(sys.argv[2:]) or 'Hello World!'
corr_id = str(uuid.uuid4())
channel.basic_consume(on_response, no_ack=True,
                           queue=callback_queue)
channel.basic_publish(exchange=exchange_name,
                      routing_key=routing_key,
                      properties=pika.BasicProperties(
                                       reply_to = callback_queue,
                                       correlation_id = corr_id,
                                       ),
                      body=message)
while response is None:
      print 'wait for response.....'
      connection.process_data_events()
      time.sleep(1)
print " [x] Sent %r:%r" % (routing_key, message)
connection.close()
