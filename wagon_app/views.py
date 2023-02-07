from django.shortcuts import render

# Create your views here.
def wagon_app(request):
    return render (request, "index.html", {})
