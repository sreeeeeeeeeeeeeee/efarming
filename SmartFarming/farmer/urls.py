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
    path('basefarmer', views.basefarmer, name='basefarmer'),
    path('signout', views.signout, name='signout'),
    path('viewtooldetails', views.viewtooldetail, name='viewtooldetails'),
    path('viewproductrequest/<int:fid>', views.viewproductrequest, name='viewproductrequest'),
    path('viewworkerdetail', views.viewworkerdetails, name='viewworkerdetail'),   
    path('addProducts/<int:id>',views.addProducts,name='addProducts'),
    path('productlist/<int:id>',views.productlist,name='productlist'),
    path('machinarylist',views.machinarylist,name='machinarylist'),
    path('rentmachinarylist',views.rentmachinarylist,name='rentmachinarylist'),
    path('pesticidelist',views.pesticidelist,name='pesticidelist'),
    path('workerdetails',views.workerdetails,name='workerdetails'),
    path('viewprofile/<int:id>',views.viewprofile,name='viewprofile'),
    path('editprofile/<int:id>',views.editprofile,name='editprofile'),
    path('editproduct/<int:id>',views.editproduct,name='editproduct'),
    path('sendjobrequests/<int:id>',views.sendjobrequests,name='sendjobrequests'),
    path('sendorderrequests/<int:id>',views.sendorderrequests,name='sendorderrequests'),
    path('sendrentrequests/<int:id>',views.sendrentrequests,name='sendrentrequests'),
    path('vieworder/<int:id>',views.vieworder,name='vieworder'),
    path('cancelorder/<int:id>',views.cancelorder,name='cancelorder'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),
    path('deleteproductrequest/<int:id>',views.deleteproductrequest,name='deleteproductrequest'),
    path('acceptproductrequest/<int:id>',views.acceptproductrequest,name='acceptproductrequest'),
]
