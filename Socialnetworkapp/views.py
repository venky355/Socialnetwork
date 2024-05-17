from django.shortcuts import render
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')

def activity(request):
    conversations = ['Conversation 1', 'Conversation 2', 'Conversation 3']
    default_conversation = conversations[0] if conversations else None
    message_history = ['Message 1', 'Message 2', 'Message 3']  

    context = {
        'conversations': conversations,
        'default_conversation': default_conversation,
        'message_history': message_history,
    }
    return render(request, 'activity.html', context)

def create_channel(request):
    return render(request, 'create_channel.html')

def channel_detail(request):
    channel_name = request.GET.get('name')
    channel_type = request.GET.get('type')
    context = {
        'channel_name': channel_name,
        'channel_type': channel_type,
    }
    return render(request, 'channel_detail.html', context)

def direct_messages(request):
    conversations = ['Conversation 1', 'Conversation 2', 'Conversation 3']

    context = {
        'conversations': conversations,
    }
    return render(request, 'direct_messages.html', context)

def message_detail(request, conversation_id=None):
    
    conversation = f"Conversation {conversation_id}"
    messages = [f"Message {i}" for i in range(1, 6)]  

    context = {
        'conversation': conversation,
        'messages': messages,
        'conversations': ['Conversation 1', 'Conversation 2', 'Conversation 3'],
    }
    return render(request, 'message_detail.html', context)