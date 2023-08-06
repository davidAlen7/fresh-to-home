
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm



# Create your views here.



def signup(request):
    form=UserCreationForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
  
            user=authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})


def loginview(request):
    uname=request.POST.get('username')
    pwd=request.POST.get('password')
    user=authenticate(request,username=uname,password=pwd)
    
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        return render(request,'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')
