function toggleProfilePopup() {
    const popup = document.getElementById("profilePopup");
    popup.style.display = popup.style.display === "block" ? "none" : "block";
}

// Optional: Close popup if clicked outside
window.addEventListener("click", function (e) {
    const popup = document.getElementById("profilePopup");
    const icon = document.querySelector(".profile-icon");
    if (popup && !popup.contains(e.target) && e.target !== icon) {
        popup.style.display = "none";
    }
});