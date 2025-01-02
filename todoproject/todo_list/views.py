from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DeleteView, View
from .models import TodoItem


class TodoItemsListView(ListView):
    model = TodoItem

class TodoItemCreateView(CreateView):
    model = TodoItem
    fields = [
        "text",
    ]
    success_url = reverse_lazy("todo-list:items-list")

class ToDoItemDeleteView(DeleteView):
    model = TodoItem
    success_url = reverse_lazy("todo-list:items-list")

class ToDoItemToggleView(View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        todo_item: TodoItem = get_object_or_404(TodoItem, pk=pk)
        todo_item.done = not todo_item.done
        todo_item.save()
        url = reverse('todo-list:items-list')
        return redirect(url)
