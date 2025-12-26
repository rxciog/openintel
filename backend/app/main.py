from fastapi import FastAPI
from .routers import ip, domain

app = FastAPI(
    title="OpenIntel API",
    description="Passive OSINT enrichment API for IP and domain intelligence",
    version="0.1.0",
)

app.include_router(ip.router, prefix="/analyze", tags=["ip"])
app.include_router(domain.router, prefix="/analyze", tags=["domain"])

@app.get("/health")
def health():
    return {"status": "ok"}
