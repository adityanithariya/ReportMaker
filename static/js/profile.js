// Input Width == Content
let baseline = document.getElementById("username-baseline")
let usernameInput = document.getElementById("username")

usernameInput.addEventListener('input', function (event) {
    let val = usernameInput.value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
    baseline.textContent = " " + val + " ";
    usernameInput.style.width = (baseline.offsetWidth - 5) + "px";
})

// Hover Animation
let profile = document.getElementsByClassName("profile")[0]
let profileImg = document.getElementsByClassName("profile-img")[0]
let profileForm = document.getElementById("profile-form")

profile.addEventListener("mouseenter", function (event) {
    profile.style.top = "50px";
    profile.style.height = "80vh";
    profile.style.width = "80vw";
    profile.style.borderRadius = "40px";
    profile.style.boxShadow = "none";
    profileImg.style.top = "-100px";
    profileForm.style.top = "-80px";
})

// Username edit
let editIcon = document.getElementById("user-edit")

editIcon.addEventListener("click", function (event) {
    if (usernameInput.readOnly) {
        usernameInput.readOnly = false;
    }
    else {
        usernameInput.readOnly = true;
    }
    usernameInput.focus()
})