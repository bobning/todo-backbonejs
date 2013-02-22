import json
import time

from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from todos.models import Todos


def index(request):
    return render_to_response('index.html', RequestContext(request, {}))

def todos(request, id=None):
    if 'GET' == request.method:
        objs = Todos.objects.all()
        items = []
        for obj in objs:
            i = {'id': obj.pk, 'title': obj.title, 'done': obj.done}
            items.append(i)
        return HttpResponse(json.dumps(items), content_type='application/json')
    elif 'DELETE' == request.method:
        obj = Todos.objects.get(pk=int(id))
        obj.delete()
        return HttpResponse()
    elif 'POST' == request.method:
        data = json.loads(request.raw_post_data)
        title = data.get('title')
        done = data.get('done')
        Todos.objects.create(title=title, done=done)
        return HttpResponse()
    elif 'PUT' == request.method:
        data = json.loads(request.raw_post_data)
        obj = Todos.objects.get(id=data['id'])
        obj.title = data['title']
        obj.done = data['done']
        obj.save()
        return HttpResponse()
