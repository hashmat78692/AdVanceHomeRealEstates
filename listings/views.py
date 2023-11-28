import http

from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from listings.models import property_listing


def listings(request):
    properties_list = property_listing.objects.all().values();
    allListings = [{'name': "home", 'url': "http://.com"},
                   {'name': "home2", 'url': "http://.net"},
                   {'name': "home3", 'url': "http://.in"},
                   {'name': "home4", 'url': "http://.com"},
                   {'name': "home5", 'url': "http://.net"},
                   {'name': "home6", 'url': "http://.in"}]
    context = {
        "data": properties_list
    }
    return render(request, 'listings.html', context)


@csrf_exempt
def savelistings(request):
    if request.method == 'POST':
        listingData = request.POST.get("listingData")
        listingData_json = json.loads(listingData)
        propertyListing = property_listing()
        propertyListing.admin_id = 1;
        propertyListing.property_listing_date = listingData_json['listingDate']
        propertyListing.property_listing_street = listingData_json['addressStreet']
        propertyListing.property_listing_city = listingData_json['addressCity']
        propertyListing.property_listing_state = listingData_json['addressState']
        propertyListing.property_listing_zipcode = listingData_json['addressZipCode']
        propertyListing.property_listing_price = listingData_json['listingPrice']
        propertyListing.listing_description = listingData_json['listingDescription']
        propertyListing.property_listing_status = listingData_json['listingStatus']
        propertyListing.property_price_range_id = listingData_json['priceRange']
        propertyListing.property_neighbourhood_id= listingData_json['neighbourhood']
        propertyListing.property_type_id = listingData_json['propertyType']
        propertyListing.property_listing_is_featured = to_boolean(listingData_json['featuredPropertyIndicator'])
        propertyListing.save()
        context = {
            'new_article_id': property_listing.pk,
        }

    return HttpResponse("success")

def to_boolean(raw_value: str) -> bool:
    if not isinstance(raw_value, str):
        raw_value = str(raw_value)
    raw_value = raw_value.strip()
    return {'true': True, 'false': False}.get(raw_value.lower(), False)
@csrf_exempt
def saveImages(request):
    if request.method == "POST":
        f=request.FILES
        print(f)
        files = request.FILES.get('data', None)

        print(files)
        return JsonResponse({"Message": "File Uploaded Successfully"})
    return JsonResponse({"Message": ""})

@csrf_exempt
def editlistings(request,id):
    if request.method == "GET":
        property = property_listing.objects.filter(property_listing_id=id)
        print(property)
    data = serializers.serialize('json', property)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def deletelistings(request,id):
    if request.method == "DELETE":
        property_listing.objects.filter(property_listing_id=id).delete()

    return HttpResponse("success")