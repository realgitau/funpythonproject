from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The homepage"""
    return render(request, 'accounts/index.html')

def topics(request):
    """The topics page show all topics"""
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'accounts/topics.html', context)

def topic(request, topic_id):
    """Show a single topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'accounts/topic.html', context)