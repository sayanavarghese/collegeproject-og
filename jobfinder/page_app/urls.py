from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('resume/',views.resume,name='resume'),
    path('jobSeeker/',views.jobSeeker,name='jobseeker'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('user/login/',views.user_login,name='userlogin'),
    path('jobadder/login/',views.jobadder_login,name='jobadderlogin'),
    path('user/home/',views.userhome,name='userhome'),
    path('jobadder/home/',views.jobadderhome,name='jobadderhome'),
    path('user/register/',views.userregister,name='userregister'),
    path('jobadder/register/',views.jobadderregister,name='jobadderregister'),
    path('user/logout/',views.logout_user,name='logout_user'),
    path('jobadder/logout/',views.logout_jobadder,name='logout_jobadder'),
     
    
    
      
      
    

]
