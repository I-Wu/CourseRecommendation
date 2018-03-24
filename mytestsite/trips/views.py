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
        recommend, description, class_type = Course.get_recommend_courses((request.GET['keyword']))
        #description: (k, v) = (title, description)
        return render_to_response('recommend_list.html',locals())
        #return HttpResponse('Welcome!~' + request.GET['keyword'])
    else:
        return HttpResponse('No result!!!')

def get_places(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        #places = Place.objects.filter(city__icontains=q)
        print(q)
        results = Course.get_match(q)
        '''
        for pl in places:
            place_json = {}
            place_json = pl.city + "," + pl.state
            results.append(place_json)
        '''
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def test(request):
    return render(request, 'test.html')
