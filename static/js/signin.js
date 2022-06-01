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
            setTimeout(changeSrc, 1000, togglePasswordVids[index], "/static/images/hide.mp4");
        } 
        else {
            togglePasswordVids[index].play();
            password.type = "password";
            setTimeout(changeSrc, 1000, togglePasswordVids[index], "/static/images/show.mp4");
        }
    };
}