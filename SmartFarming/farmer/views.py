from django.shortcuts import render
from .models import *
from .forms import *
from farmadmin.models import *
from farmadmin.forms import *
from seller.models import *
from worker.models import *

# Create your views here.
def index(request):
    return render(request,'farmer/index.html')
def basefarmer(request):
    return render(request,'farmer/basefarmer.html')
def signout(request):
    return render(request,'farmer/signout.html')
def registerfarmers(request):
    form=farmerForms()
    return render(request, 'farmer/registerfarmer.html',{'form':form})
def registerfarmers(request):
    if request.method=="GET":
        form=farmerForms()
        return render(request, 'farmer/registerfarmer.html',{'form':form})
    else:
        print("inside post")
        form=farmerForms(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
            keyuser="farmer"
            logindata=login(email=email,password=password,keyuser=keyuser)
            logindata.save()
            return render(request, 'login.html',{'form':loginForms})
        return render(request, 'farmer/registerfarmer.html',{'form':form})
def viewtooldetail(request):
    return render(request,'farmer/viewtoolsdetails.html')
def viewproductrequest(request,fid):
    print("hai",fid)
    prodlist=addProduct.objects.filter(farmerregister_id_id=fid).values_list('id')
    prodreq = customerproductorder.objects.filter(product_id__in=prodlist, status="pending")
    print(prodreq)
    return render(request, 'farmer/viewproductrequest.html', {'prodreq': prodreq})
def acceptproductrequest(request,id):
    customerproductorder.objects.filter(id=id).update(status="Accepted")
    prodreq=customerproductorder.objects.filter(status="pending")
    return render(request,'farmer/viewproductrequest.html',{'prodreq':prodreq})
def deleteproductrequest(request,id):
    customerproductorder.objects.filter(id=id).update(status="Rejected")
    return render(request,'farmer/viewproductrequest.html')
def viewworkerdetails(request):
    return render(request, 'farmer/viewworkerprofile.html')
def addProducts(request,id):
    print("inside get")
    if request.method=="GET":
        form=addProductForms()
        return render(request, 'farmer/addproducts.html',{'form':form})
    else:
        print("inside post")
        form=addProductForms(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.farmerregister_id_id=id
            form.save()
        return render(request, 'farmer/addproducts.html',{'form':form})
def productlist(request,id):
    prodlist = addProduct.objects.filter(farmerregister_id_id=id)
    print(prodlist)
    return render(request, 'farmer/viewproducts.html', {'prodlist': prodlist})
def machinarylist(request):
    toollist = sellingProducts.objects.filter(pcategory="tool")
    print(toollist)
    return render(request, 'farmer/viewtoolsdetails.html', {'toollist': toollist})
def rentmachinarylist(request):
    toolslist = rentTools.objects.all()
    print(toolslist)
    return render(request, 'farmer/viewtoolsforrent.html', {'toolslist': toolslist})
def pesticidelist(request):
    pestlist = sellingProducts.objects.filter(pcategory="pesticide")
    print(pestlist)
    return render(request, 'farmer/viewpesticidedetails.html', {'pestlist': pestlist})
def workerdetails(request):
    workerdet = workerregister.objects.filter(status=1)
    print(workerdet)
    return render(request, 'farmer/viewworkerprofile.html', {'workerdet': workerdet})
def sendjobrequests(request,id):
    print("inside get")
    if request.method=="GET":
        form=jobRequestForms()
        return render(request, 'farmer/sendjobrequest.html',{'form':form})
    else:
        print("inside post")
        form=jobRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.farmerregister_id_id=id
            form.save()
        return render(request, 'farmer/sendjobrequest.html',{'form':form}) 
def sendorderrequests(request,id):
    print("inside get")
    if request.method=="GET":
        form=toolOrderRequestForms()
        return render(request, 'farmer/sendorderrequest.html',{'form':form})
    else:
        print("inside post")
        form=toolOrderRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            #obj.userid=id
            form.save()
        return render(request, 'farmer/sendorderrequest.html',{'form':form}) 
def sendrentrequests(request,id):
    print("inside get")
    if request.method=="GET":
        form=rentRequestForms()
        return render(request, 'farmer/sendrentrequest.html',{'form':form})
    else:
        print("inside post")
        form=rentRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.farmerregister_id_id=id
            form.save()
        return render(request, 'farmer/sendrentrequest.html',{'form':form}) 
def viewprofile(request,id):
    profile=farmerregister.objects.filter(id=id)
    return render(request,'farmer/viewprofiles.html',{'profile':profile})

def editprofile(request,id):
    if(request.method=="GET"):
        center=farmerregister.objects.get(id=id)
        form=editprofileForms(instance=center)
        return render(request,'farmer/editprofiles.html',{'form':form})
    else:
        center=farmerregister.objects.get(id=id)
        form=editprofileForms(instance=center)
        farmername=request.POST.get('farmername')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        email=request.POST.get('email')
        farmerregister.objects.filter(id=id).update(farmername=farmername,phoneno=phoneno,address=address,email=email)
        return render(request,'farmer/editprofiles.html',{'form':form})

def editproduct(request,id):
    if(request.method=="GET"):
        center=addProduct.objects.get(id=id)
        form=updateProductForms(instance=center)
        request.session.prodid=center.id
        print("prodid=", request.session.prodid)
        return render(request,'farmer/editproduct.html',{'form':form})
    else:
        center=addProduct.objects.get(id=id)
        form=updateProductForms(request.POST,request.FILES,instance=center)
        productname=request.POST.get('productname')
        productimage=request.FILES.get('productimage')
        description=request.POST.get('description')
        price=request.POST.get('price')
        status=request.POST.get('status')
        addProduct.objects.filter(id=id).update(productname=productname,productimage=productimage,description=description,price=price,status=status)
        return render(request,'farmer/basefarmer.html')

def vieworder(request,id):
    orderlist = sendToolOrderRequest.objects.filter(userid=id, usertype="farmer")
    print(orderlist)
    return render(request, 'farmer/vieworders.html', {'orderlist': orderlist})
def deleteproduct(request,id):
    addProduct.objects.filter(id=id).delete()
    return render(request,'farmer/basefarmer.html')
def cancelorder(request,id):
    sendToolOrderRequest.objects.filter(id=id).delete()
    return render(request,'farmer/basefarmer.html')