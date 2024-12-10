function createCarousel(carouselId) {    
    const carouselContainer = document.getElementById(carouselId); // Selects the container element for the carousel items
    const carouselItems = document.querySelectorAll('.carousel-item'); // Selects all the carousel items
    const prevBtn = document.querySelector('.prev-btn'); // Selects the previous button
    const nextBtn = document.querySelector('.next-btn'); // Selects the next button

    const itemWidth = carouselItems[0].offsetWidth; // Calculates the width of each item

    // Event listener for the previous button
    prevBtn.addEventListener('click', () => {
    // Scrolls the carousel container to the left by the width of one item
    carouselContainer.scrollLeft -= itemWidth;
    });

    // Event listener for the next button
    nextBtn.addEventListener('click', () => {
    // Scrolls the carousel container to the right by the width of one item
    carouselContainer.scrollLeft += itemWidth;
    });
}

// Initialize carousels
createCarousel('carousel1');
// ... initialize other carousels ...