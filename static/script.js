var scrollTopBtn = document.getElementById("scrollTopBtn");

window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollTopBtn.style.display = "block";
    } else {
        scrollTopBtn.style.display = "none";
    }
}

// Show welcome modal on page load
window.onload = function() {
    document.getElementById("welcomeModal").style.display = "block";
}

// Close the modal when the "Enter as Guest" link is clicked
document.getElementById("enterAsGuest").onclick = function(event) {
    event.preventDefault(); // Prevent the default action of the link
    document.getElementById("welcomeModal").style.display = "none"; // Hide the modal
    window.location.href = "#GUEST"; // Redirect to homepage
}

// Modal
var modal = document.getElementById("testimonialModal");
var btn = document.getElementById("open-modal");
var span = document.getElementsByClassName("close")[0];

// JavaScript function to scroll to the top
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}

// Event listener for the button
document.getElementById("scrollTopBtn").addEventListener("click", topFunction);


btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
