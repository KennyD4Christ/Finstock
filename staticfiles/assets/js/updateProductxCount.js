// static/js/updateCustomerCount.js

async function updateProductxCount() {
    try {
        const response = await fetch("/products/product_count/");
        if (response.ok) {
            const data = await response.json();
            document.getElementById('product-count').innerText = data.customer_count;
        } else {
            console.error('Failed to fetch product count');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call updateCustomerCount periodically or when needed
setInterval(updateProductxCount, 5000); // Update every 5 seconds

// Optionally, you can call it immediately after loading the page
document.addEventListener('DOMContentLoaded', updateProductxCount);


