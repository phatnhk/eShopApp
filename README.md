# eShopApp
Python Django

## 1. Khởi tạo dự án django với lệnh;
cách 1:
'''cmd: django-admin startproject mystore .'''
trong đó: mystore là tên project
cách 2:
'''cmd: python -m django startproject mystore .'''
## 2. Chạy dự án
'''cmd: python manage.py runserver 8080'''
trong đó: 8080 là port do mình đặt (mặc định 8000)\
## 3. Tạo app đầu tiên trong Python Django
'''cmd: python manage.py startapp home'''
## 4. Kết nối CSDL, ORM, MOdel, constraints
COnnect CSDL
Object Relational Mapping
Model
constraints

### 4.1. connect MySQL - install mysql
'''cmd: pip install mysqlclient'''

To upgrade python cli
'''cmd: python.exe -m pip install --upgrade pip'''


### settings.py
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/path/to/my.cnf",
        },
    }
}
```
Chạy lệnh migration đến table mystore trong mysql
'''cmd: python manage.py migrate'''

### 4.2. Object Relational Mapping
Khởi tạo model:
chạy lệnh migration:
Tạo ra SQL
'''cmd: python manage.py makemigrations'''
Thực thi vào db
'''cmd: python manage.py migrate'''




