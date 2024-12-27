document.addEventListener('DOMContentLoaded', () => {
    // Image Thumbnail Preview
    const thumbnails = document.querySelectorAll('.thumbnail');
    const mainImage = document.getElementById('main-image');
    
    thumbnails.forEach(thumb => {
        thumb.addEventListener('click', () => {
            const newImageSrc = thumb.getAttribute('data-img');
            mainImage.src = newImageSrc;
        });
    });

    // Add to Cart Button Interaction
    const addToCartButton = document.querySelector('.add-to-cart');
    
    addToCartButton.addEventListener('click', () => {
        const selectedColor = document.getElementById('color').value;
        const selectedSize = document.getElementById('size').value;
        const productPrice = document.getElementById('product-price').textContent.trim();
        const productName = document.querySelector('.product-details h1').textContent;
        
        const cartItem = {
            productName: productName,
            price: productPrice,
            color: selectedColor,
            size: selectedSize
        };

        // Simulate adding the item to the cart (this would normally interact with a shopping cart system)
        alert(`Added to Cart: \n${cartItem.productName} - ${cartItem.color} - ${cartItem.size} - ${cartItem.price}`);

        // Optionally, you can save the cart item in a local storage or session storage for real cart functionality
        // For example: 
        // localStorage.setItem('cart', JSON.stringify(cartItem));
    });

    // Review Submission
    const reviewForm = document.querySelector('.review-form');
    const submitReviewButton = document.querySelector('.submit-review');
    
    submitReviewButton.addEventListener('click', () => {
        const reviewText = reviewForm.querySelector('textarea').value;
        const reviewAuthor = "Anonymous";  // This can be replaced with logged-in user info
        const reviewRating = "★★★★☆";  // Ideally, the rating would be dynamic (e.g., a star rating system)

        if (reviewText.trim() === "") {
            alert("Please write a review before submitting.");
            return;
        }

        // Create a new review element and append it to the reviews section
        const reviewSection = document.querySelector('.reviews-section');

        const newReview = document.createElement('div');
        newReview.classList.add('review');

        const reviewHeader = document.createElement('div');
        reviewHeader.classList.add('review-header');
        reviewHeader.innerHTML = `
            <span class="review-author">${reviewAuthor}</span>
            <span class="review-rating">${reviewRating}</span>
        `;

        const reviewBody = document.createElement('p');
        reviewBody.classList.add('review-text');
        reviewBody.textContent = reviewText;

        newReview.appendChild(reviewHeader);
        newReview.appendChild(reviewBody);

        reviewSection.appendChild(newReview);

        // Clear the review form
        reviewForm.querySelector('textarea').value = '';
    });
});

// carosel functions

let currentIndex = 0; // Track the current index of the visible image
const carouselItems = document.querySelectorAll('.carousel-item');
const totalItems = carouselItems.length;

// Function to move the carousel
function moveCarousel(direction) {
    currentIndex += direction;

    // If currentIndex exceeds totalItems, reset it to 0 (loop back)
    if (currentIndex < 0) {
        currentIndex = totalItems - 1;
    } else if (currentIndex >= totalItems) {
        currentIndex = 0;
    }

    updateCarouselPosition();
}

// Update the position of the carousel to show the current image
function updateCarouselPosition() {
    const carousel = document.querySelector('.carousel');
    const itemWidth = carouselItems[0].offsetWidth; // Get the width of an individual image
    carousel.style.transform = `translateX(-${itemWidth * currentIndex}px)`;
}

// Optionally, you can automatically slide the carousel (e.g., every 3 seconds)
setInterval(() => {
    moveCarousel(1); // Move to the next image every 3 seconds
}, 3000);
