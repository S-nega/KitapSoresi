from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# def account(request, userid):
def account(request):
    if(request.GET):
        print(request.GET)

    return HttpResponse(f"<h1>Account Page</h1>")
    # return HttpResponse(f"<h1>Account Page</h1><p>{userid}</p>")

def archive(request, year):
    if int(year) > 2022:
        return redirect('account', permanent=True)
        # return redirect('/account/')
        # raise Http404()

    return HttpResponse(f"<h1>Archive by years</h1><p>{year}</p>")

def settingsPage(request, userid):
    return HttpResponse("Settings Page")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')

def accessDenied(request, exception):
    return HttpResponseNotFound('<h1>access is denied</h1>')

def unableRequest(request, exception):
    return HttpResponseNotFound('<h1>Unable Request</h1>')

def serviceError(request, exception):
    return HttpResponseNotFound('<h1>Service Error</h1>')

###