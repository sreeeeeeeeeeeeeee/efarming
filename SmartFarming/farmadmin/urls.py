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
import farmer.views
import worker.views
import seller.views


urlpatterns = [
    path('', views.index, name='index'),
    path('baseindex', views.baseindex, name='baseindex'),
    path('base', views.basepage, name='base'),
    path('home', views.homepage, name='home'),
    path('signout', views.signout, name='signout'),
    path('aboutus1', views.aboutus1, name='aboutus1'),
    path('aboutus2', views.aboutus2, name='aboutus2'),
    path('basepurchase',views.basepurchase,name='basepurchase'),
    path('farmerlist',views.farmerlist,name='farmerlist'),
    path('workerlist',views.workerlist,name='workerlist'),
    path('sellerlist',views.sellerlist,name='sellerlist'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('viewtoolproduct',views.viewtoolproduct,name='viewtoolproduct'),
    path('viewpesticideproduct',views.viewpesticideproduct,name='viewpesticideproduct'),
    path('approvefarmeracc', views.approvefarmeracc, name='approvefarmeracc'),
    path('approvefarmer/<int:id>', views.approvefarmer, name='approvefarmer'),
    path('approveworkeracc', views.approveworkeracc, name='approveworkeracc'),
    path('approveworker/<int:id>', views.approveworker, name='approveworker'),
    path('approveselleracc', views.approveselleracc, name='approveselleracc'),
    path('approveseller/<int:id>', views.approveseller, name='approveseller'),
    path('logins', views.logins, name='logins'),
    path('customerpage', views.customerpage, name='customerpage'),
    path('registerfarmers',farmer.views.registerfarmers,name='registerfarmer'),
    path('registerworkers',worker.views.registerworkers,name='registerworker'),
    path('registersellers',seller.views.registersellers,name='registerseller'),
    path('customerdetail',views.customerdetail,name='customerdetail'),
    path('customerproductorderrequest/<int:id>',views.customerproductorderrequest,name='customerproductorderrequest'),
    path('customerpesticideorderrequest/<int:id>',views.customerpesticideorderrequest,name='customerpesticideorderrequest'),
    path('customermachineryorderrequest/<int:id>',views.customermachineryorderrequest,name='customermachineryorderrequest'),
    path('deletefarmer/<int:id>',views.deletefarmer,name='deletefarmer'),
    path('deleteworker/<int:id>',views.deleteworker,name='deleteworker'),
    path('deleteseller/<int:id>',views.deleteseller,name='deleteseller'),
    path('viewcustomerprofile/<int:id>',views.viewcustomerprofile,name='viewcustomerprofile'),
    path('editcustomerprofile/<int:id>',views.editcustomerprofile,name='editcustomerprofile'),
    path('viewmachineryorders/<int:id>',views.viewmachineryorders,name='viewmachineryorders'),
    path('viewproductorders/<int:id>',views.viewproductorders,name='viewproductorders'),
    path('cancelmachineryorder/<int:id>',views.cancelmachineryorder,name='cancelmachineryorder'),
    path('cancelproductorder/<int:id>',views.cancelproductorder,name='cancelproductorder'),
]

