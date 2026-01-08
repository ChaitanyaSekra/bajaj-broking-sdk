from fastapi import FastAPI
from app.routers import instruments, orders, trades, portfolio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Trading API Simulation",
    description="Simplified trading backend for campus assignment",
    version="1.0.0"
)

app.include_router(instruments.router)
app.include_router(orders.router)
app.include_router(trades.router)
app.include_router(portfolio.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "running"}
