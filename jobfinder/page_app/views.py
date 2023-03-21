from django.shortcuts import render,redirect
from .forms import userForm
from .forms import jobadderForm
from .models import Profile

# Create your views here.
def home(request):
    return render(request,'home.html')
def resume(request):
    return render(request,'resume.html')
def jobSeeker(request):
    return render(request,'jobseeker.html')
def login(request):
    return render(request,'login.html')
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
    return render(request,'userlogin.html')
def jobadder_login(request):
    return render(request,'jobadderlogin.html')
def userhome(request):
    return render(request,'userhome.html')
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
    

    

    
    
    
    
