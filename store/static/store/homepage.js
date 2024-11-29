// Get elements for carousel control
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const carouselContainer = document.querySelector('.carousel-container');
const carouselItems = document.querySelectorAll('.carousel-item');

// Set the width of the container dynamically based on number of items to display
const itemsToShow = 5; // Number of items to show at once (adjust based on your layout)

let currentIndex = 0;
const totalItems = carouselItems.length;

// Function to move carousel to the next set of items
function moveCarousel(direction) {
    // Calculate the new index
    currentIndex += direction;
    
    // Ensure we don't go out of bounds
    if (currentIndex < 0) {
        currentIndex = totalItems - itemsToShow;
    } else if (currentIndex >= totalItems) {
        currentIndex = 0;
    }
    
    // Update the transform property to show the correct set of items
    const offset = -(currentIndex * (100 / itemsToShow));
    carouselContainer.style.transform = `translateX(${offset}%)`;
}

// Add event listeners to the buttons
prevBtn.addEventListener('click', () => moveCarousel(-1)); // Move left
nextBtn.addEventListener('click', () => moveCarousel(1)); // Move right

