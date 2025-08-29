//time clock
function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2, '0');
    const m = String(now.getMinutes()).padStart(2, '0');
    const s = String(now.getSeconds()).padStart(2, '0');
    document.getElementById('clock').textContent = `${h}:${m}:${s}`;
}
setInterval(updateClock, 1000);
updateClock();

// Slider toggle
const slider = document.getElementById('modeToggle');
const modeIndicator = document.getElementById('modeIndicator');

document.addEventListener("DOMContentLoaded", () => {
    const modeToggle = document.getElementById("modeToggle");
    const userText = document.getElementById("User");
    const debugText = document.getElementById("Debug");

    // Nastavíme výchozí stav (Test aktivní)
    userText.classList.add("active");
    debugText.classList.add("inactive");

    // Reakce na změnu přepínače
    modeToggle.addEventListener("change", () => {
        if (modeToggle.checked) {
            // Debug mód
            userText.classList.remove("active");
            userText.classList.add("inactive");

            debugText.classList.remove("inactive");
            debugText.classList.add("active");
        } else {
            // Test mód
            userText.classList.remove("inactive");
            userText.classList.add("active");

            debugText.classList.remove("active");
            debugText.classList.add("inactive");
        }
    });
});