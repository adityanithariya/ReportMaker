inputPasswords = document.getElementsByClassName("password");
togglePasswordVids = document.getElementsByClassName("anime-passShow")

function changeSrc(video, src) {
    video.src = src;
}

for (let index = 0; index < inputPasswords.length; index++) {
    togglePasswordVids[index].onclick = function (event) {
        password = inputPasswords[index];
        if (password.type == "password") {
            togglePasswordVids[index].play();
            password.type = "text";
            setTimeout(changeSrc, 1000, togglePasswordVids[index], "/static/images/sign/hide.mp4");
        } 
        else {
            togglePasswordVids[index].play();
            password.type = "password";
            setTimeout(changeSrc, 1000, togglePasswordVids[index], "/static/images/sign/show.mp4");
        }
    };
}

// Error Message Close
let messageMainDiv = document.getElementsByClassName("message-box")
let messageDiv = document.getElementsByClassName("message-div")
let closeBtn = document.getElementsByClassName("close")
for (let index = 0; index < messageMainDiv.length; index++) {
    const msgMainDiv = messageMainDiv[index];
    const msgDiv = messageDiv[index];
    const close = closeBtn[index];
    if (msgDiv.innerHTML.trim() == "") {
        msgMainDiv.style.display = "none";
    }
    
    close.onclick = function (event) {
        msgMainDiv.style.display = "none";
    }
}