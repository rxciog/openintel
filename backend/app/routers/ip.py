from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, IPvAnyAddress
from ..services.ip_intel import analyze_ip
from ..services.rdap import look_up_rdap

router = APIRouter()

class IPRequest(BaseModel):
    ip : IPvAnyAddress


@router.post("/ip")
def analyze(request: IPRequest):
    return look_up_rdap(str(request.ip))