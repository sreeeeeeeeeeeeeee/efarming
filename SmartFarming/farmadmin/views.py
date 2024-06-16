from django.shortcuts import render
from .models import *
from .forms import *
from farmer.models import *
from worker.models import *
from seller.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def baseindex(request):
    return render(request,'index.html')
def basepage(request):
    return render(request,'base.html')
def homepage(request):
    return render(request,'dashboard.html')
def signout(request):
    return render(request,'signoutpage.html')
def aboutus1(request):
    return render(request,'aboutus1.html')
def aboutus2(request):
    return render(request,'aboutus2.html')
def basepurchase(request):
    return render(request,'basepurchase.html')
def logins(request):   
    form=loginForms() 
    email = request.POST.get('email')
    password = request.POST.get('password')
    if login.objects.filter(email=email,password=password).exists():
        userdetail=login.objects.get(email=email,password=password)
        if(userdetail.keyuser=='admin'):
            return render(request, 'base.html')
        elif(userdetail.keyuser=='farmer'):
            if farmerregister.objects.filter(email=email,password=password,status=1).exists():
                farmerobj=farmerregister.objects.get(email=email)
                request.session['userid']=farmerobj.id
                return render(request, 'farmer/basefarmer.html')
            else:
                return render(request,'login.html',{'form':form})
        elif(userdetail.keyuser=='worker'):
            if workerregister.objects.filter(email=email,password=password,status=1).exists():
                workerobj=workerregister.objects.get(email=email)
                request.session['userid']=workerobj.id            
                return render(request, 'worker/baseworker.html')
            else:
                return render(request,'login.html',{'form':form})
        elif(userdetail.keyuser=='seller'):
            if sellerregister.objects.filter(email=email,password=password,status=1).exists():
                sellerobj=sellerregister.objects.get(email=email)
                request.session['userid']=sellerobj.id
                return render(request, 'seller/baseseller.html')
            else:
                return render(request,'login.html',{'form':form})
        elif(userdetail.keyuser=='customer'):
            customerobj=customerdetails.objects.get(email=email)
            request.session['userid']=customerobj.id
            return render(request, 'basepurchase.html')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'login.html',{'form':loginForms})

def farmerlist(request):
    farmeracc = farmerregister.objects.filter(status=1)
    print(farmeracc)
    return render(request, 'viewfarmeraccounts.html', {'farmeracc': farmeracc})
def workerlist(request):
    workeracc = workerregister.objects.filter(status=1)
    print(workeracc)
    return render(request, 'viewworkeraccounts.html', {'workeracc': workeracc})
def sellerlist(request):
    selleracc = sellerregister.objects.filter(status=1)
    print(selleracc)
    return render(request, 'viewselleraccounts.html', {'selleracc': selleracc})

def approvefarmeracc(request):
    print("GFFFFFFFFFFF")
    user=farmerregister.objects.filter(status=0)
    print (user)
    return render(request,'approvefarmeraccounts.html',{'farmeracc':user})
def approvefarmer(request,id):
    farmerregister.objects.filter(id=id).update(status=1)
    """ keyuser="farmer"
    email=farmerregister.objects.filter(id=id).email
    password=farmerregister.objects.filter(id=id).password
    logindata=login(email=email,password=password,keyuser=keyuser)
    logindata.save() """
    user=farmerregister.objects.filter(status=0)
    return render(request,'approvefarmeraccounts.html',{'farmeracc':user})
def approveworkeracc(request):
    print("GFFFFFFFFFFF")
    user=workerregister.objects.filter(status=0)
    print (user)
    return render(request,'approveworkeraccounts.html',{'workeracc':user})
def approveworker(request,id):
    workerregister.objects.filter(id=id).update(status=1)
    user=workerregister.objects.filter(status=0)
    return render(request,'approveworkeraccounts.html',{'workeracc':user})
def approveselleracc(request):
    print("GFFFFFFFFFFF")
    user=sellerregister.objects.filter(status=0)
    print (user)
    return render(request,'approveselleraccounts.html',{'selleracc':user})
