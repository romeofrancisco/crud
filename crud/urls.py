from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView


urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list_view'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name='todo_detail_view'),
    path('todo/add', TodoCreateView.as_view(), name='todo_create_view'),
    path('todo/<int:pk>/edit', TodoUpdateView.as_view(), name='todo_update_view'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name='todo_delete_view'),
]