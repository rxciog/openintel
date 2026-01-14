import pytest
from app.services.domain_intel import extract_domain, analyze_domain

@pytest.mark.parametrize("input_url, expected", [
    ("https://www.google.com/search", "google.com"),
    ("google.com", "google.com"),
    ("  WWW.EXAMPLE.IO  ", "example.io"),
    ("", None),
    ("   ", None)
])
def test_extract_domain(input_url, expected):
    assert extract_domain(input_url) == expected

@pytest.mark.asyncio
async def test_analyze_domain_flow(mocker):
    # Mock all imported utilities
    mock_cache = mocker.patch('app.services.domain_intel.cache')
    mocker.patch('app.services.domain_intel.logger')
    
    # Ensure cache returns None (Cache Miss)
    mock_cache.get.return_value = None

    mock_a = mocker.patch('app.services.domain_intel.get_a_records')
    mock_mx = mocker.patch('app.services.domain_intel.get_mx_records')
    mock_rdap_dom = mocker.patch('app.services.domain_intel.look_up_radp_domain')
    mock_rdap_ip = mocker.patch('app.services.domain_intel.look_up_rdap_ip')
    mock_ssl = mocker.patch('app.services.domain_intel.get_ssl_certificate_info')

    # Set return values
    mock_a.return_value = ["1.1.1.1"]
    mock_mx.return_value = ["mail.site.io"]
    mock_rdap_dom.return_value = {"registrar": "TestReg"}
    mock_rdap_ip.return_value = {"asn": "123"}
    mock_ssl.return_value = {"valid": True}

    result = await analyze_domain("https://site.io")

    assert result["domain"] == "site.io"
    assert result["dns"]["ips"] == ["1.1.1.1"]
    assert result["registration"]["registrar"] == "TestReg"
    assert result["ip_intel"]["asn"] == "123"
    assert result["ssl"]["valid"] is True

    # Verify cache was set
    mock_cache.set.assert_called_once()

    # Check that IP lookup was called with the result from DNS lookup
    mock_rdap_ip.assert_called_once_with("1.1.1.1")

@pytest.mark.asyncio
async def test_analyze_domain_cache_hit(mocker):
    mock_cache = mocker.patch('app.services.domain_intel.cache')
    mocker.patch('app.services.domain_intel.logger')
    
    cached_data = {"domain": "cached.com", "cached": True}
    mock_cache.get.return_value = cached_data

    # This should return immediately without calling any lookups
    result = await analyze_domain("cached.com")

    assert result == cached_data
    mock_cache.get.assert_called_with("domain:cached.com")
    # Verify that a lookup function was NOT called
    assert mocker.patch('app.services.domain_intel.get_a_records').call_count == 0

@pytest.mark.asyncio
async def test_analyze_domain_invalid_input(mocker):
    # Should return the error message dictionary if domain extraction fails
    result = await analyze_domain("")
    assert result["valid"] is False
    assert "message" in result