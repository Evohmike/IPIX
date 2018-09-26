from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

def ipix(request):
    title='Home'

    return render(request, 'ipix.html')
