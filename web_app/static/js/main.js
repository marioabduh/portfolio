// main.js

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Get a reference to the hamburger menu button
    const hamburgerButton = document.querySelector('.hamburger-menu');
    
    // Get a reference to the navigation menu
    const navMenu = document.getElementById('nav-menu');
    
    // Add a click event listener to the hamburger menu button
    hamburgerButton.addEventListener('click', function() {
        // Toggle the 'active' class on the navigation menu
        navMenu.classList.toggle('active');
        hamburgerButton.classList.toggle('close');

    });
});
