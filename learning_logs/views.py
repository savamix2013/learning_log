from django.shortcuts import render

# Create your views here.

from .models import Topic

def index(request):
    """головна сторінка журналу спостережень"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """виводить всі теми"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """виводить всі записи для однієї теми"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)