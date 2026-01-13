from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from ..services.domain_intel import analyze_domain
router = APIRouter()

class DomainRequest(BaseModel):
    domain: str = Field(..., max_length=253)

@router.post("/domain")
async def domain_lookup(request: DomainRequest):
    return await analyze_domain(request.domain)