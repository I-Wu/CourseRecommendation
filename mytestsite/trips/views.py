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
        keyword = request.GET['keyword']

        # matches = Course.get_match(keyword)
        # if len(matches) > 0:
        #     recommend = Course.get_recommend(matches[0])

        recommend, descrip, types = Course.get_recommend_courses(keyword)

        #return render()
        return HttpResponse('Welcome!~' + request.GET['keyword'])
    else:
        return HttpResponse('not allowed')
