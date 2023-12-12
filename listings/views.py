
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
    properties_list = property_listing.objects.filter(property_listing_status=('active')).values()
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
        print(request.POST)
        if id !='':
            print(id)
            property = property_listing.objects.get(property_listing_id=id)
            property.admin_id = 1
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

            try:
                image1 = request.POST['image1']
            except:
                image1 = request.FILES['image1']

            try:
                image2 = request.POST['image2']
            except:
                image2 = request.FILES['image2']

            try:
                image3 = request.POST['image3']
            except:
                image3 = request.FILES['image3']

            try:
                image4 = request.POST['image4']
            except:
                image4 = request.FILES['image4']

            if image1 != 'undefined':
                print("not undefined Image 1")
                property.property_listing_pic1 = image1
            if image2 != 'undefined':
                print("not undefined Image 2")
                property.property_listing_pic2 = image2
            if image3 != 'undefined':
                print("not undefined Image 3")
                property.property_listing_pic3 = image3
            if image4 != 'undefined':
                print("not undefined Image 4")
                property.property_listing_pic4 = image4

            property.save()
            return HttpResponse("edited")
        else:
            print(listingData)
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            image3 = request.FILES['image3']
            image4 = request.FILES['image4']
            propertyListing = property_listing()
            propertyListing.admin_id = 1
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
        property = property_listing.objects.filter(property_listing_id=id)
        property.property_listing_status = "Inactive"
        property.save()
    return HttpResponse("success")



def detailview(request, id):
    prop = property_listing.objects.get(property_listing_id=id)
    context = {'item': prop}
    return render(request, 'detailedView.html', context)

@csrf_exempt
def filterlisting(request):
    if request.method == "GET":
        priceRangeFilter = request.GET['priceRangeFilter']
        propertyTypeFilter = request.GET['propertyTypeFilter']
        neighbourhoodFilter = request.GET['neighbourhoodFilter']
        print(priceRangeFilter)
        print(propertyTypeFilter)
        print(neighbourhoodFilter)

        if propertyTypeFilter == "noPropertyType" and priceRangeFilter != "noPriceRange" and neighbourhoodFilter == "noNeighbourhood":
            properties_list = property_listing.objects.filter(property_price_range_id=priceRangeFilter).values()

        if propertyTypeFilter == "noPropertyType" and priceRangeFilter == "noPriceRange" and neighbourhoodFilter != "noNeighbourhood":
            properties_list = property_listing.objects.filter(property_neighbourhood_id=neighbourhoodFilter).values()

        if propertyTypeFilter != "noPropertyType" and priceRangeFilter == "noPriceRange" and neighbourhoodFilter == "noNeighbourhood":
            properties_list = property_listing.objects.filter(property_type_id=propertyTypeFilter).values()

        if propertyTypeFilter != "noPropertyType" and priceRangeFilter != "noPriceRange" and neighbourhoodFilter != "noNeighbourhood":
            properties_list = property_listing.objects.filter(property_price_range_id=priceRangeFilter,property_type_id=propertyTypeFilter, property_neighbourhood_id=neighbourhoodFilter).values()

        if propertyTypeFilter != "noPropertyType" and priceRangeFilter != "noPriceRange" and neighbourhoodFilter == "noNeighbourhood":
            properties_list = property_listing.objects.filter(property_price_range_id=priceRangeFilter,property_type_id=propertyTypeFilter).values()

        if propertyTypeFilter == "noPropertyType" and priceRangeFilter != "noPriceRange" and neighbourhoodFilter != "noNeighbourhood":
            properties_list = property_listing.objects.filter(property_price_range_id=priceRangeFilter,property_neighbourhood_id=neighbourhoodFilter).values()

        if propertyTypeFilter != "noPropertyType" and priceRangeFilter == "noPriceRange" and neighbourhoodFilter != "noNeighbourhood":
            properties_list = property_listing.objects.filter(property_type_id=propertyTypeFilter,property_neighbourhood_id=neighbourhoodFilter).values()

        propertyTypeList = property_type.objects.all().values()
        neighbourhoodList = property_neighbourhood.objects.all().values()
        propertyPriceRangeList = property_price_range.objects.all().values()



        context = {
            "data": properties_list,
            "propertyTypeList": propertyTypeList,
            "neighbourhoodList": neighbourhoodList,
            "propertyPriceRangeList": propertyPriceRangeList
        }

        #return HttpResponse(context)

        return render(request, 'listings.html', context)
