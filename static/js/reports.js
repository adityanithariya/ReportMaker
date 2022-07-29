// Add Report
let addReportBtn = document.getElementById("report-add");
let reportTitle = document.getElementById("reportTitle");

addReportBtn.onclick = function (event) {
    reportTitle.focus()
}

// Submit Report Prompt
let reportForm = document.getElementById("report-form")
let confirmBox = document.getElementById("confirm-box")
let confirmCover = document.getElementById("confirm-box-cover")
let confirmBtn = document.querySelector("#btn-div button:nth-child(1)")
let cancelBtn = document.querySelector("#btn-div button:nth-child(2)")

confirmBtn.onclick = function (event) {
    reportForm.submit()
}

function hideConfirmBox(event) {
    confirmCover.style.display = "none";
    confirmBox.style.display = "none";
}

reportForm.addEventListener("submit", function(evt) {
    confirmCover.style.display = "flex";
    confirmBox.style.display = "flex";
    evt.preventDefault();
}, true);

cancelBtn.onclick = hideConfirmBox;
confirmCover.onclick = hideConfirmBox;