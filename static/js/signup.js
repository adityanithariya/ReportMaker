teamcodediv = document.getElementById("teamcode-div");
inputPasswords = document.getElementsByClassName("password");
togglePasswordVids = document.getElementsByClassName("anime-passShow")

role.onchange = function (event) {
    if(event.target.value == "member"){
        teamcodediv.style.display = "block";
    }
    else{
        teamcodediv.style.display = "none";
    }
};

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

// for (let index = 0; index < inputPasswords.length; index++) {
//     togglePasswordImgs[index].onclick = function (event) {
//         password = inputPasswords[index];
//         if (password.type == "password") {
//             password.type = "text";
//             togglePasswordImgs[index].src = "/static/images/eye-open.jpg";
//         } 
//         else {
//             password.type = "password";
//             togglePasswordImgs[index].src = "/static/images/eye-close.jpg";
//         }
//     };
// }

// for (let index = 0; index < inputPasswords.length; index++) {
//     togglePasswordVids[index].onclick = function (event) {
//         var stop = (interval) => {
//             togglePasswordVids[index].pause();
//             console.log("stop");
//             clearInterval(interval);
//         };
//         password = inputPasswords[index];
//         if (password.type == "password") {
//             password.type = "text";
//             togglePasswordVids[index].play();
//             console.log("interval");
//             interval = setInterval(stop, 1000, interval);
//         } 
//         else {
//             password.type = "password";
//             interval = setInterval(stop, 1000, interval)
//             console.log("interval");
//             togglePasswordVids[index].play();
//         }
//     };
// }