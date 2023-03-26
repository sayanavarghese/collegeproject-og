from django.shortcuts import render,redirect
from .forms import userForm
from .forms import jobadderForm
from .models import Profile,Job,Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
from .forms import JobForm
from django.core.paginator import Paginator


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



# User
def home(request):
    if request.method == 'POST':
        search  = request.POST['search']
        return redirect(f'/jobSeeker?search={search}')
    categories = Category.objects.all()[:5]
    list_categories = Category.objects.all()
    data ={
        "categories":categories,
        "list_categories":list_categories
    }

    return render(request,'home.html',data)

def jobSeeker(request):
    categoryID = request.GET.get('category')
    search = request.GET.get('search')
    if categoryID:
        jobs = Job.objects.filter(category=categoryID)
        category = Category.objects.filter(id=categoryID)[0]
    elif search:
        jobs = Job.objects.filter(position__contains=search)
        category = None
    else:
        jobs = Job.objects.all()
        category = None
    pagination = Paginator(jobs,10)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    data ={
        "jobs":jobs,
        "page_obj":page_obj,
        "category":category
    }
    return render(request,'jobseeker.html',data)

def resume(request):
    return render(request,'resume.html')


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

def add_job(request):
    if request.method == 'POST':
        job_form = JobForm(request.POST,request.FILES)
        if job_form.is_valid():
            job= Job()
            job.title = job_form.cleaned_data['title']
            job.position = job_form.cleaned_data['position']
            job.category =job_form.cleaned_data['category']
            job.location = job_form.cleaned_data['location']
            job.description = job_form.cleaned_data['description']
            job.salary = job_form.cleaned_data['salary']
            job.added_by = request.user
            job.save()
            return redirect('jobadderhome')
    else:
        job_form = JobForm()

    data ={
        "job_form":job_form
    }
    return render(request,'jobadder_addjob.html',data)

def jobadderhome(request):
    jobs = Job.objects.all()
    pagination = Paginator(jobs,10)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    data ={
        "jobs":jobs,
        "page_obj":page_obj

    }
    return render(request,'jobadderhome.html',data)




def it_job(request):
     return render(request,'itjob.html')
def Aviation(request):
     return render(request,'Aviation.html')
def Medical (request):
     return render(request,'Medical.html')
def Hotel_Management(request):
     return render(request,'hotelmanagement.html')
def Engineering(request):
     return render(request,'Engineering.html')
def Dress_Design(request):
     return render(request,'Dress Design.html')

    

    

    
    
    
    
