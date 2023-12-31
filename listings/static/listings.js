$(document).ready(function() {
    $( "#listingDate" ).datepicker({
        dateFormat: "yy-mm-dd"
    });
    $('#image1').hide();
    $('#image2').hide();
    $('#image3').hide();
    $('#image4').hide();
});

$('.addListingsModal').on('hidden.bs.modal', function () {
 location.reload();
})


function SaveListing() {

var listingData = new Object();
listingData.listingDate = $('#listingDate').val();
listingData.addressStreet = $('#addressStreet').val();
listingData.addressCity = $('#addressCity').val();
listingData.addressState = $('#addressState').val();
listingData.addressZipCode = $('#addressZipCode').val();
listingData.listingPrice = $('#listingPrice').val();
listingData.listingDescription = $('#listingDescription').val();
listingData.listingStatus = $('#listingStatus').val();
if ($('#featuredPropertyIndicator').is(':checked')) {
    listingData.featuredPropertyIndicator = "true";
}
else
{
    listingData.featuredPropertyIndicator = "false";
}

listingData.priceRange = $('#priceRange').val();
listingData.neighbourhood = $('#neighbourhood').val();
listingData.propertyType = $('#propertyType').val();
listingData.proprtyId = $('#propertyId').val();
listingData = JSON.stringify(listingData);

const propertyImage1 = $('#propertyImage1').get(0).files[0];
const propertyImage2 = $('#propertyImage2').get(0).files[0];
const propertyImage3 = $('#propertyImage3').get(0).files[0];
const propertyImage4 = $('#propertyImage4').get(0).files[0];

var Data = new FormData();
Data.append("image1", propertyImage1)
Data.append("image2", propertyImage2)
Data.append("image3", propertyImage3)
Data.append("image4", propertyImage4)
Data.append("listingData", listingData)
Data.append("csrfmiddlewareoken", '{{ csrf_token }}')

  $.ajax({
  url: "/save-listings",
  type: "POST",
  processData: false,
  contentType: false,
  mimeType:"multipart/form-data",
  data:Data,
  success: (data) => {
    console.log(data);
    if(data == "success"){
        alert("Saved Successfully!!")
        location.reload();}
    if(data == "edited"){
        alert("Edited Successfully!!")
        location.reload();}
  },
  error: (error) => {
    console.log(error);
  }
});


}

function addListing(){
console.log("Clicked");

$('.addListingsModal').modal('show');

}

function editListing(id){

$.ajax({
         url:'/edit-listing/'+id,
         type: 'GET',
         success: function (response) {
         var selectedProperty = response[0]['fields'];
         var propertyID = response[0]['pk'];
         console.log('hi')
         setValuesToModal(selectedProperty,propertyID);
         },
         error: function (response) {
         console.log(response);
         }
   });

}

function setValuesToModal(selectedProperty,propertyID){
console.log('hello')
$('.addListingsModal').modal('show');
$('#image1').show();
$('#image2').show();
$('#image3').show();
$('#image4').show();

console.log(selectedProperty);

$('#listingDate').val(selectedProperty.property_listing_date);
$('#addressStreet').val(selectedProperty.property_listing_street);
$('#addressCity').val(selectedProperty.property_listing_city);
$('#addressState').val(selectedProperty.property_listing_state);
$('#addressZipCode').val(selectedProperty.property_listing_zipcode);
$('#listingPrice').val(selectedProperty.property_listing_price);
$('#listingDescription').val(selectedProperty.listing_description);
$('#listingStatus').val(selectedProperty.property_listing_status);

if(selectedProperty.property_listing_is_featured== true)
{
  $('#featuredPropertyIndicator').prop('checked', true);;
}

$('#priceRange').val(selectedProperty.property_price_range_id);
$('#neighbourhood').val(selectedProperty.property_neighbourhood_id);
$('#propertyType').val(selectedProperty.property_type_id);
$('#propertyId').val(propertyID);

$('#image1').attr("src", "/static/"+selectedProperty.property_listing_pic1);
$('#image2').attr("src", "/static/"+selectedProperty.property_listing_pic2);
$('#image3').attr("src", "/static/"+selectedProperty.property_listing_pic3);
$('#image4').attr("src", "/static/"+selectedProperty.property_listing_pic4);



}

function deleteListing(id){
if (confirm('are you sure you want to delete the listing: '+id+' ?')) {
    $.ajax({
         url:'/delete-listing/'+id,
         type: 'DELETE',
         success: function (response) {
            console.log(response)
            if(response == "success")
            {
                alert("Deleted Successfully!!")
                location.reload();
            }
         },
         error: function (response) {
         console.log(response);
         }
   });
} else {
    alert('Why did you press cancel? You should have confirmed');
}


}

function filterListings()
{
console.log("inFilter")
var filterData = new Object();
filterData.priceRangeFilter = $("#priceRangeFilter").val();
filterData.propertyTypeFilter = $("#propertyTypeFilter").val();
filterData.neighbourhoodFilter = $("#neighbourhoodFilter").val();

console.log(filterData);

$.ajax({
         url:'/filter-listing',
         type: 'GET',
         data:filterData,
         success: function (response) {
            console.log(response)
         },
         error: function (response) {
         console.log(response);
         }
   });


}