from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image,Location,Category
# Create your views here.

def ipix(request):
    title='Home'
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'index.html',{'title':title,'images':images,'locations':locations})


def location_filter(request, location):
    locations = Location.objects.all()
    images = Image.filter_by_location(location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations})




def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        images_found = Image.search_image
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'images':images_found})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})

