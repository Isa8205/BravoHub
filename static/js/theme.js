function setTheme() {
    state = localStorage.getItem('theme')
    document.getElementById('theme').setAttribute('data-theme', state)
  }
  
  function themeFunction() {
    var themeElement = document.getElementById('theme');
    var currentState = themeElement.getAttribute("data-theme");
  
    if (currentState === "light") {
        themeElement.setAttribute("data-theme", "dark");
        localStorage.setItem('theme', 'dark')
    } else {
        themeElement.setAttribute("data-theme", "light");
        localStorage.setItem('theme', 'light')
    }
  }
  
  document.addEventListener("DOMContentLoaded", setTheme);