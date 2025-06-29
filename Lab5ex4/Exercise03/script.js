const products = [
  { id: 1, name: "HTML Course", price: 3000000 },
  { id: 2, name: "JavaScript Course", price: 2500000 },
  { id: 3, name: "React Course", price: 3200000 }
];

let cart = [];

const productList = document.getElementById("productList");
const cartList = document.getElementById("cartList");
const totalEl = document.getElementById("total");

function renderProducts() {
  productList.innerHTML = "";
  products.forEach(product => {
    const div = document.createElement("div");
    div.className = "product";
    div.innerHTML = `${product.name} - ${product.price} VND 
      <button onclick="addToCart(${product.id})">Add</button>`;
    productList.appendChild(div);
  });
}

function renderCart() {
  cartList.innerHTML = "";
  let total = 0;
  cart.forEach((item, index) => {
    total += item.price;
    const div = document.createElement("div");
    div.className = "cart-item";
    div.innerHTML = `<span>${item.name} - ${item.price} VND</span>
      <button onclick="removeFromCart(${index})">Remove</button>`;
    cartList.appendChild(div);
  });
  totalEl.innerText = total.toLocaleString();
}

function addToCart(id) {
  const product = products.find(p => p.id === id);
  cart.push(product);
  renderCart();
}

function removeFromCart(index) {
  cart.splice(index, 1);
  renderCart();
}

// Initialize
renderProducts();
renderCart();
