// Function to "open" and "close" the secondary menu
function buttonFlip() {
    var tog = document.getElementById("secondary"); // Gets the element of the "secondary" menu
    tog.classList.toggle("show"); // Toggles secondary menu between hidden and visible
    var hamburger = document.querySelector(".hamburger"); /// Select the hamburger query 
    hamburger.classList.toggle("is-active"); // Toggle between active and inactive for button animation
  }