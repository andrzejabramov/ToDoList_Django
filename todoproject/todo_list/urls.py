from django.urls import path
from .views import TodoItemsListView, TodoItemCreateView, ToDoItemDeleteView, ToDoItemToggleView

app_name = "todo-list"

urlpatterns = [
    path("", TodoItemsListView.as_view(), name="items-list"),
    path("create/", TodoItemCreateView.as_view(), name="create-item"),
    path("<int:pk>/confirm-delete/", ToDoItemDeleteView.as_view(), name="delete-item"),
    path("<int:pk>/toggle/", ToDoItemToggleView.as_view(), name="toggle-item"),
]
