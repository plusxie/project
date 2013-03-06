__author__ = 'xyb'

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse,Http404
import datetime


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    # current_date = datetime.datetime.now()
    current_date = datetime.datetime.now()
    hour_offset = 5
    next_time = datetime.datetime.now()
    return render_to_response('hours_ahead.html', locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    values.sort()
    # html = []
    # for k, v in values:
    #     html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return render_to_response('display_meta/single.txt', locals())