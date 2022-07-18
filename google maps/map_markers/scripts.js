function loadMap() {
      var mapOptions = {
         center:new google.maps.LatLng(47.547412076332755, -122.15551020814637),
         zoom:7
      }
       var map = new google.maps.Map(document.getElementById("sample"),mapOptions);
        var marker = new google.maps.Marker({
        position: new google.maps.LatLng(47.547412076332755, -122.15551020814637),
        map: map,
      });
      window.map = map
   };


function addMarker() {
    var mapOptions = {
     center:new google.maps.LatLng(47.547412076332755, -122.15551020814637),
     zoom:7
    }
    //var map = new google.maps.Map(document.getElementById("sample"),mapOptions);
    map = window.map
     var marker = new google.maps.Marker({
    position: new google.maps.LatLng(46.000, -121.000),
    map: map,});
}


const myImages = [];

function addImage(imageBlob) {
  myImages.push(imageBlob);
}

function redrawImages() {
  const divForImages = document.getElementById('image_list');
  divForImages.innerHTML = '';
  myImages.forEach((imageBlob) => {
    const img = document.createElement('img');
    img.style.margin = "0 auto";
    img.src = URL.createObjectURL(imageBlob);
    divForImages.appendChild(img);
  });
  addMarker()
}

function addImageAndRedraw() {
  const fileInput = document.getElementById('fileInput');
  if (fileInput.files.length === 1) {
    addImage(fileInput.files[0]);
    redrawImages();
  } else {
    alert('No file selected. Select a file and try again.');
  }
}
