// Dropdown
const dropbtn = document.querySelector(".dropbtn");
const dropdownContent = document.querySelector(".dropdown-content");

// Darkmode toggle
const themeButton = document.getElementById("themeButton");
const body = document.body;

//change testing mode
const modeButton = document.getElementById("modeButton");

if (modeButton) {
    modeButton.addEventListener("click", (event) => {
    });
}

if (themeButton) {
    themeButton.addEventListener("click", (event) => {
        event.preventDefault();
        body.classList.toggle("darkmode");
    });
}

// Help button
const helpButton = document.getElementById("helpButton");
if (helpButton) {
    helpButton.addEventListener("click", (event) => {
        event.preventDefault();
        alert("Help dialog here!");
    });
}

// Dropdown toggle
if (dropbtn && dropdownContent) {
    dropbtn.addEventListener("click", function (event) {
        event.stopPropagation();
        dropdownContent.classList.toggle("show");
    });
}

// Dropdown close when clicking outside
window.addEventListener("click", function () {
    if (dropdownContent && dropdownContent.classList.contains("show")) {
        dropdownContent.classList.remove("show");
    }
});
