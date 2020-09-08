from django.shortcuts import render
from .forms import *

def register(request):
    formDriver = DriverForm(request.POST)
    formUser = UserDriver(request.POST)
    
    if request.method == "POST":
        if formDriver.is_valid() and formUser.is_valid():
            try:
                postUser = formUser.save()
                postDriver = formDriver.save(commit=False)
                postDriver.driver_id = postUser
                postDriver.save()
            except:
                print('deu merda aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

    
    return render(request, 'register.html', {'formDriver': formDriver, 'formUser': formUser})