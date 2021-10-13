from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import UserModels
from .forms import UserRegisterForm

def addandshow(request):
    if request.method=='POST':
        fm=UserRegisterForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            res=UserModels(name=nm,email=em,password=pw)
            res.save()
            fm=UserRegisterForm()
    else:
        fm=UserRegisterForm()
        result=UserModels.objects.all()
    return render(request,'users/addandshow.html',{'form':fm,'result':result})

#function for edit/update
def update_data(request,id):
    if request.method=='POST':
        pi=UserModels.objects.get(pk=id)
        fm=UserRegisterForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=UserModels.objects.get(pk=id)
        fm=UserRegisterForm(instance=pi)
    return render(request,'users/update.html',{'form':fm})
# function for delete
def delete(request,id):
    if request.method=='POST':
        pi=UserModels.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')