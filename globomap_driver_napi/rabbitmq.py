"""
   Copyright 2017 Globo.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
# -*- coding: utf-8 -*-
import json

import pika


class RabbitMQClient(object):

    def __init__(self, host, port, user, password, vhost, queue_name):

        credentials = pika.PlainCredentials(user, password)
        parameters = pika.ConnectionParameters(
            host=host, port=port,
            virtual_host=vhost, credentials=credentials
        )
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def read_messages(self, number_messages=1):
        messages = []
        while True:
            try:
                message = self.get_message()
            except StopIteration:
                if messages:
                    yield messages
                break
            else:
                messages.append(message)
                if len(messages) == number_messages:
                    yield messages

    def get_message(self):
        message = self._consumer().next()
        if isinstance(message, dict):
            return message

    def _consumer(self):
        while True:
            method_frame, _, body = self.channel.basic_get(self.queue_name)
            if method_frame:
                self.channel.basic_ack(method_frame.delivery_tag)
                body = json.loads(body)
                yield body
            else:
                break
