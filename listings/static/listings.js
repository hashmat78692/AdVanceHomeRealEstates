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
    $.ajax({
         url:'/save-images',
         type: 'POST',
         data: data,
         success: function (response) {
         },
         error: function (response) {
         },
        cache: false,
        contentType: false,
        processData: false
   });
  },
  error: (error) => {
    console.log(error);
  }
});


}