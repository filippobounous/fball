"""Investment FastAPI application.

Run with::

    uvicorn api.investment.main:app --reload
"""

from fastapi import APIRouter, Depends, FastAPI

from investment.config import FASTAPI_INVESTMENT_API_KEY

from .core import router as core_router
from .analytics import router as analytics_router
from ..security import create_api_key_dependency

ROUTERS: list[APIRouter] = [core_router, analytics_router]

app = FastAPI(
    title="Investment API",
    dependencies=[Depends(create_api_key_dependency(FASTAPI_INVESTMENT_API_KEY))],
)

@app.get("/")
async def read_root() -> dict[str, str]:
    """Basic message showing the investment API is running."""
    return {"message": "Welcome to the Investment API"}

@app.get("/health")
async def health_check() -> dict[str, str]:
    """Simple health check for the investment API."""
    return {"status": "ok"}

for router in ROUTERS:
    app.include_router(router)
