# school-backend API
A dynamic school management website 

</br>

# commands
```
commands: 

for development
-> export DJANGO_SETTINGS_MODULE=Teknipath.settings.development

for production
-> export DJANGO_SETTINGS_MODULE=Teknipath.settings.production

in wsgi change:
-> os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Teknipath.settings.production')

server deployment command / local deployment simulation [host running on http://127.0.0.1:8080/]
-> sudo docker-compose -f docker-compose-deploy.yml up --build

development [host running on http://127.0.0.1:8080/]
-> sudo docker-compose build && sudo docker-compose up

to activate virtual env in linux [not needed for production]
-> source ./Teknipath/venv/bin/activate
```

# Features

1. Blogs
2. Events
3. Messages notification
4. News and announcements
5. Testimonials
6. API for mobile apps

</br>

## requirements.txt
```
asgiref==3.2.10
autopep8==1.6.0
defusedxml==0.7.1
diff-match-patch==20200713
Django==3.1.1
django-cors-headers==3.5.0
django-enum-choices==2.1.2
django-filter==21.1
django-import-export==2.7.1
django-summernote==0.8.11.6
djangorestframework==3.13.1
djangorestframework-simplejwt==5.1.0
et-xmlfile==1.1.0
Markdown==3.3.6
MarkupPy==1.14
mysqlclient==2.1.0
odfpy==1.4.1
openpyxl==3.0.9
Pillow==9.1.0
pycodestyle==2.8.0
PyJWT==2.3.0
pytz==2022.1
PyYAML==6.0
sqlparse==0.4.2
tablib==3.2.1
toml==0.10.2
xlrd==2.0.1
xlwt==1.3.0
```
