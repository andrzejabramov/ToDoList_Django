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
4. Добавляем наименование приложения в список Install_app файла settings.py:
![install_app](https://github.com/andrzejabramov/ToDoList_Django/blob/master/screens/install_app.png)
