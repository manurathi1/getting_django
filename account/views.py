from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from .forms import UserRegistrationForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html' , {'section' : 'dashboard'})



def register(request):
    # if request.method == 'POST':
    #     user_form = UserRegistrationForm(request.POST)
    #     if user_form.is_valid():
    #         print(['-']^7 + 'form is valid')
    #         new_user = user_form.save(commit = False)
    #         new_user.set_password(user_form.cleaned_data['password'])
    #         # new_user.clean_password2()
    #         new_user.save()
    #         return render(request, 'account/register_done.html', {'new_user' : new_user})
    # else:
    #     user_form = UserRegistrationForm()
    #     return render(request, 'account/register.html', {'user_form' : user_form})

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = form.cleaned_data.get('username')
            messages.success(request, f'account created for { new_user }')
            # return render(request, 'account/register_done.html', {'new_user' : new_user})
            return redirect('dashboard')          
    else:   
        form = UserCreationForm()

    return render(request, 'account/register.html', {'user_form' : form})