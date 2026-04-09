"""B3 SOC Brain – FastAPI entry point."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="B3 SOC Brain API",
    description="Autonomous Cyber Defense SaaS – threat detection and rule engine.",
    version="1.0.0",
)


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@app.get("/health", response_model=HealthResponse, tags=["health"])
def health() -> HealthResponse:
    """Return service health status."""
    return HealthResponse(status="ok", service="b3-soc-brain-api", version="1.0.0")


@app.get("/api/v1/status", tags=["status"])
def status() -> dict:
    """Return platform operational status."""
    return {
        "autonomous_ai": "running",
        "threat_graph": "connected",
        "rule_engine": "active",
    }
