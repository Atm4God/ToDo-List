from django.urls import path, include
from . import views as todo_views


urlpatterns = [
    path('', todo_views.index, name='todo-index'),
    path('add', todo_views.add_todo, name='add'),
    path('complete/<todo_id>', todo_views.complete_todo, name='complete'),
    path('delete_complete', todo_views.delete_completed, name='delete_complete'),
    path('delete_all', todo_views.delete_all, name='delete_all'),
]

