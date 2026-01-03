from fastapi import FastAPI
from .routers import ip, domain
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="OpenIntel API",
    description="Passive OSINT enrichment API for IP and domain intelligence",
    version="0.1.0",
)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ip.router, prefix="", tags=["ip"])
app.include_router(domain.router, prefix="", tags=["domain"])

@app.get("/health")
def health():
    return {"status": "ok"}
