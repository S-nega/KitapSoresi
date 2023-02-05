from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def messenger(request):
    return HttpResponse(f"<h1>Messenger Page</h1>")
###