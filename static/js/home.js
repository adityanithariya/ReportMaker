// Search-Btn Animation
let searchInput = document.getElementById("search-input");
let search = document.getElementById("search-vid");

searchInput.addEventListener("focusin", function (event) {
    search.play();
})

// Notification Icon Animation
let notifVid = document.getElementById("notif-vid");
let notifDiv = document.getElementById("notif-div");

notifDiv.onmouseenter = function (event) {
    notifVid.play()
}

// Notification Bar Animation
let notifBar = document.getElementById("notif-bar");
let notifText = document.getElementById("notif-bar-text");
let notifClose = document.getElementById("close");

if (notifText.innerHTML.trim() == "") {
    notifBar.style.display = "none";
}

notifClose.onclick = function (event) {
    notifClose.style.display = "none";
    notifText.style.display = "none";
    notifBar.style.height = 0;
    notifBar.style.border = "0px solid #c3e6cb";
}