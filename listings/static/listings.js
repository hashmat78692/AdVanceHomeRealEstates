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

  $.ajax({
  url: "/save-listings",
  type: "POST",
  dataType: "json",
  data: listingData,
  success: (data) => {
    console.log(data);
  },
  error: (error) => {
    console.log(error);
  }
});


}