"""
URL configuration for Jewellery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import *
from FairyCraft.views import *
from FairyCraft.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_jewellery, name='main'),
    path('account', account, name='account'),
    path('chek', chek, name='chek'),
    path('katalog', katalog_view, name='katalog'),
    path('mastera', mastera_view, name='mastera'),
    path('api/master/<int:master_id>/products/', master_products_api, name='master_products_api'),
    path('master_katalog/<int:ID_user>', master_katalog, name="master_katalog"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)