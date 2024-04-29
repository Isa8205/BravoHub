function myFunction(){
    var x = document.getElementById("myTopnav")
    
    if (x.className === "topnav") {
        x.className += " responsive"
        // y.classname += "active"
    } else {
        x.className = "topnav"
    }
}

function showpass() {
    var a = document.getElementById("pass");
    var b = document.getElementById("show")
    if (a.type === "password") {
      a.type = "text";
      b.src = '../static/images/icons/hide.png'
    } else {
      a.type = "password";
      b.src = '../static/images/icons/show.png'
    }
  }


