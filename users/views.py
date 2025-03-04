from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Показати порожню форму реєстрації
        form = UserCreationForm()
    else:
        # Обробити заповнену форму
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Увійти користувача і перенаправити на домашню сторінку
            login(request, new_user)
            return redirect('learning_logs:index')

    # Показати порожню або недійсну форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)
