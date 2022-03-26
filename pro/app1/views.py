from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import reg , login


def display(request):
    return render(request,'login.html')


def creation1(request):
    if(request.method=='POST'):
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['username']
        e = request.POST['password']
        data = reg.objects.create(Name=a,Roll_no=b,Age=c)
        data.save()
        data1 = login.objects.create(Username=d,Password=e)
        data1.save()
    return HttpResponse('registration completed')

def regis(request):
    return render(request,'registration.html')


def search1(request):
    if (request.method=='POST'):
        a = request.POST['n1']
        f = login.objects.filter(Username=a)
    return render(request,'viewtablereg.html',{'li':f})




def update1(request):
    if (request.method=='POST'):
        a = request.POST['n1']
        b = request.POST['n2']
        login.objects.filter(Username=a).update(Password=b)
    return HttpResponse('PASSWORD SUCCESSFULLY CHANGED')



def profile(request):
    if 'id' in request.session:
        return render(request, 'profile.html')
    else:
        return redirect(login1)
def login1(request):
    if (request.method=='POST'):
        a = request.POST['n1']
        b = request.POST['n2']
        data = login.objects.get(Username=a)
        if (data.Password==b):
            request.session['id'] = a
            return redirect(profile)

        else:
            return HttpResponse('LOGIN FAILED')
    else:
        return render(request,'login.html')

def logout(request):
    if 'id' in request.session:
        request.session.flush()
    return redirect(login1)


def list1(request):
    if (request.method=='POST'):
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        l=[]
        l.append(a)
        l.append(b)
        l.append(c)
    return render(request,'list.html',{'v':l})




