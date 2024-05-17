from django import forms

class ActivityForm(forms.Form):
    activity = forms.ChoiceField(choices=[
        ('mentions', 'Mentions'),
        ('threads', 'Threads'),
        ('reactions', 'Reactions'),
        ('invitations', 'Invitations'),
    ], label='Select Activity')

class ChannelForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    # Add more fields as needed

class ChannelCreationForm(forms.Form):
    channel_name = forms.CharField(label='Channel Name', max_length=100)
    channel_type = forms.ChoiceField(label='Channel Type', choices=[('public', 'Public'), ('private', 'Private')])    

class MessageForm(forms.Form):
    message = forms.CharField(label='Message', widget=forms.TextInput(attrs={'placeholder': 'Type your message...'}))    
