from django.shortcuts import render
from .forms import AddPointsMap, AddMap
import pdb
from django.http import HttpResponse

def render_map(request):
    context = dict()
    #Verify if driver has a map
    if request.method == 'POST':
        form_create_map = AddMap(request.POST)
        if form_create_map.is_valid():
            form_create = form_create_map.save()
            context['form_points'] = form_create
            return render(request,'map.html',context)
        else:
            return render(request,'map.html',context)
    else:
        context['form_points'] = AddMap()
        return render(request,'map.html',context)