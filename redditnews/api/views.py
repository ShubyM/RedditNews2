from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    # events = util.get_events("/r/news/?limit=100", util.get_token())
    # res = ""

    # for event in events:
    #     res += "<p>" + event + "</p>"


    return HttpResponse("<p> main </p>")







