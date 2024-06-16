from django.shortcuts import render
from .models import *
from .forms import *
from farmadmin.forms import *
from farmadmin.models import *
from seller.models import *
from farmer.models import *
from farmer.forms import *
from seller.forms import *

# Create your views here.
def index(request):
    return render(request,'worker/index.html')
def baseworker(request):
    return render(request,'worker/baseworker.html')
def signout(request):
    return render(request,'worker/signout.html')
def base(request):
    return render(request,'worker/base.html')
def viewjobrequest(request):
    return render(request,'worker/viewjobrequests.html')
def viewtoolpage(request):
    return render(request,'worker/viewtoolspage.html')
def registerworkers(request):
    if request.method=="GET":
        form=workerForms()
        return render(request, 'worker/registerworker.html',{'form':form})
    else:
        print("inside post")
        form=workerForms(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
            keyuser="worker"
            logindata=login(email=email,password=password,keyuser=keyuser)
            logindata.save()
            return render(request, 'login.html',{'form':loginForms})
        return render(request, 'worker/registerworker.html',{'form':form})
def machinarydetails(request):
    toollist = sellingProducts.objects.filter(pcategory="tool")
    print(toollist)
    return render(request, 'worker/viewmachinerypage.html', {'toollist': toollist})
def viewjobrequest(request,id):
    jobreq = sendJobRequest.objects.filter(workerid_id=id,status="pending")
    print(jobreq)
    return render(request, 'worker/viewjobrequests.html', {'jobreq': jobreq})
def viewworkerprofile(request,id):
    profile=workerregister.objects.filter(id=id)
    return render(request,'worker/viewprofiles.html',{'profile':profile})
def acceptjob(request,id):
    sendJobRequest.objects.filter(id=id).update(status="Accepted")
    jobreq=sendJobRequest.objects.filter(workerid_id=id,status="pending")
    return render(request,'worker/viewjobrequests.html',{'jobreq':jobreq})
def editworkerprofile(request,id):
    if(request.method=="GET"):
        center=workerregister.objects.get(id=id)
        form=editworkerForms(instance=center)
        return render(request,'worker/editprofiles.html',{'form':form})
    else:
        center=workerregister.objects.get(id=id)
        form=editworkerForms(instance=center)
        workername=request.POST.get('workername')
        age=request.POST.get('age')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        occupation=request.POST.get('occupation')
        experience=request.POST.get('experience')
        email=request.POST.get('email')
        workerregister.objects.filter(id=id).update(workername=workername,age=age,phoneno=phoneno,address=address,occupation=occupation,experience=experience,email=email)
        return render(request,'worker/editprofiles.html',{'form':form})

def viewworkerorder(request,id):
    orderlist = sendToolOrderRequest.objects.filter(userid=id,usertype="worker")
    print(orderlist)
    return render(request, 'worker/vieworders.html', {'orderlist': orderlist})
def cancelworkerorder(request,id):
    sendToolOrderRequest.objects.filter(id=id).delete()
    return render(request,'worker/baseworker.html')
def viewproductorder(request,id):
    orderlist = sendproductRequest.objects.filter(userid=id,usertype="worker")
    print(orderlist)
    return render(request, 'worker/viewproductorders.html', {'orderlist': orderlist})
def cancelproductorder(request,id):
    sendproductRequest.objects.filter(id=id).delete()
    return render(request,'worker/baseworker.html')
def viewproduct(request,id):
    prodlist = addProduct.objects.filter(status='available')
    print(prodlist)
    return render(request, 'worker/viewproducts.html', {'prodlist': prodlist})
def deletejobrequest(request,id):
    sendJobRequest.objects.filter(id=id).delete()
    return render(request,'worker/baseworker.html')
def sendproductsrequests(request,id):
    print("inside get")
    if request.method=="GET":
        form=productRequestForms()
        return render(request, 'worker/sendproductrequest.html',{'form':form})
    else:
        print("inside post")
        form=productRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.userid=id
            form.save()
        return render(request, 'worker/sendproductrequest.html',{'form':form})
def sendtoolorderrequests(request,id):
    print("inside get")
    if request.method=="GET":
        form=toolOrderRequestForms()
        return render(request, 'worker/sendtoolorderrequest.html',{'form':form})
    else:
        print("inside post")
        form=toolOrderRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.userid=id
            form.save()
        return render(request, 'worker/sendtoolorderrequest.html',{'form':form}) 