import pytest
from app.services.ip_intel import analyze_ip

@pytest.mark.asyncio
async def test_analyze_ip_integration():
    """
    Integration test for analyze_ip using a live public IP (Google DNS).
    """
    target_ip = "8.8.8.8"
    
    # Act
    result = await analyze_ip(target_ip)
    
    assert result["asn"] == '15169'
    assert "GOGL" in result["network"]["name"]
    
    # Reverse DNS (PTR) results
    assert result["rdns_available"] is True
    assert "dns.google" in result["ptr"]
    assert result["ptr_domain"] == "dns.google"