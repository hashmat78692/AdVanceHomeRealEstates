
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from listings.models import property_listing
from listings.models import property_neighbourhood
from listings.models import property_type
from listings.models import property_price_range


def listings(request):
    properties_list = property_listing.objects.all().values()
    propertyTypeList = property_type.objects.all().values()
    neighbourhoodList = property_neighbourhood.objects.all().values()
    propertyPriceRangeList = property_price_range.objects.all().values()


    context = {
        "data": properties_list,
        "propertyTypeList":propertyTypeList,
        "neighbourhoodList":neighbourhoodList,
        "propertyPriceRangeList":propertyPriceRangeList
    }
    return render(request, 'listings.html', context)


@csrf_exempt
def savelistings(request):
    if request.method == 'POST':
        listingData = request.POST['listingData']
        listingData_json = json.loads(listingData)
        id = listingData_json['proprtyId']
        print(id)
        if id is not None:
            print(id)
            property = property_listing.objects.get(property_listing_id=id)
            property.admin_id = 1;
            property.property_listing_date = listingData_json['listingDate']
            property.property_listing_street = listingData_json['addressStreet']
            property.property_listing_city = listingData_json['addressCity']
            property.property_listing_state = listingData_json['addressState']
            property.property_listing_zipcode = listingData_json['addressZipCode']
            property.property_listing_price = listingData_json['listingPrice']
            property.listing_description = listingData_json['listingDescription']
            property.property_listing_status = listingData_json['listingStatus']
            property.property_price_range_id = listingData_json['priceRange']
            property.property_neighbourhood_id = listingData_json['neighbourhood']
            property.property_type_id = listingData_json['propertyType']
            property.property_listing_is_featured = to_boolean(listingData_json['featuredPropertyIndicator'])
            property.save()
            return HttpResponse("edited")
        else:
            print(listingData)
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            image3 = request.FILES['image3']
            image4 = request.FILES['image4']

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
            propertyListing.property_listing_pic1 = image1
            propertyListing.property_listing_pic2 = image2
            propertyListing.property_listing_pic3 = image3
            propertyListing.property_listing_pic4 = image4
            propertyListing.save()

            return HttpResponse("success")

def to_boolean(raw_value: str) -> bool:
    if not isinstance(raw_value, str):
        raw_value = str(raw_value)
    raw_value = raw_value.strip()
    return {'true': True, 'false': False}.get(raw_value.lower(), False)

@csrf_exempt
def editlistings(request,id):
    if request.method == "GET":
        property = property_listing.objects.filter(property_listing_id=id)
        print(property)
    data = serializers.serialize('json', property)
    print(data)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def deletelistings(request,id):
    if request.method == "DELETE":
        property_listing.objects.filter(property_listing_id=id).delete()

    return HttpResponse("success")