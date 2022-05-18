from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    print(request.META)
    return HttpResponse('<h1>Hello Class!</h1>')


def special(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }    
    return render(request, 'app/special.html', context)