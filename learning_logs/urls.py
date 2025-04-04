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
    # сторінка для додавання нової теми
    path('new_topic/', views.new_topic, name='new_topic'),
    # сторінка для додавання нового запису
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # сторінка для редагування запису
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Сторінка для додавання нової теми
    path('new_topic/', views.new_topic, name='new_topic'),
    # Сторінка для додавання нового запису
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Сторінка для редагування запису
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # ще назву
    path('<int:pk>', views.TopicDetailView.as_view(), name='topic_detail'),
]
