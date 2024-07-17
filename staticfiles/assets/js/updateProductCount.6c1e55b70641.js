async function fetchProductCount() {
    try {
        const response = await fetch('/products/product_count'); // Make sure this URL matches your API endpoint
        const data = await response.json();
        const productCount = data.product_count;

        // Update your HTML to display the count
        const countElement = document.getElementById('product-count');
        countElement.textContent = productCount;
    } catch (error) {
        console.error('Error fetching product count:', error);
        // Handle the error appropriately (e.g., display an error message to the user)
    }
}

// Call the function to fetch and display the count when the page loads
fetchProductCount();
// Call updateProductCount periodically or when needed
setInterval(fetchProductCount, 5000); // Update every 5 seconds

// Optionally, you can call it immediately after loading the page
document.addEventListener('DOMContentLoaded', fetchProductCount);
