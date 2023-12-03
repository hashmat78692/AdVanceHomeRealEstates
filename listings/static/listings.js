$("div#my-awesome-dropzone").dropzone();
$("div#my-awesome-dropzone1").dropzone();
$("div#my-awesome-dropzone2").dropzone();
$("div#my-awesome-dropzone3").dropzone();

Dropzone.options.myawesomedropzone = { // camelized version of the `id`
    paramName: "file", // The name that will be used to transfer the file
    maxFilesize: 2, // MB
    maxFiles: 2,
    uploadMultiple: true,
    accept: function(file, done) {
      if (file.name == "justinbieber.jpg") {
        done("Naha, you don't.");
      }
      else { done(); }
    }
  };

  Dropzone.options.myawesomedropzone1 = { // camelized version of the `id`
    paramName: "file2", // The name that will be used to transfer the file
    maxFilesize: 2, // MB
    maxFiles: 1,
    accept: function(file, done) {
      if (file.name == "justinbieber.jpg") {
        done("Naha, you don't.");
      }
      else { done(); }
    }
  };
  Dropzone.options.myawesomedropzone2 = { // camelized version of the `id`
    paramName: "file3", // The name that will be used to transfer the file
    maxFilesize: 2, // MB
    maxFiles: 1,
    accept: function(file, done) {
      if (file.name == "justinbieber.jpg") {
        done("Naha, you don't.");
      }
      else { done(); }
    }
  };
  Dropzone.options.myawesomedropzone3 = { // camelized version of the `id`
    paramName: "file4", // The name that will be used to transfer the file
    maxFilesize: 2, // MB
    maxFiles: 1,
    accept: function(file, done) {
      if (file.name == "justinbieber.jpg") {
        done("Naha, you don't.");
      }
      else { done(); }
    }
  };

function SaveListing(id) {

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

const propertyImage1 = $('#propertyImage1').get(0).files[0];
const propertyImage2 = $('#propertyImage2').get(0).files[0];
const propertyImage3 = $('#propertyImage3').get(0).files[0];
const propertyImage4 = $('#propertyImage4').get(0).files[0];
console.log(propertyImage1)
var Data = new FormData();
Data.append("listingData", listingData)
Data.append("image1", propertyImage1)
Data.append("image2", propertyImage2)
Data.append("image3", propertyImage3)
Data.append("image4", propertyImage4)
Data.append("csrfmiddlewareoken", '{{ csrf_token }}')


  $.ajax({
  url: "/save-listings/"+id,
  type: "POST",
  processData: false,
  contentType: false,
  mimeType:"multipart/form-data",
  data:Data,
  success: (data) => {
    console.log(data);
    if(data == "success")
            {
                alert("Saved Successfully!!")
                location.reload();
            }
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