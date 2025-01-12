# Пояснение 
## к приложению To Do List на Django в рамках дипломной работы студента 
## Абрамова Андрея Васильевича

Используемая литература:  
https://metanit.com/python/django/  

https://www.djangoproject.com/


Итоговая структура приложения:
![project_tree](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/project_tree.png)

1. Создаем проект Django (в консоли):
```commandline
python3 -m startproject todoproject
```
2. Переходим в папку проекта:
```commandline
cd todoproject
```
3. Создаем приложениеЖ
```commandline
python3 manage.py startapp todo_list
```
4. Добавляем наименование приложения в список INSTALLED_APPS файла settings.py:
![install_app](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/install_app.png)
5. В файле urls.py приложения зададим переменной имя, которое будет использоваться в шаблоне и свяжем адреса страниц с функциями:
![app_url](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/app_url.png)
6. В корневом файле (проекта) urls.py сошлемся на файл urls.py приложения:
![project](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/project_urls.png)
7. Создадим модель Бд, будем использовать SQLite3:
![model_bd](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/model_bd.png)
8. Применим миграцию:
```
python3 manage.py migrate
python3 makemigrations
```
![makemigrations](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/migrations.png)
9. Визуально проверяем миграцию:
![migrations_control](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/migrations_control.png)
10. Проверяем БД:
![sqlite3](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/sqlite3.png)
11. Создадим в файле views.py классы для отображения списка заданий, добавления, удаления и изменения статуса (выполнено/не выполнено):
Эти вьюшки уже связаны с url (см. п. 5)
![views](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/views.png)
12. Создадим шаблоны:
- базовый (base.html)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}
        Base title
        {% endblock %}
    </title>
</head>
<body>
{% block body %}
base body
{% endblock %}
</body>
</html>
```
- для отображения списка заданий и изменения их статуса (todo_list.html):
```commandline
{% extends 'todo_list/base.html' %}


{% block title %}
ToDo List Django
{% endblock %}
{% block body %}
<h2>Hello Django ToDo List</h2>
<a href="{% url 'todo-list:create-item' %}">Add new todo</a>
<div>
    <ul>
        {% for todo in object_list %}
            <li>
                <form
                        style="display:inline;"
                        action="{% url 'todo-list:toggle-item' pk=todo.pk %}"
                        method = "post"
                >
                    {% csrf_token %}
                    <input type="submit" value="▶️">
                </form>
                {{ todo.text }}

                {% if todo.done %}
                    ✅
                {% else %}
                    🔘
                {% endif %}
                <a href="{% url 'todo-list:delete-item' pk=todo.pk %}">
                    ❌
                </a>
            </li>
        {% endfor %}
    </ul>
</div>
{% endblock %}
```
Первая строка - данные из этого шаблона подставляются в родительский base.html
Затем блок title, который также подставляется в родительский блок title
Блок body начинается с заголовка <h2>
Далее - контейнер <div>, внутри которого список (<ul>) заданий, загружаемых из БД с помощью цикла for
Внутри цикла элементы списка (<li>)
Также форма с элементами для смены статуса выполнения задания
Форма имеет защиту: {% csrf_token %}
Если пользователь кликает на эмодзи ▶️, то справа от наименования задания в списке эмодзи 🔘 и ✅ заменяют друг друга
Далее добавляется к строке задания интерактивный эмодзи ❌, клик которого вызывает функцию delete-item из views.py
- для добавления задачи (todoitem_form.html):
```commandline
{% extends 'todo_list/base.html' %}

{% block title %}
Create ToDo
{% endblock %}

{% block body %}
<h2>Hello Django ToDo List</h2>
<h3>Add new todo</h3>
<div>
    <Form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Add"/>
    </Form>
</div>
<div>
    <a href="{% url 'todo-list:items-list' %}">Back to items list</a>
</div>
{% endblock %}
```
- для удаления задачи из списка (todoitem_confirm.html):
```commandline
{% extends 'todo_list/base.html' %}

{% block title %}
Confirm delete Todo {{ object.id }}
{% endblock %}

{% block body %}
<h3>Are you sure you want to delete Todo {{ object.id }} with text '{{ object.text }}'</h3>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <a href="{% url 'todo-list:items-list' %}">Back to items list</a>
  <br>
  <input type="submit" value="Delete"/>
</form>
{% endblock %}
```
13. Запустим сервер и посмотрим, что получилось :
```commandline
python3 manage.py runserver
```
![runserver](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/runserver.png)
веб страница:
![page](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/page.png)
В базе данных:
![res_bd](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/res_bd.png)

