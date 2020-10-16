from django.shortcuts import render
from .forms import UserRegisterForm 
# Create your views here.

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()
            new_user = form.cleaned_data['username']

            return render(request, 'users/register_done.html', {'new_user' : new_user})


    else:

        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form' : form})






