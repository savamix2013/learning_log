from django.db import models
from django.contrib.auth.models import User

# Функція, яка повертає першого користувача
def get_default_user():
    return User.objects.first()

# Модель Topic
class Topic(models.Model):
    """Тема, яку вивчає користувач"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

    def __str__(self):
        return self.text

# Модель Entry
class Entry(models.Model):
    """Вхідні дані користувача"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
    
# Модель Articles
class Articles(models.Model):
    """Модель статей"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """Повертає URL-адресу статті"""
        return f"/articles/{self.id}/"
    def get_update_url(self):
        """Повертає URL-адресу для редагування статті"""
        return f"/articles/{self.id}/edit/"
    def get_delete_url(self):
        """Повертає URL-адресу для видалення статті"""
        return f"/articles/{self.id}/delete/"
    def get_list_url(self):
        """Повертає URL-адресу для списку статей"""
        return "/articles/"
    def get_create_url(self):
        """Повертає URL-адресу для створення нової статті"""    

