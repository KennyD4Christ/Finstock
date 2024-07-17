document.addEventListener('DOMContentLoaded', function() {
    fetchProducts();
});

function fetchProducts() {
    fetch('http://127.0.0.1:8000/products/')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('productTableBody');
            data.forEach(product => {
                const row = document.createElement('tr');

                // Product Name
                const productNameCell = document.createElement('td');
                productNameCell.textContent = product.name;
                row.appendChild(productNameCell);

                // Description
                const descriptionCell = document.createElement('td');
                descriptionCell.textContent = product.description;
                row.appendChild(descriptionCell);

                // Price
                const priceCell = document.createElement('td');
                priceCell.textContent = product.price;
                row.appendChild(priceCell);

                // Created
                const createdCell = document.createElement('td');
                createdCell.textContent = new Date(product.created).toLocaleString();
                row.appendChild(createdCell);

                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
}
