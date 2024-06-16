from django.shortcuts import render
from .models import *
from .forms import *
from farmadmin.models import *
from farmadmin.forms import *
from farmer.models import *

# Create your views here.
def index(request):
    return render(request,'seller/index.html')
def baseseller(request):
    return render(request,'seller/baseseller.html')
def signout(request):
    return render(request,'seller/signout.html')
def base(request):
    return render(request,'seller/base.html')
def registersellers(request):
    if request.method=="GET":
        form=sellerForms()
        return render(request, 'seller/registerseller.html',{'form':form})
    else:
        print("inside post")
        form=sellerForms(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
            keyuser="seller"
            logindata=login(email=email,password=password,keyuser=keyuser)
            logindata.save()
            return render(request, 'login.html',{'form':loginForms})
        return render(request, 'seller/registerseller.html',{'form':form})
def sellingproduct(request,id):
    print("inside get")
    if request.method=="GET":
        form=sellingProductForms()
        return render(request, 'seller/addtools.html',{'form':form})
    else:
        print("inside post")
        form=sellingProductForms(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.sellerregister_id_id=id
            form.save()
        return render(request, 'seller/addtools.html',{'form':form})
def renttool(request,id):
    print("inside get")
    if request.method=="GET":
        form=rentToolForms()
        return render(request, 'seller/addrenttools.html',{'form':form})
    else:
        print("inside post")
        form=rentToolForms(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.sellerregister_id_id=id
            form.save()
        return render(request, 'seller/addrenttools.html',{'form':form})
""" def viewsellingproduct(request):
    return render(request,'seller/viewtools.html') """
def viewrequest(request):
    return render(request,'seller/viewpurchaserequests.html')
def viewproductlist(request,id):
    toollist = sellingProducts.objects.filter(sellerregister_id_id=id)
    print(toollist)
    return render(request, 'seller/viewtools.html', {'toollist': toollist})
def viewtoollist(request,id):
    toolslist = rentTools.objects.filter(sellerregister_id_id=id)
    print(toolslist)
    return render(request, 'seller/viewrenttools.html', {'toolslist': toolslist})
def viewtoolorderrequest(request):
    toolreq = sendToolOrderRequest.objects.filter(status="pending")
    print(toolreq)
    return render(request, 'seller/viewpurchaserequests.html', {'toolreq': toolreq})
def viewrenttoolrequest(request,sid):
    rentlist=rentTools.objects.filter(sellerregister_id_id=sid).values_list('id')
    rentreq = sendRentRequest.objects.filter(toolid_id__in=rentlist, status="pending")
    print(rentreq)
    return render(request, 'seller/viewrentrequest.html', {'rentreq': rentreq})
def viewsellerprofile(request,id):
    profile=sellerregister.objects.filter(id=id)
    return render(request,'seller/viewprofiles.html',{'profile':profile})
def accepttoolrequest(request,id):
    sendToolOrderRequest.objects.filter(id=id).update(status="Accepted")
    jobreq=sendToolOrderRequest.objects.filter(status="pending")
    return render(request,'seller/baseseller.html',{'jobreq':jobreq})
def acceptrentrequest(request,id):
    sendRentRequest.objects.filter(id=id).update(status="Accepted")
    tid=sendRentRequest.objects.get(id=id)
    pid=tid.toolid_id
    tool=rentTools.objects.get(id=pid)
    nos=tool.nooftools
    no=nos-1
    rentTools.objects.filter(id=pid).update(nooftools=no)
    rentreq=sendRentRequest.objects.filter(status="pending")
    return render(request,'seller/baseseller.html',{'rentreq':rentreq})

def editsellerprofile(request,id):
    if(request.method=="GET"):
        center=sellerregister.objects.get(id=id)
        form=editsellerForms(instance=center)
        return render(request,'seller/editprofiles.html',{'form':form})
    else:
        center=sellerregister.objects.get(id=id)
        form=editsellerForms(instance=center)
        ownername=request.POST.get('ownername')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        shopname=request.POST.get('shopname')
        location=request.POST.get('location')
        email=request.POST.get('email')
        sellerregister.objects.filter(id=id).update(ownername=ownername,phoneno=phoneno,address=address,shopname=shopname,location=location,email=email)
        return render(request,'seller/editprofiles.html',{'form':form})

def edittoolproduct(request,id):
    if(request.method=="GET"):
        center=sellingProducts.objects.get(id=id)
        form=updatetoolForms(instance=center)
        request.session.toolid=center.id
        print("toolid=", request.session.toolid)
        return render(request,'seller/edittoolproduct.html',{'form':form})
    else:
        center=sellingProducts.objects.get(id=id)
        form=updatetoolForms(request.POST,request.FILES,instance=center)
        pname=request.POST.get('pname')
        pimage=request.FILES.get('pimage')
        description=request.POST.get('description')
        price=request.POST.get('price')
        status=request.POST.get('status')
        sellingProducts.objects.filter(id=id).update(pname=pname,pimage=pimage,description=description,price=price,status=status)
        return render(request,'seller/viewtools.html')

def viewproducts(request,id):
    prodlist = addProduct.objects.filter(status='available')
    print(prodlist)
    return render(request, 'seller/viewproducts.html', {'prodlist': prodlist})
def deletetool(request,id):
    sellingProducts.objects.filter(id=id).delete()
    return render(request,'seller/baseseller.html') 
def deletetoolrequest(request,id):
    sendToolOrderRequest.objects.filter(id=id).update(status="Rejected")
    return render(request,'seller/baseseller.html')
def deleterentrequest(request,id):
    sendRentRequest.objects.filter(id=id).update(status="Rejected")
    return render(request,'seller/baseseller.html')
def viewsellerorder(request,id):
    orderlist = sendproductRequest.objects.filter(userid=id,usertype="seller")
    print(orderlist)
    return render(request, 'seller/vieworders.html', {'orderlist': orderlist})
def cancelsellerorder(request,id):
    sendproductRequest.objects.filter(id=id).delete()
    return render(request,'seller/baseseller.html')
def editrenttool(request,id):
    if(request.method=="GET"):
        center=rentTools.objects.get(id=id)
        form=updaterentToolForms(instance=center)
        request.session.toolid=center.id
        print("toolid=", request.session.toolid)
        return render(request,'seller/editrenttools.html',{'form':form})
    else:
        center=rentTools.objects.get(id=id)
        form=updaterentToolForms(request.POST,request.FILES,instance=center)
        tname=request.POST.get('tname')
        timage=request.FILES.get('timage')
        description=request.POST.get('description')
        priceperday=request.POST.get('priceperday')
        nooftools=request.POST.get('nooftools')
        status=request.POST.get('status')
        rentTools.objects.filter(id=id).update(tname=tname,timage=timage,description=description,priceperday=priceperday,nooftools=nooftools,status=status)
        return render(request,'seller/viewrenttools.html')
def deleterenttool(request,id):
    rentTools.objects.filter(id=id).delete()
    return render(request,'seller/baseseller.html')

def sendproductrequests(request,id):
    print("inside get")
    if request.method=="GET":
        form=productRequestForms()
        return render(request, 'seller/sendproductrequest.html',{'form':form})
    else:
        print("inside post")
        form=productRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.sellerregister_id_id=id
            form.save()
        return render(request, 'seller/sendproductrequest.html',{'form':form})
    
def viewcustomerrequest(request,sid):
    print("hai",sid)
    toollist=sellingProducts.objects.filter(sellerregister_id_id=sid).values_list('id')
    custreq = customermachineryorder.objects.filter(product_id__in=toollist,status="pending")
    print(custreq)
    return render(request, 'seller/viewcustomerrequest.html', {'custreq': custreq})
def acceptcustomerrequest(request,id):
    customermachineryorder.objects.filter(id=id).update(status="Accepted")
    custreq=customermachineryorder.objects.filter(status="pending")
    return render(request,'seller/viewcustomerrequest.html',{'custreq':custreq})
def deletecustomerrequest(request,id):
    customermachineryorder.objects.filter(id=id).delete()
    return render(request,'seller/viewcustomerrequest.html')
