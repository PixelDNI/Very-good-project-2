"""
URL configuration for mylibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from library.views import show_start_page, show_add_rent_page, show_addreader_page, show_addbook_page, \
    show_showbooks_page, show_readers, show_rents, remove_book, remove_rent, remove_reader

urlpatterns = [
    path('', show_start_page),
    path('showbooks/', show_showbooks_page),
    path('addbook/', show_addbook_page),
    path('addreader/', show_addreader_page),
    path('addrent/', show_add_rent_page),
    path('admin/', admin.site.urls),
    path('showreaders/', show_readers),
    path('showrents/', show_rents),
    path('removebook/', remove_book),
    path('removereader/', remove_reader),
    path('removerent/', remove_rent),
]

