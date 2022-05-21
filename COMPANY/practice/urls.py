"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import myapp.views
import staticapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.first),
    path('second/', myapp.views.second),
    # 'url명/' 으로 이런 이름 하에 있는 url은 '앱명.urls'를 통해 앱명/urls.py에서 관리해줄 겁니다.
    path('products/', include('product.urls')),
    path('boards/', include('board.urls')),
    path('staticapp/', staticapp.views.home),
]
