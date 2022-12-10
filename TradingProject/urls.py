"""TradingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from MainApp import views

from rest_framework import routers

from MainApp.views import Tradeviewset
router=routers.SimpleRouter()
router.register("Trade",Tradeviewset)
urlpatterns=router.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    #re_path('Trade/$',views.Trade,name='tradelist'),
    re_path('Trade/upload_data/$',views.upload_data,name='trade-upload-data'),
    #re_path('Trade/(?<pk>[^/.]+)/$',name='Trade-detail'),
]
