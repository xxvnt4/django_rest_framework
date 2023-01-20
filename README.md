# Django REST Framework

#### [1. Введение](#введение)
#### [2. Установка](#установка)
#### [3. Базовый класс APIView для представлений](#базовый-класс-apiview-для-представлений)
---

## ВВЕДЕНИЕ

[_YouTube_](https://youtu.be/i-uvtDKeFgE)

**Django REST Framework (DRF);**
- is a toolkit built on top of the Django web framework that reduces the amount of code you need to write to create REST interfaces;

- библиотека, которая работает со стандартными моделями Django для создания гибкого и мощного API для проекта;

**REST (Representational State Transfer, передача репрезентативного состояния) API;**

- is an architectural style for an application program interface (API) that uses HTTP requests to access and use data;

- способ создания API с помощью протокола HTTP;

**API (Application Programming Interface, программный интерфейс приложения);**

- is a set of definitions and protocols for building and integrating application software;

- совокупность инструментов и функций в виде интерфейса для создания новых приложений, благодаря которому одна программа будет взаимодействовать с другой;

--
  
на стороне сервера создается специальный программный интерфейс, Application Programming Interface (API)

DRF – инструмент для создания API c целью удаленного взаимодействия с ним




типовые задачи:  
  
- создание, чтение, изменение и удаление данных (CRUD);  
- проверка корректности передаваемых данных от клиента и защита от возможных хакерских атак;  
- авторизация и регистрация пользователей;  
- права доступа к данным через API

---

## УСТАНОВКА

[_YouTube_](https://youtu.be/EVrMbS14FdE)

```pip install djangorestframework```

добавить в переменную **INSTALLED_APPS** приложение **rest_framework**

```python
INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',
   'women.apps.WomenConfig',
   'rest_framework',
]
```

**women/views.py**

```python
from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer


class WomenAPIView(generics.ListAPIView):
   queryset = Women.objects.all()
   serializer_class = WomenSerializer
```

**women/serializers.py (вновь созданный)**

```python
from rest_framework import serializers
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
   class Meta:
       model = Women
       fields = ('title', 'cat_id')
```

**drfsite/urls.py**

```python
from django.contrib import admin
from django.urls import path
from women.views import WomenAPIView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/womenlist/', WomenAPIView.as_view())
]
```

**women/models.py**

```python
from django.db import models


class Women(models.Model):
   title = models.CharField(max_length=255)
   content = models.TextField(blank=True)
   time_create = models.DateTimeField(auto_now_add=True)
   time_update = models.DateTimeField(auto_now=True)
   is_published = models.BooleanField(default=True)
   cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

   def __str__(self):
       return self.title


class Category(models.Model):
   name = models.CharField(max_length=100, db_index=True)

   def __str__(self):
       return self.name
```

**women/admin.py**

```python
from django.contrib import admin
from .models import Women

admin.site.register(Women)
```
---

## БАЗОВЫЙ КЛАСС APIVIEW ДЛЯ ПРЕДСТАВЛЕНИЙ

[_YouTube_](https://youtu.be/HNqt2wZyKz4)

- Создание представления

```python
class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
```

- Создание сериализатора

```python
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id')
```

- Маршрутизация

```python
urlpatterns = [
    ...
    path('api/v1/womenlist/', WomenAPIView.as_view())
]
```

**women/views.py**

```python
class WomenAPIView(APIView):
# Класс APIView стоит во главе иерархии всех классов представления DRF.
# Представляет самый базовый функционал для работы различных классов представлений.
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
```
