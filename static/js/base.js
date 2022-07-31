// Nav Bar Slide Animation
let menuDiv = document.getElementById("menu");
let menuTxt = document.getElementById("menu-txt");
let navBar = document.getElementById("nav-expander-span");
let sideBar = document.getElementsByClassName("nav-on")[0];
let navMenu = document.getElementById("nav-open-menu");
let navCover = document.getElementById("nav-cover");
let profileDowArrow = document.getElementById("profile-downarrow");

function OpenNavBar() {
    if (window.matchMedia("(max-width:600px)").matches) {
        if (navBar.style.width != "150px") {
            navBar.style.width = "150px";
            try {
                sideBar.style.setProperty('--side-bar-left', '144px');
            } catch (error) {}
            profileMenu.style.left = "135px";
            profileDowArrow.style.left = "75px";
            profileDowArrow.style.top = "2px";
            navCover.style.width = "100%";
            navCover.style.height = "100%";
            navCover.style.backdropFilter = "blur(3px)";
            navCover.style.backgroundColor = "rgb(236 239 255 / 40%)";
            setTimeout(() => {
                navMenu.style.display = "flex";
            }, 300);
        }
        else{
            navBar.style.width = "60px";
            try {
                sideBar.style.setProperty('--side-bar-left', '54px');
            } catch (error) {}
            profileDowArrow.style.left = "-7px";
            profileDowArrow.style.top = "0px";
            profileMenu.style.left = "50px";
            navMenu.style.display = "none";
            navCover.style.backdropFilter = "blur(0px)";
            navCover.style.backgroundColor = "transparent";
            setTimeout(() => {
                navCover.style.width = "0%";
                navCover.style.height = "0%";
            }, 300);
        }
    
        // Timeouts, to check correct state at last of animation
        setTimeout(() => {
            if (navBar.style.width != "150px" && navMenu.style.display == "flex") {
                navMenu.style.display = "none";
            }
            if (navBar.style.width == "150px" && navCover.style.width == "0%") {
                navCover.style.width = "100%";
                navCover.style.height = "100%";
            }
        }, 300);
        setTimeout(() => {
            if (navBar.style.width == "150px" && navCover.style.width == "0%") {
                navCover.style.width = "100%";
                navCover.style.height = "100%";
            }
        }, 300);
    }
    else{
        
        if (navBar.style.width != "180px") {
            navBar.style.width = "180px";
            try {
                sideBar.style.setProperty('--side-bar-left', '173.5px');
            } catch (error) {}
            profileMenu.style.left = "160px";
            profileDowArrow.style.left = "90px";
            navCover.style.width = "100%";
            navCover.style.height = "100%";
            navCover.style.backdropFilter = "blur(3px)";
            navCover.style.backgroundColor = "rgb(236 239 255 / 40%)";
            setTimeout(() => {
                navMenu.style.display = "flex";
            }, 300);
        }
        else{
            navBar.style.width = "75px";
            try {
                sideBar.style.setProperty('--side-bar-left', '68.5px');
            } catch (error) {}
            profileMenu.style.left = "65px";
            profileDowArrow.style.left = "-7px";
            navMenu.style.display = "none";
            navCover.style.backdropFilter = "blur(0px)";
            navCover.style.backgroundColor = "transparent";
            setTimeout(() => {
                navCover.style.width = "0%";
                navCover.style.height = "0%";
            }, 300);
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
        }, 300);
        setTimeout(() => {
            if (navBar.style.width == "180px" && navCover.style.width == "0%") {
                navCover.style.width = "100%";
                navCover.style.height = "100%";
            }
        }, 300);
    }
}

menuDiv.onclick = OpenNavBar;
menuTxt.onclick = OpenNavBar;
navCover.onclick = OpenNavBar;

// Dropdown Profile Menu
let profileBtn = document.getElementsByClassName("profile-btn")[0];
let profileTxt = document.getElementById("profile-txt");
let profileMenu = document.getElementById("dd-profile-menu");
let profileMenuCover = document.getElementById("ddmenu-cover");

function ddMenuCover(event) {
    if (profileMenu.style.display == "none") {
        profileMenu.style.display = "flex";
        profileMenuCover.style.width = "100vw";
        profileMenuCover.style.height = "100vh";
        console.log("show");
    }
    else{
        profileMenu.style.display = "none";
        profileMenuCover.style.width = "0";
        profileMenuCover.style.height = "0";
        console.log("hide");
    }
}

profileBtn.onclick = ddMenuCover;
profileTxt.onclick = ddMenuCover;
profileMenuCover.onmousedown = ddMenuCover;
