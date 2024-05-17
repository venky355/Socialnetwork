from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('activity', views.activity, name='activity'),
    path('channel_detail/', views.channel_detail, name='channel_detail'),
    path('create_channel', views.create_channel, name='create_channel'),
    path('direct_messages', views.direct_messages, name='direct_messages'),
    path('message_detail/', views.message_detail, name='message_detail'),
]
