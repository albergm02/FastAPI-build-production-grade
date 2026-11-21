from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import orders as orders_router, stats as stats_router
from database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    create_tables()
    yield
    # Perform any cleanup tasks here if needed
    print("Application shutdown: Cleanup tasks completed.")

app = FastAPI(
    title="Dabbe Wala API",
    description="API for managing orders and statistics in the Dabbe Wala application.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(orders_router.router)
app.include_router(stats_router.router)

app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy"}
