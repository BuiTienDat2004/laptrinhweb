const images = ["image1.jpg", "image2.jpg", "image3.jpg"];
let currentIndex = 0;
const imgElement = document.getElementById("slideshow");

function showImage(index) {
  imgElement.src = images[index];
}

function nextImage() {
  currentIndex = (currentIndex + 1) % images.length;
  showImage(currentIndex);
}

function prevImage() {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  showImage(currentIndex);
}

// Auto slideshow every 3 seconds
setInterval(nextImage, 3000);

// Initialize
showImage(currentIndex);
