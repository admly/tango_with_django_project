from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'> About</a>.")

def about(request):
    return HttpResponse("Rango says there is about page! <br/> <a href='/rango/'> Index</a>.")
