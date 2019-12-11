"""kino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from kinoCRUD import views
# from .router import router


urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('kino/', views.KinoList.as_view()),
    path('kino/<int:pk>', views.KinoDetail.as_view()),
    path('kino/<int:pk>/sala/', views.SalaList.as_view()),
    path('film/', views.FilmList.as_view()),
    path('film/<int:pk>', views.FilmDetail.as_view()),
    path('kino/seans/', views.SeansList.as_view()),
    path('kino/seans/<int:pk>', views.SeansDetail.as_view()),
    path('sala/', views.SalaList.as_view()),
    path('sala/<int:pk>', views.SalaDetail.as_view()),
    path('miejsce/', views.MiejsceList.as_view()),
    path('miejsce/<int:pk>', views.MiejsceDetail.as_view()),
    path('zamowienie/bilet/', views.BiletList.as_view()),
    path('zamowienie/bilet/<int:pk>', views.BiletDetail.as_view()),
    path('zamowienie/', views.ZamowienieList.as_view()),
    path('zamowienie/<int:pk>', views.ZamowienieDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
