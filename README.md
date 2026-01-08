# Trading API Simulation – Bajaj Broking Assignment

This project implements a simplified trading backend system as part of the Bajaj Broking campus hiring assignment.  
The application simulates core trading workflows commonly found in online stock broking platforms, including instrument discovery, order placement, trade execution, and portfolio tracking.  
The system is designed for simulation and testing purposes only and does not integrate with real market data or live trading systems.

---

## Objective

The objective of this assignment is to demonstrate:

- Backend system design and code structure  
- RESTful API development  
- Understanding of fundamental trading domain concepts such as orders, trades, and portfolio holdings  

---

## Tech Stack

- **Language:** Python 3.13  
- **Framework:** FastAPI  
- **Data Validation:** Pydantic  
- **Storage:** In-memory data structures  
- **Testing:** Pytest  
- **Frontend:** HTML, CSS, Vanilla JavaScript  

---

## High-Level System Design

The application follows a layered architecture:

- **API Layer (Routers):** Handles HTTP requests and responses  
- **Service Layer:** Contains business logic and trading workflows  
- **Repository Layer:** Manages in-memory data storage  

The system models core trading entities explicitly:

- Instruments  
- Orders  
- Trades  
- Portfolio holdings  

No authentication is used and the system is simulated using a single hardcoded user.

---

## Features Implemented

- Fetch list of tradable instruments  
- Place BUY orders  
- Support for MARKET and LIMIT order types  
- Automatic trade generation for executed orders  
- Portfolio based on executed trades  
- Input validation and proper error handling  
- Automated unit tests for core functionality  
- A basic frontend for API interaction  

---

## API Endpoints
- GET /api/v1/instruments
- POST /api/v1/orders
- GET /api/v1/orders/{orderId}
- GET /api/v1/trades
- GET /api/v1/portfolio

Interactive API documentation is available via Swagger UI:  http://127.0.0.1:8000/docs

---

## Order Execution Logic

- MARKET orders are executed immediately at the instrument’s last traded price  
- LIMIT orders require a price and are validated against instrument data  
- Only EXECUTED orders generate trades  
- Portfolio holdings are derived from executed trades  

---

## Assumptions & Limitations

- Single hardcoded user (no authentication system)  
- Static list of predefined instruments  
- Fixed last traded prices (no live market data)  
- No partial order fills  
- No order cancellation or modification  
- In-memory storage (application restart resets data)  

---

## Setup & Run Instructions

### 1. Clone the repository

```bash
git clone https://github.com/ChaitanyaSekra/Bajaj-Broking-SDK.git
cd Bajaj-Assignment
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn app.main:app --reload
```
---

## Testing

APIs were tested using:

- Swagger UI
- curl commands
- Automated unit tests using pytest

To run tests:
```bash
pytest
```
---

## Demo Frontend

A simple HTML + JavaScript frontend is included to demonstrate API usage and trading workflows.

How to run:
- Start the backend server

- Open http://127.0.0.1:5500/frontend/index.html in a browser

Use the UI to:

- View instruments
- Place market orders
- View trades
- View portfolio holdings
