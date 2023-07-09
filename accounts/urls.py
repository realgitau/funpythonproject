
from django.urls import path
from .import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    
]