from django.shortcuts import render, redirect
from .forms import ActivityForm, ChannelCreationForm, MessageForm

def home(request):
    return render(request, 'home.html')

def activity(request):
    content = "Select an activity option to view content."
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.cleaned_data['activity']
            if activity == 'mentions':
                content = "📧 No mentions yet."
            elif activity == 'threads':
                content = "@ No threads yet."
            elif activity == 'reactions':
                content = "😑 No reactions yet."
            elif activity == 'invitations':
                content = "📩 No invitations yet."
    else:
        form = ActivityForm()
    
    return render(request, 'activity.html', {'form': form, 'content': content})

def channel_detail(request):
    context = {
        'example_data': 'This is some example data to pass to the template.',
    }
    return render(request, 'channel_detail.html', context)

def create_channel(request):
    if request.method == 'POST':
        form = ChannelCreationForm(request.POST)
        if form.is_valid():
            channel_name = form.cleaned_data['channel_name']
            channel_type = form.cleaned_data['channel_type']
            return redirect('channel_details', name=channel_name, type=channel_type)
    else:
        form = ChannelCreationForm()
    
    return render(request, 'create_channel.html', {'form': form})

def direct_messages(request):
    conversations = ['User 1', 'User 2', 'User 3']
    default_conversation = conversations[0]

    message_history = get_message_history(default_conversation)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            send_message(default_conversation, message)
            return redirect('direct_messages')
    else:
        form = MessageForm()

    context = {
        'conversations': conversations,
        'default_conversation': default_conversation,
        'message_history': message_history,
        'form': form,
    }
    return render(request, 'direct_messages.html', context)

def get_message_history(conversation):
    return [
        {'sender': 'User 1', 'message': 'Hi there!'},
        {'sender': 'You', 'message': 'Hello!'},
        {'sender': 'User 1', 'message': 'How are you?'},
        {'sender': 'You', 'message': 'I\'m doing great, thanks!'},
    ]

def send_message(conversation, message):
    print(f"Sending message to {conversation}: {message}")
