from django.shortcuts import render
from django.views.generic import ListView
from .models import TodoItem


class TodoItemListView(ListView):
    model = TodoItem