def approveseller(request,id):
    sellerregister.objects.filter(id=id).update(status=1)
    user=sellerregister.objects.filter(status=0)
    return render(request,'approveselleraccounts.html',{'selleracc':user})
def viewproduct(request):
    product = addProduct.objects.all()
    print(product)
    return render(request, 'viewproductpage.html', {'product': product})
def viewtoolproduct(request):
    toolproduct = sellingProducts.objects.filter(pcategory="tool")
    print(toolproduct)
    return render(request, 'viewmachinery.html', {'toolproduct': toolproduct})
def viewpesticideproduct(request):
    pestproduct = sellingProducts.objects.filter(pcategory="pesticide")
    print(pestproduct)
    return render(request, 'viewpesticide.html', {'pestproduct': pestproduct})
def customerdetail(request):
    if request.method=="GET":
        form=customerForms()
        return render(request, 'customerdata.html',{'form':form})
    else:
        print("inside post")
        form=customerForms(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            form.save()
            keyuser="customer"
            logindata=login(email=email,password=password,keyuser=keyuser)
            logindata.save()
            return render(request, 'login.html',{'form':loginForms})
        return render(request, 'basepurchase.html',{'form':form})
def customerproductorderrequest(request,id):
    print("inside get")
    if request.method=="GET":
        form=customerProductOrderRequestForms()
        return render(request, 'customerproductorder.html',{'form':form})
    else:
        print("inside post")
        form=customerProductOrderRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.customer_id_id=id
            form.save()
        return render(request, 'customerproductorder.html',{'form':form})
def customermachineryorderrequest(request,id):
    print("inside get")
    if request.method=="GET":
        form=customerMachineryOrderRequestForms()
        return render(request, 'customermachineryorder.html',{'form':form})
    else:
        print("inside post")
        form=customerMachineryOrderRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.customer_id_id=id
            form.save()
        return render(request, 'customermachineryorder.html',{'form':form})
def customerpesticideorderrequest(request,id):
    print("inside get")
    if request.method=="GET":
        form=customerMachineryOrderRequestForms()
        return render(request, 'customerpesticideorder.html',{'form':form})
    else:
        print("inside post")
        form=customerMachineryOrderRequestForms(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.customer_id_id=id
            form.save()
        return render(request, 'customerpesticideorder.html',{'form':form})
def viewcustomerprofile(request,id):
    profile=customerdetails.objects.filter(id=id)
    return render(request,'viewcustomerprofiles.html',{'profile':profile})
def deletefarmer(request,id):
    farmerregister.objects.filter(id=id).delete()
    return render(request,'base.html')
def deleteworker(request,id):
    workerregister.objects.filter(id=id).delete()
    return render(request,'base.html')
def deleteseller(request,id):
    sellerregister.objects.filter(id=id).delete()
    return render(request,'base.html')
def customerpage(request):
    return render(request,'customerfrontpage.html')
def editcustomerprofile(request,id):
    if(request.method=="GET"):
        center=customerdetails.objects.get(id=id)
        form=editcustomerForms(instance=center)
        return render(request,'editcustomerprofile.html',{'form':form})
    else:
        center=customerdetails.objects.get(id=id)
        form=editcustomerForms(instance=center)
        cname=request.POST.get('cname')
        phoneno=request.POST.get('phoneno')
        address=request.POST.get('address')
        email=request.POST.get('email')
        customerdetails.objects.filter(id=id).update(cname=cname,phoneno=phoneno,address=address,email=email)
        return render(request,'editcustomerprofile.html',{'form':form})
def viewmachineryorders(request,id):
    orderlist = customermachineryorder.objects.filter(customer_id_id=id,)
    print(orderlist)
    return render(request, 'viewmachineryorder.html', {'orderlist': orderlist})
def cancelmachineryorder(request,id):
    customermachineryorder.objects.filter(id=id).delete()
    return render(request,'viewmachineryorder.html')
def viewproductorders(request,id):
    orderlist = customerproductorder.objects.filter(customer_id_id=id,)
    print(orderlist)
    return render(request, 'viewproductorder.html', {'orderlist': orderlist})
def cancelproductorder(request,id):
    customerproductorder.objects.filter(id=id).delete()
    return render(request,'viewproductorder.html')