document.addEventListener('DOMContentLoaded', function() {
    fetchOrders();
});

function fetchOrders() {
    fetch('http://127.0.0.1:8000/orders/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('orderTableBody');
            let totalOrders = 0;
            const uniqueProductIds = new Set();

            data.forEach(order => {
                order.items.forEach(item => {
                    const row = document.createElement('tr');

                    // Customer Name
                    const customerNameCell = document.createElement('td');
                    customerNameCell.textContent = `${order.customer.first_name} ${order.customer.last_name}`;
                    row.appendChild(customerNameCell);

                    // Product Name
                    const productNameCell = document.createElement('td');
                    const productNameDiv = document.createElement('div');
                    productNameDiv.className = 'd-flex align-items-center';
                    
                    const productImg = document.createElement('img');
                    productImg.src = '{% static "assets/images/logos.png" %}';
                    productImg.alt = '';
                    productImg.className = 'flex-shrink-0 me-12 radius-8 me-12';

                    const productInfoDiv = document.createElement('div');
                    productInfoDiv.className = 'flex-grow-1';

                    const productName = document.createElement('h6');
                    productName.className = 'text-md mb-0 fw-normal';
                    productName.textContent = item.product.name;

                    const productCategory = document.createElement('span');
                    productCategory.className = 'text-sm text-secondary-light fw-normal';
                    productCategory.textContent = 'Fashion'; // Adjust this as necessary

                    productInfoDiv.appendChild(productName);
                    productInfoDiv.appendChild(productCategory);
                    productNameDiv.appendChild(productImg);
                    productNameDiv.appendChild(productInfoDiv);
                    productNameCell.appendChild(productNameDiv);
                    row.appendChild(productNameCell);

                    // Product Price
                    const productPriceCell = document.createElement('td');
                    productPriceCell.textContent = item.product.price;
                    row.appendChild(productPriceCell);

                    // Phone
                    const phoneCell = document.createElement('td');
                    phoneCell.textContent = order.customer.phone;
                    row.appendChild(phoneCell);

                    // Shipped
                    const shippedCell = document.createElement('td');
                    shippedCell.textContent = order.is_shipped ? 'Yes' : 'No';
                    row.appendChild(shippedCell);

                    // Paid
                    const paidCell = document.createElement('td');
                    paidCell.textContent = order.is_paid ? 'Yes' : 'No';
                    row.appendChild(paidCell);

                    // Created
                    const createdCell = document.createElement('td');
                    createdCell.textContent = new Date(order.created).toLocaleString();
                    row.appendChild(createdCell);

                    tableBody.appendChild(row);

                    // Increment the total orders counter
                    totalOrders++;

                    // Add product ID to the set of unique product IDs
                    uniqueProductIds.add(item.product.id);
                });
            });

            // Display the total orders count
            document.getElementById('totalOrders').textContent = `${totalOrders}`;
            
            // Display the total products count
            document.getElementById('totalProducts').textContent = `${uniqueProductIds.size}`;
        })
        .catch(error => {
            console.error('4', error);
            document.getElementById('totalOrders').textContent = '3';
            document.getElementById('totalProducts').textContent = '4';
        });
}
