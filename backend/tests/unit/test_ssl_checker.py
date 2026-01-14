import pytest
from app.utils.ssl_checker import get_ssl_certificate_info
from datetime import timezone, datetime, timedelta

@pytest.mark.parametrize("is_expired, expected_valid", [
    (False, True), # Test case: Cert is within valid dates
    (True, False)  # Test case: Cert is expired
])

def test_get_ssl_certificate_info_validity(mocker, is_expired, expected_valid):
    # Mock dates
    now = datetime(2026, 1, 8, tzinfo=timezone.utc)
    mocker.patch('app.utils.ssl_checker.datetime').now.return_value = now

    if is_expired:
        not_before = now - timedelta(days=10)
        not_after = now - timedelta(days=1)
    else:
        not_before = now - timedelta(days=1)
        not_after = now + timedelta(days=1)

    #Mock socket
    mock_sock = mocker.patch('app.utils.ssl_checker.socket.create_connection')

    #Mock SSL context and wrapped socket
    mock_context = mocker.patch('app.utils.ssl_checker.ssl.create_default_context')
    mock_ssock = mock_context.return_value.wrap_socket.return_value.__enter__.return_value

    mock_ssock.version.return_value = "TLSv1.3"
    mock_ssock.getpeercert.return_value = b"binary_cert_data"

    mock_cert = mocker.Mock()
    mock_cert.not_valid_after_utc = not_after
    mock_cert.not_valid_before_utc = not_before


    mock_attr = mocker.Mock()
    mock_attr.value = "Test Authority"
    mock_cert.issuer.get_attributes_for_oid.return_value = [mock_attr]

    mocker.patch('app.utils.ssl_checker.x509.load_der_x509_certificate', return_value=mock_cert)

    result = get_ssl_certificate_info("example.com")

    assert result["valid"] == expected_valid
    assert result["error"] is None
    assert result["issuer"] == "Test Authority"
    assert result["version"] == "TLSv1.3"

def test_get_ssl_certificate_info_success(mocker):
    mocker.patch('app.utils.ssl_checker.socket.create_connection', side_effect=Exception("Connection timed out"))

    result = get_ssl_certificate_info("NotADomain.com")

    assert result["valid"] is False
    assert result["error"] == "Connection timed out"