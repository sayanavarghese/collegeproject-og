from django.shortcuts import render

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
    
