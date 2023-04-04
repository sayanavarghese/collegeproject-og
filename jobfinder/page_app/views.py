from django.shortcuts import render,redirect
from .forms import userForm
from .forms import jobadderForm,ResumeForm
from .models import Profile,Job,Category,Resume,Application
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test
from .forms import JobForm
from django.http import HttpResponse
from django.core.paginator import Paginator


def is_user(user):     
    try:         
        return user.is_authenticated and (user.profile.user_type == 'USER')     
    except Profile.DoesNotExist:         
        return False      
def is_jobadder(user):     
     try:         
        return user.is_authenticated and (user.profile.user_type == 'JOB_ADDER' )     
     except Profile.DoesNotExist:         
        return False



# User
@user_passes_test(is_user,login_url='/user/login/')
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

@user_passes_test(is_user,login_url='/user/login/')
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
    check_apply = Application.objects.filter(applied_by=request.user)
    job_array=[]
    for i in check_apply:
        job_array.append(i.job)


    data ={
        "jobs":jobs,
        "page_obj":page_obj,
        "category":category,
        "job_array":job_array
    }
    return render(request,'jobseeker.html',data)

@user_passes_test(is_user,login_url='/user/login/')
def resume(request):
        res= None
        print(request.user)
        res=Resume.objects.filter(user=request.user)
        if res:
            return render(request,'resume.html',{'res':res[0]})
   
        else:
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
                    return redirect("/")

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
                    return redirect("/jobadder/home")
    else:
        form = AuthenticationForm()

    return render(request,'jobadderlogin.html',{'form':form})


@user_passes_test(is_jobadder,login_url='/jobadder/login/')
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
            profile.user_type = 'JOB_ADDER'
            profile.user = user
            profile.save()
            return redirect('jobadderlogin')

    else:
        form = jobadderForm()
    return render(request,'jobadderregister.html',{'form':form})


@user_passes_test(is_jobadder,login_url='/jobadder/login/')
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

@user_passes_test(is_jobadder,login_url='/jobadder/login/')
def jobadderhome(request):
    jobs = Job.objects.filter(added_by=request.user)
    pagination = Paginator(jobs,10)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    data ={
        "jobs":jobs,
        "page_obj":page_obj

    }
    return render(request,'jobadderhome.html',data)


def jobSeeker_view_job(request,id):

    job = Job.objects.get(id=id)
    check_apply = Application.objects.filter(applied_by=request.user)
    job_array=[]
    for i in check_apply:
        job_array.append(i.job)



    return render(request,'jobseekerviewjob.html',{'job':job,"job_array":job_array})

@user_passes_test(is_user,login_url='/user/login/')
def addresume(request):

    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            abc=form.save(commit=False)
            abc.user=request.user
            abc.save() 
            return redirect('resume')
    else:

        form=ResumeForm()
    return render(request,'add_resume.html',{'form':form})
    


@user_passes_test(is_user,login_url='/user/login/')
def apply_job(request,id):
    job = Job.objects.get(id=id)
    check_apply = Application.objects.filter(job=job).filter(applied_by=request.user)
    if not check_apply:
        Applied = Application()
        Applied.job = job
        Applied.applied_by = request.user
        Applied.save()
        return redirect('home')
    else:
        return HttpResponse("Job already Applied")


def applied_jobs(request,id):
    applications=Application.objects.filter(job=id)
    return render(request,'applied_jobs.html',{'applications':applications})


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
def add_resume(request):
     return render(request,'add_resume.html')
def viewresume(request):
     return render(request,'viewresume.html')



    

    

    
    
    
    
