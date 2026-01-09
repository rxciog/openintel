import pytest
from app.services.ip_intel import analyze_ip


@pytest.mark.asyncio
async def test_analyze_ip_success(mocker):
    mock_rdap = mocker.patch('app.services.ip_intel.look_up_rdap_ip')
    mock_ptr = mocker.patch('app.services.ip_intel.reverse_dns_lookup')
    mock_base = mocker.patch('app.services.ip_intel.extract_base_domain')

    mock_rdap.return_value = {
        "asn": "AS15169",
        "asn_description": "Google LLC",
        "country": "US",
        "network": {"name": "GOOGLE", "cidr": "8.8.8.0/24"}
    }
    mock_ptr.return_value = "dns.google"
    mock_base.return_value = "google.com"

    result = await analyze_ip("8.8.8.8")

    assert result["asn"] == "AS15169"
    assert result["ptr"] == "dns.google"
    assert result["ptr_domain"] == "google.com"
    assert result["rdns_available"] is True
    mock_rdap.assert_called_once_with("8.8.8.8")


@pytest.mark.asyncio
async def test_analyze_ip_no_rdap_data(mocker):
    mocker.patch('app.services.ip_intel.look_up_rdap_ip', return_value=None)
    mocker.patch('app.services.ip_intel.reverse_dns_lookup', return_value="some.host")
    mocker.patch('app.services.ip_intel.extract_base_domain', return_value="host")

    result = await analyze_ip("1.1.1.1")

    # Result should still contain DNS data even if RDAP is None
    assert result["ptr"] == "some.host"
    assert result["rdns_available"] is True

    assert "asn" not in result

@pytest.mark.asyncio
async def test_analyze_ip_no_dns(mocker):
    mocker.patch('app.services.ip_intel.look_up_rdap_ip', return_value={"asn": "123"})
    mocker.patch('app.services.ip_intel.reverse_dns_lookup', return_value=None)
    mocker.patch('app.services.ip_intel.extract_base_domain', return_value=None)

    result = await analyze_ip("192.168.1.1")

    assert result["rdns_available"] is False
    assert result["ptr"] is None
    assert result["asn"] == "123"