from django.shortcuts import render

from .models import AppUser

from .forms import AppUserForm

def AppUser_create_view(request):
    form = AppUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AppUserForm()
    context = {
        'form' : form 
    }    
    return render(request, "appUsers/appUser_create.html", context)