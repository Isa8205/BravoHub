/*
---------------------------------------------------------------------------------------------------------------
Navbar
---------------------------------------------------------------------------------------------------------------
*/

function navfunction(){
    var x = document.getElementById("myTopnav")
    
    if (x.className === "topnav") {
        x.className += " responsive"
    } else {
        x.className = "topnav"
    }
}

/*
---------------------------------------------------------------------------------------------------------------
Slideshow
---------------------------------------------------------------------------------------------------------------
*/
var slideIndex = 1 
showSlides(slideIndex)

function plusSlides(n) {
  showSlides(slideIndex += n)
}

function currentSlide(n) {
  showSlides(slideIndex = n)
}

function showSlides(n) {
  var i ;
  var slides = document.getElementsByClassName("slide")
  var dots = document.getElementsByClassName("dot")
  if (n > slides.length) {slideIndex = 1};
  if (n < 1) {slideIndex = slides.length}

  for (i=0; i < slides.length; i++) {
    slides[i].style.display = "none"
  }
  for (i=0; i < slides.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "")
  }

  slides[slideIndex - 1].style.display = "block"
  dots[slideIndex - 1].className += " active"
}

/*
---------------------------------------------------------------------------------------------------------------
Body
---------------------------------------------------------------------------------------------------------------
*/
// -------Changes the format of the date----------
document.addEventListener("DOMContentLoaded", function() {
  // Get all elements with the class "date"
  var dateElements = document.querySelectorAll(".date");

  // Loop through each date element
  dateElements.forEach(function(dateElement) {
      var dateValue = dateElement.textContent.trim();
      var parts = dateValue.split(/[-\s]+/);

      if (parts.length === 4) {
          var year = parts[0];
          var month = parseInt(parts[1]);
          var day = parts[2];
          var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

          if (month >= 1 && month <= 12) {
              var formattedDate = day + ', ' + months[month - 1] + ', ' + year;
              dateElement.textContent = formattedDate;
          } else {
              console.error("Invalid month:", month);
          }
      } else {
          console.error("Invalid date format:", dateValue);
      }
  });
});

// Function to scroll to the top of the page
function scrollToTop() {
  window.scrollTo({
      top: 0,
      behavior: 'smooth'
  });
}

// Show the back-to-top button when user scrolls down
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      document.querySelector('.back-to-top').style.display = "block";
  } else {
      document.querySelector('.back-to-top').style.display = "none";
  }
}

/*
---------------------------------------------------------------------------------------------------------------
Modal
---------------------------------------------------------------------------------------------------------------
*/
function modalfunction(state) {
  const modal = document.getElementById('modal')

  if (state) {            
      modal.style.visibility = "visible"
  } else {
      modal.style.visibility = "hidden"
  }
}

/*
---------------------------------------------------------------------------------------------------------------
Forms
---------------------------------------------------------------------------------------------------------------
*/
// The function for showing the password
function showpass() {
  var a = document.getElementById("pass");
  var c = document.getElementById("pass2")
  var b = document.getElementById("show")
  if (a.type === "password") {
    a.type = "text";
    c.type = "text"
    b.src = '../static/images/icons/hide.png'
  } else {
    a.type = "password";
    c.type = "password"
    b.src = '../static/images/icons/show.png'
  }
}

// To check on whether or not a usrname is available
document.getElementById("username").addEventListener("input", function() {
    var username = this.value.trim();
    if (username !== "") {
        checkUsernameAvailability(username);
    } else {
        document.getElementById("usernameAvailability").textContent = "";
    }
});

function checkUsernameAvailability(username) {
    fetch("/check_username", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username })
    })
    .then(response => response.json())
    .then(data => {
        var response = document.getElementById("usernameAvailability")
        if (data.available) {
            response.textContent = "Username available";
            response.style.color = "green"
        } else {
            response.textContent = "Username not available";
            response.style.color = "red"
        }
    })
    .catch(error => {
        console.error("Error checking username availability:", error);
    });
}



