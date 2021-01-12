from django.shortcuts import render
from django.http import HttpResponse


from .util import *


# Create your views here.


def main(request):
    events = get_events("/r/news/?limit=100", get_token())
    res = ""

    for event in events:
        res += "<p> " + event + "</p>"

    return HttpResponse(res)

    
    




