console.log("Eng. Tenywa Ibrahim portfolio loaded successfully.");// =========================
// MOBILE NAVIGATION
// =========================

document.addEventListener("DOMContentLoaded", function () {

    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (!menuToggle || !navLinks) {
        return;
    }

    menuToggle.addEventListener("click", function () {

        navLinks.classList.toggle("active");

    });


    const links = navLinks.querySelectorAll("a");

    links.forEach(function (link) {

        link.addEventListener("click", function () {

            navLinks.classList.remove("active");

        });

    });

});