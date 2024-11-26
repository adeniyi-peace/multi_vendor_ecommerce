// Toggle Sidebar Menu
const menuIcon = document.getElementById('menuIcon');
const sideNav = document.getElementById('sideNav');
const closeBtn = document.getElementById('closeBtn');

// Open the sidebar when the menu icon is clicked
menuIcon.addEventListener('click', function() {
    sideNav.style.display = "block" ;// Add 'open' class to show the sidebar
});

// Close the sidebar when the close button is clicked
closeBtn.addEventListener('click', function() {
    sideNav.style.display = "none"; // Remove 'open' class to hide the sidebar
});