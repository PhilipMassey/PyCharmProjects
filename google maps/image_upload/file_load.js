
const myImages = [];

function addImage(imageBlob) {
  myImages.push(imageBlob);
}

function redrawImages() {
  const divForImages = document.getElementById('myImages');
  divForImages.innerHTML = '';
  myImages.forEach((imageBlob) => {
    const img = document.createElement('img');
    img.src = URL.createObjectURL(imageBlob);
    divForImages.appendChild(img);
  });
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
