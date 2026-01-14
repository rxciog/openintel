import pytest
from app.services.domain_intel import analyze_domain

@pytest.mark.asyncio
async def test_analyze_domain_integration():
    """
    Integration test for analyze_domain using a live domain.
    Verifies that real DNS, RDAP, and SSL data is retrieved and aggregated.
    """
    target_domain = "google.com"
    
    results = await analyze_domain(target_domain)
    
    assert results["domain"] == "google.com"
    
    # DNS Data
    assert "ips" in results["dns"]
    assert len(results["dns"]["ips"]) > 0
    assert any("142.25" in ip or "172.217" in ip for ip in results["dns"]["ips"])
    
    # Registration (RDAP) Data
    assert results["registration"] is not None
    assert "registrar_name" in results["registration"]
    assert "Markmonitor Inc." in results["registration"]["registrar_name"]
    
    # IP Intelligence (derived from the first A record)
    assert results["ip_intel"] is not None
    assert "asn" in results["ip_intel"]
    
    # SSL Data
    assert results["ssl"]["valid"] is True
