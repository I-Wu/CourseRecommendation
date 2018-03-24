from django.shortcuts import render, render_to_response
from django.template import loader, Context

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
<<<<<<< HEAD
        recommend, description, class_type = Course.get_recommend((request.GET['keyword']))
        #description: (k, v) = (title, description)
        return render_to_response('recommend_list.html',locals())
        #return HttpResponse('Welcome!~' + request.GET['keyword'])
=======
        keyword = request.GET['keyword']

        # matches = Course.get_match(keyword)
        # if len(matches) > 0:
        #     recommend = Course.get_recommend(matches[0])

        recommend, descrip, types = Course.get_recommend_courses(keyword)

        #return render()
        return HttpResponse('Welcome!~' + request.GET['keyword'])
>>>>>>> c415a7d402b3e0aba1280359f7440814558879c9
    else:
        return HttpResponse('not allowed')
