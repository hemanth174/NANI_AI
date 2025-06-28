from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('talk/', views.talk_to_nani, name='talk_to_nani'),
    path('explore/', views.explore, name='explore'),
    path('emergency/', views.emergency, name='emergency'),
    path('profile/', views.profile, name='profile'),
    path('start-assistant', views.start_assistant, name='start_assistant'),
    path('talk-assistant/', views.talk_assistant, name='talk_assistant'),
]

