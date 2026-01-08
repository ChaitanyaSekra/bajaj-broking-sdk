const BASE_URL = "http://127.0.0.1:8000/api/v1";

async function loadInstruments() {
  const res = await fetch(`${BASE_URL}/instruments`);
  const data = await res.json();

  const list = document.getElementById("instruments");
  list.innerHTML = "";

  data.forEach(i => {
    const li = document.createElement("li");
    li.innerText = `${i.symbol} (${i.exchange}) - ₹${i.lastTradedPrice}`;
    list.appendChild(li);
  });
}

async function placeOrder() {
  const symbol = document.getElementById("symbol").value;
  const quantity = parseInt(document.getElementById("quantity").value);

  const res = await fetch(`${BASE_URL}/orders`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      symbol: symbol,
      side: "BUY",
      orderType: "MARKET",
      quantity: quantity
    })
  });

  const data = await res.json();
  alert(`Order Status: ${data.status}`);
}

async function loadTrades() {
  const res = await fetch(`${BASE_URL}/trades`);
  const data = await res.json();
  document.getElementById("trades").innerText =
    JSON.stringify(data, null, 2);
}

async function loadPortfolio() {
  const res = await fetch(`${BASE_URL}/portfolio`);
  const data = await res.json();
  document.getElementById("portfolio").innerText =
    JSON.stringify(data, null, 2);
}
