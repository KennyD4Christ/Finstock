// static/js/updateCustomerCount.js

async function updateCustomerCount() {
    try {
        const response = await fetch("/users/customer_count/");
        if (response.ok) {
            const data = await response.json();
            document.getElementById('customer-count').innerText = data.customer_count;
        } else {
            console.error('Failed to fetch customer count');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call updateCustomerCount periodically or when needed
setInterval(updateCustomerCount, 1000); // Update every 5 seconds

// Optionally, you can call it immediately after loading the page
document.addEventListener('DOMContentLoaded', updateCustomerCount);
