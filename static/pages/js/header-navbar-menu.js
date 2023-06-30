hamburger = document.querySelector(".hamburger-wrapper");
hamburger.onclick = function() {
	navBar = document.querySelector(".nav-bar");
	navBar.classList.toggle("active");
	line = document.querySelector(".hamburger-wrapper");
	line.classList.toggle("active");
}