from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import DetailView
from .models import Articles
from .forms import ArticlesForm

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

class TopicDetailView(DetailView):
    model = Articles
    template_name = 'learning_logs/topic_detail.html'
    context_object_name = 'article'

def index(request):
    """Головна сторінка журналу спостережень"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Виводить всі теми"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Виводить всі записи для однієї теми"""
    topic = Topic.objects.get(id=topic_id)
    # Перевірка того, чи тема належить поточному користувачеві
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Додає нову тему."""
    if request.method != 'POST':
        # Жодних даних не було надіслано; створюється порожня форма
        form = TopicForm()
    else:
        # Відправлений POST-запит; обробити дані.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Показати порожню або недійсну форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Додає новий запис для певної теми."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Жодних даних не було надіслано; створюється порожня форма
        form = EntryForm()
    else:
        # Відправлений POST-запит; обробити дані.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Показати порожню або недійсну форму
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

