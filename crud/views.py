from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = 'todo_list_view.html'
    
class TodoDetailView(DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'todo_detail_view.html'
    
class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description"]
    template_name = 'todo_create_view.html'
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "description"]
    template_name = 'todo_update_view.html'
    
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete_view.html'
    success_url = reverse_lazy('todo_list_view')