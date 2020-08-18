from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import Account
from django.contrib.auth import login as auth_login, authenticate
from .form import RegistrationForm, LoginForm,RegistrationUserForm,ContactForm
from django.shortcuts import get_object_or_404
from prince_gym.decorator import login_register_check
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home(request):
    return render(request,'prince_gym.html')


@login_register_check()
def login(request):
    user = request.user
    # if user.is_authenticated:
    #     return redirect("gym:home")

    form = AuthenticationForm(data=request.POST or None)
    print(request.method,form.is_valid())
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('gym:home')

    param = {
        'form':form,
    }

    return render(request, "login.html", param)

    # if request.POST:
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = request.POST['name']
    #         password = request.POST['password']
    #         user = auth.authenticate(username=username, password=password)
    #         print(user,username,password )
    #         if user:
    #             auth_login(request, user)
    #             return redirect("gym:home")

    # else:
    #     form = LoginForm()
    # param ={'form':form}
    # return render(request, "login.html", param)

@login_register_check()
def register(request):
    user = request.user
    form = RegistrationUserForm(request.POST or None)
    c_form = RegistrationForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid() and c_form.is_valid():
            user = form.save()
            user.account.email = c_form.cleaned_data.get('email')
            user.account.contact = c_form.cleaned_data.get('contact')
            user.account.save()  
            # c_form.save()
            return redirect('gym:login')

    param = {
        'form':form,
        'c_form':c_form
    }
    return render (request,'sign_up.html',param)

    # if user.is_authenticated:
    #     return redirect("gym:home")
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     print(form.is_valid())
    #     if form.is_valid():
    #         form.save()
    #         name = form.cleaned_data.get('name')
    #         email = form.cleaned_data.get('email')
    #         password1 = form.cleaned_data.get('password')
    #         password2 = form.cleaned_data.get('confirm_Password')
    #         if password1 == password2:
    #             if User.objects.filter(username=name).exists():
    #                 messages.info(request, 'Username Taken')
    #                 return redirect('gym:register')
    #             elif User.objects.filter(email=email).exists():
    #                 messages.info(request, 'Email Id Taken')
    #                 return redirect('gym:register')
    #             else:
    #                 new_user = User.objects.create_user(
    #                     username=name, email=email, password=password1)
    #                 new_user.save()
    #                 return redirect('gym:login')
    #         else:
    #             messages.info(request, 'Password not match')
    #             return redirect('gym:register')
    # else:
    #     form = RegistrationForm()
    # return render(request, 'sign_up.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect("/")


def galary(request):
    return render(request,'galary.html')


def about_us(request):
    return render(request,'about_us.html')



def contact(request):
    form = ContactForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gym:home')

    param = {
        'form':form,
    }

    return render(request,'contact_us.html',param)