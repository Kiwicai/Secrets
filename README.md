# Secrets

##Python Version: 2.7
##Platform: Django 1.10
##Browser: Chrome
##OS: Mac OS X Yosemite 10.10.4

##Environment SetUp
1. If you don't have python, please install it. Before instsall python, you could install pip first. Make sure you are using python 2.7. This project works well with python 2.7
2. TODO: Install Django 1.10  
3. Clone Secrets project from git
4. Using your terminal to enter Secrets/webapps/, make sure you could see manage.py.
5. Then run this app by following instructions:
```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```
If you want to clean the database, run these instruction:
```
  python manage.py flush
```
Then run server again by
```
  python manage.py runserver
```
6. You could visit http://127.0.0.1:8000/ to see the UI. Registration,login, add new secret, update and delete secret are implemented.

##External sources:
[DjangoAdvancedTestTopic](https://docs.djangoproject.com/en/1.10/topics/testing/advanced/)  
