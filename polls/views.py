from django.http import HttpResponse

def index(response):
    return HttpResponse('<h1>Polls Index</h1>')