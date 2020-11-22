from django.shortcuts import render


# Create your views here.

def home(request):
    #title = 'Welcome: This is the home page'
    #first = 'This is my first django project'
    #context = {
        #"title" : title,
        #"h1" : first
    #}
    return render(request, "index.html")