from django.shortcuts import render,redirect
from .forms import userForm
from .forms import jobadderForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test

def is_user(user):     
    try:         
        return user.is_authenticated and (user.profile.usertype == 'USER')     
    except Profile.DoesNotExist:         
        return False      
def is_jobadder(user):     
     try:         
        return user.is_authenticated and (user.profile.usertype == 'JOBADDER' )     
     except Profile.DoesNotExist:         
        return False

# Create your views here.
def home(request):
    return render(request,'home.html')
def resume(request):
    return render(request,'resume.html')
def jobSeeker(request):
    return render(request,'jobseeker.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeatyourpassword=request.POST.get('repeatyourpassword')
        print(firstname)
        print(lastname)
        print(email)
        print(password)
        print(repeatyourpassword)
    return render(request,'register.html')

def user_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if(user.profile.user_type == 'JOB_ADDER'):
                    return redirect("jobadderlogin")
                else:
                    return redirect("userhome")

    else:
        form = AuthenticationForm()

   
    return render(request,'userlogin.html',{'form':form})
def logout_user(request):
    logout(request)
    return redirect('userlogin')
def jobadder_login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if(user.profile.user_type == 'USER'):
                    return redirect("userlogin")
                else:
                    return redirect("jobadderhome")
    return render(request,'jobadderlogin.html',{'form':form})
@user_passes_test(is_user,login_url='/user/login/')
def userhome(request):
    return render(request,'userhome.html')
@user_passes_test(is_jobadder,login_url='/jobadder/login/')
def jobadderhome(request):
    return render(request,'jobadderhome.html')
def userregister(request):
    if request.method =='POST':
        form=userForm(request.POST)
        if form.is_valid():
            user=form.save()
            profile=Profile()
            profile.type='USER'
            profile.user=user
            profile.save()
            return redirect('userlogin')

    else:
        form = userForm()
    return render(request,'userregister.html',{'form':form})
def logout_jobadder(request):
    logout(request)
    return redirect('jobadderlogin')
def jobadderregister(request):
    if request.method =='POST':
        form = jobadderForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.type = 'JOB_ADDER'
            profile.user = user
            profile.save()
            return redirect('jobadderlogin')

    else:
        form = jobadderForm()
    return render(request,'jobadderregister.html',{'form':form})
    

    

    
    
    
    
