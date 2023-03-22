from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userForm(UserCreationForm):
   def __init__(self, *args, **kwargs):         
      super(userForm, self).__init__(*args, **kwargs)
      self.fields['username'].help_text = ''          
      self.fields['email'].help_text = ''         
      self.fields['password1'].help_text = ''

   class Meta:
      model = User
      fields = ('username','email','password1','password2')
      

class jobadderForm(UserCreationForm):
   def __init__(self, *args, **kwargs):        
      super(jobadderForm, self).__init__(*args, **kwargs)  
      self.fields['username'].help_text = ''        
      self.fields['email'].help_text = ''         
      self.fields['password1'].help_text = ''

   class  Meta:
      model = User
      fields = ('username','email','password1','password2')