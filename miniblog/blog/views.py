from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm

# Create your views here.
#Home page
def home(request):
    return render(request, 'blog/home.html')

#About page 
def about(request):
    return render(request, 'blog/about.html')  

#Contact page 
def contact(request):
    return render(request, 'blog/contact.html') 

#Dashboard page 
def dashboard(request):
    return render(request, 'blog/dashboard.html')  

#User Logout page 
def user_logout(request):
   return HttpResponseRedirect('/')

#SingUp page 
def user_signup(request):
    form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

#Login page 
def user_login(request):
    form = LoginForm()
    return render(request, 'blog/login.html', {'form':form})    
