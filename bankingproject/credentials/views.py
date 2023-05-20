import email

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)

            user.save();
            return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def new_page(request):


    return render(request,'newpage.html')

def form_page(request):
    return render(request,'formpage.html')

def final_page(request):
    return render(request,'finalpage.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def back_to_home(request):
    auth.logout(request)
    return redirect('/')

def wiki_page(request,district):
    wikipedia_url="https://en.wikipedia.org/wiki/{}".format(district)
    return redirect(wikipedia_url)


from django.shortcuts import render

# Create your views here.
