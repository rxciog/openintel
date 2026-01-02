from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.domain_intel import analyze_domain
router = APIRouter()

class DomainRequest(BaseModel):
    value: str

@router.post("/domain")
async def domain_lookup(request: DomainRequest):
    return await analyze_domain(request.value)