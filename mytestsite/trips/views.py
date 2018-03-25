from django.shortcuts import render, render_to_response
from django.template import loader, Context

# Create your views here.
from django.http import HttpResponse

from .models import Course

from datetime import datetime
import json


def home(request):
	#return HttpResponse("Hello World!")
	return render(request, 'hello_world.html', {
           'current_time': str(datetime.now()),
    })


def find_similarity(request):
    if 'keyword' in request.GET:
        course = Course.get_course((request.GET['keyword']))
        recommends = Course.get_recommend_courses((request.GET['keyword']))
        keyword = request.GET['keyword']
        if 't' in request.GET:
            t = request.GET['t']
        else:
            t = 0
        t_recommend = recommends[int(t)]
        print("comes here!!!")
        return render_to_response('recommend_list.html', locals())
    else:
        return HttpResponse('No result!!!')


def get_places(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        results = Course.get_match(q)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def test(request):
    return render(request, 'test.html')
