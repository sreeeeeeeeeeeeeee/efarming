"""SmartFarming URL Configuration

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
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('baseworker', views.baseworker, name='baseworker'),
    path('base', views.base, name='base'),
    path('signout', views.signout, name='signout'),
    path('viewjobrequests', views.viewjobrequest, name='viewjobrequests'),
    path('viewtoolpages', views.viewtoolpage, name='viewtoolpages'),
    path('machinarydetails', views.machinarydetails, name='machinarydetails'),
    path('viewjobrequest/<int:id>',views.viewjobrequest,name='viewjobrequest'),
    path('viewworkerprofile/<int:id>',views.viewworkerprofile,name='viewworkerprofile'),
    path('editworkerprofile/<int:id>',views.editworkerprofile,name='editworkerprofile'),
    path('acceptjob/<int:id>',views.acceptjob,name='acceptjob'),
    path('viewworkerorder/<int:id>',views.viewworkerorder,name='viewworkerorder'),
    path('cancelworkerorder/<int:id>',views.cancelworkerorder,name='cancelworkerorder'),
    path('viewproductorder/<int:id>',views.viewproductorder,name='viewproductorder'),
    path('cancelproductorder/<int:id>',views.cancelproductorder,name='cancelproductorder'),
    path('viewproduct/<int:id>',views.viewproduct,name='viewproduct'),
    path('deletejobrequest/<int:id>',views.deletejobrequest,name='deletejobrequest'),
    path('sendproductrequests/<int:id>',views.sendproductsrequests,name='sendproductrequests'),
    path('sendtoolorderrequests/<int:id>',views.sendtoolorderrequests,name='sendtoolorderrequests'),


]