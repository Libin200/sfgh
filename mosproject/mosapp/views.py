from django.shortcuts import render,redirect
from django.http import HttpResponse
from mosapp.models import email,email
from mosapp.form import emailform,emailform
from django.core.mail import send_mail
from mosproject import settings
# Create your views here.
def index(request):
    return render(request,'INDEX.html')
def home(request):
    if request.method=="POST":
        form=emailform(request.POST)
        if form.is_valid():
            try:
                form.save()
                to=form['email']
                sub='registration'
                msg='registered successfully'
                sen=send_mail(sub,msg,settings.EMAIL_HOST_USER,[to])
                return redirect('/view')
                
            except:
                form=emailform()
                return render(request,'b.html',{'form':form})
            
                
        else:
            form=emailform()
            return render(request,'b.html',{'form':form})
    form=emailform()
    return render(request,'b.html',{'form':form})

def view(request):
    datas=email.objects.all()
    return render(request,'view.html',{'datas':datas})

def edit(request,id):
    a=email.objects.get(employee_id=id)
    return render(request,'update.html',{'a':a})

def update(request,id):
    if request.method=='POST':
        id=email.objects.get(employee_id=id)
        form=emailform(request.POST,instance=id)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                return HttpResponse('jsbhfkds')

def destroy(request,id):
    a=email.objects.get(employee_id=id)
    a.delete()
    return redirect('/view')