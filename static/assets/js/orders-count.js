document.addEventListener('DOMContentLoaded', function() {
    fetchTotalOrders();
});

function fetchTotalOrders() {
    fetch('http://127.0.0.1:8000/orders/')
        .then(response => response.json())
        .then(data => {
            const totalOrders = data.length;
            document.getElementById('totalOrders').textContent = `Total Orders: ${totalOrders}`;
        })
        .catch(error => {
            console.error('Error fetching orders:', error);
            document.getElementById('totalOrders').textContent = 'Error loading total orders';
        });
}
