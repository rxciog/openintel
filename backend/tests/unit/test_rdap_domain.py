import pytest
from app.utils.rdap.domain import look_up_radp_domain

@pytest.mark.asyncio
async def test_look_up_rdap_domain_success(mocker):
    mock_whoisit = mocker.patch('app.utils.rdap.domain.whoisit.domain')
    mock_whoisit.return_value = {
            'entities': {
                'registrar': [{'name': 'Name'}]  
                },
            "registration_date": 'YYYY:MM:DD',
            "last_changed_date": 'YYYY:MM:DD',
            "expiration_date": 'YYYY:MM:DD',
            "nameservers": ['name1', 'name2'],
            "status": ['active'],
            "url": 'site.io'
    }

    result = await look_up_radp_domain('https://site.io/profile')

    assert result["raw_url"] == "site.io"
    assert result["name_servers"][0] == "name1"

@pytest.mark.asyncio
async def test_look_up_rdap_domain_fail(mocker):
     mocker.patch('app.utils.rdap.domain.whoisit.domain', side_effect=Exception)

     result = await look_up_radp_domain('https://sus.ai/34Wawr79swgg')
     assert result is None


