from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 7314392b You're at the polls index.")