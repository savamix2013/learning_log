"""Визначає схеми URL для користувачів"""

from django.urls import path, include

from . import views


app_name = 'users'

urlpatterns = [
    # Додати уставні URL автентифікації
    path('', include('django.contrib.auth.urls')),
    # Сторінка реєстрації
    path('register/', views.register, name='register'),
]
