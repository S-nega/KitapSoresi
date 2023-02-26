from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from messenger.models import Books


# Create your views here.
def index(request):
    books = Books.objects.all()
    return render(request, 'library/index.html', {'title': 'General leaf', 'books': books})


def categories(request, catid):
    return HttpResponse(f"<h1>Categories<br></h1>  <p>{catid}</p>")


def error400(request, exception):
    return render(request, 'library/errors/400.html', status=400)


def error403(request, exception):
    return render(request, 'library/errors/403.html', status=403)


def error404(request, exception):
    return HttpResponseNotFound('<h1>Page not found </h1>')


def error500(request):
    return render(request, 'library/errors/500.html', status=500)
