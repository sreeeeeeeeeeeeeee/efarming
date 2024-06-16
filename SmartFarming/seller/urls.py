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
    path('baseseller', views.baseseller, name='baseseller'),
    path('base', views.base, name='base'),
    path('signout', views.signout, name='signout'),
    # path('viewsellingproduct', views.viewsellingproduct, name='viewsellingproduct'),
    path('viewrequests', views.viewrequest, name='viewrequests'),
    path('viewtoolorderrequests', views.viewtoolorderrequest, name='viewtoolorderrequests'),
    path('viewrenttoolrequest/<int:sid>', views.viewrenttoolrequest, name='viewrenttoolrequest'),
    path('sellingproduct/<int:id>',views.sellingproduct,name='sellingproduct'),
    path('viewproductlist/<int:id>',views.viewproductlist,name='viewproductlist'),
    path('viewsellerprofile/<int:id>',views.viewsellerprofile,name='viewsellerprofile'),
    path('editsellerprofile/<int:id>',views.editsellerprofile,name='editsellerprofile'),
    path('edittoolproduct/<int:id>',views.edittoolproduct,name='edittoolproduct'),
    path('accepttoolrequest/<int:id>',views.accepttoolrequest,name='accepttoolrequest'),
    path('acceptrentrequest/<int:id>',views.acceptrentrequest,name='acceptrentrequest'),
    path('viewproducts/<int:id>', views.viewproducts, name='viewproducts'),
    path('deletetool/<int:id>', views.deletetool, name='deletetool'),
    path('deletetoolrequest/<int:id>', views.deletetoolrequest, name='deletetoolrequest'),
    path('deleterentrequest/<int:id>', views.deleterentrequest, name='deleterentrequest'),
    path('renttool/<int:id>', views.renttool, name='renttool'),
    path('viewtoollist/<int:id>', views.viewtoollist, name='viewtoollist'),
    path('editrenttool/<int:id>', views.editrenttool, name='editrenttool'),
    path('deleterenttool/<int:id>', views.deleterenttool, name='deleterenttool'),
    path('sendproductrequests/<int:id>', views.sendproductrequests, name='sendproductrequests'),
    path('viewcustomerrequest/<int:sid>', views.viewcustomerrequest, name='viewcustomerrequest'),
    path('deletecustomerrequest/<int:id>',views.deletecustomerrequest,name='deletecustomerrequest'),
    path('acceptcustomerrequest/<int:id>',views.acceptcustomerrequest,name='acceptcustomerrequest'),
    path('viewsellerorder/<int:id>',views.viewsellerorder,name='viewsellerorder'),
    path('cancelsellerorder/<int:id>',views.cancelsellerorder,name='cancelsellerorder'),

]