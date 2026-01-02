from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, IPvAnyAddress
from ..services.ip_intel import analyze_ip

router = APIRouter()

class IPRequest(BaseModel):
    ip : IPvAnyAddress


@router.post("/ip")
async def analyze(request: IPRequest):
    return await analyze_ip(str(request.ip))