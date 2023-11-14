import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def listings(request):
    allListings = [{'name': "home", 'url': "http://.com"},
                   {'name': "home2", 'url': "http://.net"},
                   {'name': "home3", 'url': "http://.in"},
                   {'name': "home4", 'url': "http://.com"},
                   {'name': "home5", 'url': "http://.net"},
                   {'name': "home6", 'url': "http://.in"}]
    context = {
        "data": allListings
    }
    return render(request, 'listings.html', context)


@csrf_exempt
def savelistings(request):
    dataBack = {'a': "success"}
    if request.method == 'POST':
        data = json.load(request)
        print(data)

    return JsonResponse(dataBack)
