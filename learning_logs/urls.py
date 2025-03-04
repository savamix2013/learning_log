"""Defines URL"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
    # сторінка відображає усі теми
    path('topics/', views.topics, name='topics'),
    # сторінка, присвячена окремій темі
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]