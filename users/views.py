from django.shortcuts import render, redirect
from .forms import UserRegisterForm 
from django.contrib.auth import login, authenticate
from testgateway.models import Profile, Userstats, Questions
# Create your views here.

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            new_user = form.cleaned_data['username']
            password2 = form.cleaned_data['password2']

            user = authenticate(username = new_user, password = password2)
            login(request, user)
            p = Profile(user =  user)
            p.save()
            for question in Questions.objects.all():
                Userstats.objects.create(userProfile = p, questions = question)
            return redirect('test_main')
            # return render(request, '', {'new_user' : new_user})


    else:

        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form' : form})






