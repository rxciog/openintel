import pytest
from app.utils.rdap.ip import look_up_rdap_ip

@pytest.mark.asyncio
async def test_look_up_rdap_ip_success(mocker):
    mock_whois = mocker.patch('app.utils.rdap.ip.IPWhois')
    mock_instance = mock_whois.return_value
    mock_instance.lookup_rdap.return_value = {
       "asn": "1234",
        "asn_description": "Test ISP",
        "country": "X",
        "network": {
            "name": "Test Net",
            "cidr": "1.1.1.0/24",
            "start_address": "1.1.1.0",
            "end_address": "1.1.1.255",
        },
        "source": "-"
    }

    result = await look_up_rdap_ip("1.1.1.1")

    assert result["asn"] == "1234"
    assert result["network"]["name"] == "Test Net"

@pytest.mark.asyncio
async def test_look_up_rdap_ip_fail(mocker):
    from ipwhois.exceptions import IPDefinedError
    mocker.patch('app.utils.rdap.ip.IPWhois', side_effect=IPDefinedError)

    result = await look_up_rdap_ip("127.0.0.1")
    assert result is None

@pytest.mark.asyncio
async def test_look_up_rdap_ip_invalid(mocker):
    from ipwhois.exceptions import IPDefinedError
    mocker.patch('app.utils.rdap.ip.IPWhois', side_effect=Exception)

    result = await look_up_rdap_ip("127.0.0")
    assert result is None