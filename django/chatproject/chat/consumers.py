# chat/consumers.py

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.receiver_username = self.scope['url_route']['kwargs']['username']
        try:
            self.receiver = User.objects.get(username=self.receiver_username)
        except User.DoesNotExist:
            self.close()
            return

        self.sender = self.scope['user']
        if self.sender == self.receiver:
            self.close()
            return

        self.room_name = f'chat_{min(self.sender.id, self.receiver.id)}_{max(self.sender.id, self.receiver.id)}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '').strip()

        if message:
            # Save message to database
            Message.objects.create(
                sender=self.sender,
                receiver=self.receiver,
                content=message
            )

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': self.sender.username,
                }
            )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))
