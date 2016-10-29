# Secrets

##Python Version: 2.7
##Platform: Django 1.10
##Browser: Chrome
##OS: Mac OS X Yosemite 10.10.4

## Why use Django framework?
Because Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It takes security issue into account such as CSRF, SQL injection, password encryption. It also provides useful features such as form validation.  

In this project, I use the default SQLite for data persistence.  

To get more information of Django, you could visit https://www.djangoproject.com/

##Environment SetUp
* If you don't have python, please install it. Before instsall python, you should install pip first. Make sure you are using python 2.7. This project works well with python 2.7
* Install Django 1.10  
```
  pip install Django==1.10.2
```
To verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import Django:
```
  >>>import django
  >>>print(django.get_version())
  1.10
```

* Clone Secrets project from git
* Use your terminal to enter Secrets/webapps/, make sure you could see manage.py.
* Then run this app by following instructions:
```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```
If you want to clean the database, run this instruction:
```
  python manage.py flush
```
Then run server again by
```
  python manage.py runserver
```

* You could visit http://127.0.0.1:8000/ to see the UI. Registration,login, add new secret, update and delete secret are implemented.

* Tests are implemented in Secrets/webapps/secrets/tests.py. To run the test file, make sure you are in Secrets/webapps/ so that you could see manage.py, then use the below instruction in terminal:  
```
  ./manage.py test secrets.tests
```
You will see OK in your console if all test cases passes.

##URLS
http://127.0.0.1:8000/  
The above link is for Login, if already login, redirect to http://127.0.0.1:8000/mySecrets/  

http://127.0.0.1:8000/register/    
http://127.0.0.1:8000/logout/  

http://127.0.0.1:8000/mySecrets/  
The above link is for showing login user's secrets. User could only see his/her own secrets.  

http://127.0.0.1:8000/updateSecret/SECRET_ID  
The above link is for updating user's one secret. User could only update his/her own secrets.  With GET, UI will show previous secret content. With POST, secret will be updated.

http://127.0.0.1:8000/deleteSecret/SECRET_ID  
The above link is for deleting login user's one secret. User could only delete his/her own secrets. 

##External sources:
[DjangoAdvancedTestTopic](https://docs.djangoproject.com/en/1.10/topics/testing/advanced/)  
