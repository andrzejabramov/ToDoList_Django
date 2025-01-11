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
10. Запустим сервер и посмотрим, что получилось :
```commandline
python3 manage.py runserver
```
