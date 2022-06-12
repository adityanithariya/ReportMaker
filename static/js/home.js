// Search-Btn Animation
let searchInput = document.getElementById("search-input");
let search = document.getElementById("search-vid");

searchInput.addEventListener("focusin", function (event) {
    search.play();
})

// Home Icon Animation
let homeDiv = document.getElementById("home");
let homeVid = document.getElementById("home-vid");

homeDiv.onmouseenter = function (event) {
    homeVid.play()
}

// Notification Icon Animation
let notifVid = document.getElementById("notif-vid");
let notifDiv = document.getElementById("notif-div");

notifDiv.onmouseenter = function (event) {
    notifVid.play()
}

// Nav Bar Slide Animation
let menuIcon = document.getElementById("menu");
let menuTxt = document.getElementById("menu-txt");
let navBar = document.getElementById("nav-expander-span");
let sideBar = document.getElementsByClassName("nav-side-bar");
let navMenu = document.getElementById("nav-open-menu");
let navCover = document.getElementById("nav-cover");

function OpenNavBar() {
    if (navBar.style.width != "180px") {
        navBar.style.width = "180px";
        sideBar[0].style.left = "173.5px";
        navCover.style.width = "100%";
        navCover.style.height = "100%";
        navCover.style.backdropFilter = "blur(3px)";
        navCover.style.backgroundColor = "rgb(236 239 255 / 40%)";
        setTimeout(() => {
            navMenu.style.display = "flex";
        }, 500);
    }
    else{
        navBar.style.width = "75px";
        sideBar[0].style.left = "68.5px";
        navMenu.style.display = "none";
        navCover.style.backdropFilter = "blur(0px)";
        navCover.style.backgroundColor = "transparent";
        setTimeout(() => {
            navCover.style.width = "0%";
            navCover.style.height = "0%";
        }, 1000);
    }

    // Timeouts, to check correct state at last of animation
    setTimeout(() => {
        if (navBar.style.width != "180px" && navMenu.style.display == "flex") {
            navMenu.style.display = "none";
        }
        if (navBar.style.width == "180px" && navCover.style.width == "0%") {
            navCover.style.width = "100%";
            navCover.style.height = "100%";
        }
    }, 500);
    setTimeout(() => {
        if (navBar.style.width == "180px" && navCover.style.width == "0%") {
            navCover.style.width = "100%";
            navCover.style.height = "100%";
        }
    }, 1001);
}

menuIcon.onclick = OpenNavBar;
menuTxt.onclick = OpenNavBar;
navCover.onclick = OpenNavBar;