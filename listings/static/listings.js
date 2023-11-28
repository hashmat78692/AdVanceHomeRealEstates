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
listingData.featuredPropertyIndicator = $('#featuredPropertyIndicator').val();
listingData.priceRange = $('#priceRange').val();
listingData.neighbourhood = $('#neighbourhood').val();
listingData.propertyType = $('#propertyType').val();
listingData = JSON.stringify(listingData);

const Image1 = $('#propertyImage1').prop('files')[0];
var data = new FormData();
data.append('image1', Image1)

console.log(Image1);
console.log(listingData);

  $.ajax({
  url: "/save-listings",
  type: "POST",
  data: {'listingData': listingData},
  success: (data) => {
    console.log(data);
    if(data == "success")
            {
                alert("Saved Successfully!!")
                location.reload();
            }
//    $.ajax({
//         url:'/save-images',
//         type: 'POST',
//         data: data,
//         success: function (response) {
//         },
//         error: function (response) {
//         },
//        cache: false,
//        contentType: false,
//        processData: false
//   });
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
         setValuesToModal(selectedProperty);
         },
         error: function (response) {
         console.log(response);
         }
   });

}

function setValuesToModal(selectedProperty){

$('.addListingsModal').modal('show');

console.log(selectedProperty);

$('#listingDate').val(selectedProperty.property_listing_date);
$('#addressStreet').val(selectedProperty.property_listing_street);
$('#addressCity').val(selectedProperty.property_listing_city);
$('#addressState').val(selectedProperty.property_listing_state);
$('#addressZipCode').val(selectedProperty.property_listing_zipcode);
$('#listingPrice').val(selectedProperty.property_listing_price);
$('#listingDescription').val(selectedProperty.listing_description);
$('#listingStatus').val(selectedProperty.property_listing_status);
$('#featuredPropertyIndicator').val(selectedProperty.property_listing_is_featured);
$('#priceRange').val(selectedProperty.property_price_range_id);
$('#neighbourhood').val(selectedProperty.property_neighbourhood_id);
$('#propertyType').val(selectedProperty.property_type_id);

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