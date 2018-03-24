from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse

from .models import Course

from datetime import datetime

def home(request):
	#return HttpResponse("Hello World!")
	return render(request, 'hello_world.html', {
           'current_time': str(datetime.now()),
    })

def find_similarity(request):
    if 'keyword' in request.GET:
        recommend = Course.get_recommend((request.GET['keyword']))
        #return render()
        return HttpResponse('Welcome!~' + request.GET['keyword'])
    else:
        return HttpResponse('not allowed')
