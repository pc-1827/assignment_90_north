# chat/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Message

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

@login_required
def chat(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/chat.html', {'users': users})

@login_required
def get_messages(request, username):
    try:
        receiver = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=404)

    messages = Message.objects.filter(
        sender=request.user, receiver=receiver
    ) | Message.objects.filter(
        sender=receiver, receiver=request.user
    )
    messages = messages.order_by('timestamp')

    messages_data = []
    for msg in messages:
        messages_data.append({
            'sender': msg.sender.username,
            'content': msg.content,
            'timestamp': msg.timestamp,
        })

    return JsonResponse({'messages': messages_data})
