import pytest
import socket
from app.utils.rdns import reverse_dns_lookup, extract_base_domain, dns_lookup, get_a_records, get_mx_records

def test_reverse_dns_lookup_success(mocker):
    mock_socket = mocker.patch('app.utils.rdns.socket.gethostbyaddr')
    mock_socket.return_value = ('google.com', [], [])
    assert reverse_dns_lookup('8.8.8.8') == "google.com"

def test_reverse_dns_lookup_success(mocker):
    mock_socket = mocker.patch('app.utils.rdns.socket.gethostbyaddr', side_effect =socket.error)

    assert reverse_dns_lookup('0.0.0.0') == None

def test_extract_base_domain():
    assert extract_base_domain("sub.example.com") == "example.com"
    assert extract_base_domain("example.com") == "example.com"
    assert extract_base_domain("localhost") is None
    assert extract_base_domain("") is None

def test_dns_lookup_success(mocker):
    mock_socket = mocker.patch('app.utils.rdns.socket.gethostbyname')
    mock_socket.return_value = ('8.8.8.8', [], [])
    assert dns_lookup('google.com') == "8.8.8.8"

def test_dns_lookup_fail(mocker):
    mock_socket = mocker.patch('app.utils.rdns.socket.gethostbyname', side_effect=socket.error)

    assert dns_lookup('odd.com') == None

def test_get_a_records_success(mocker):
    mock_resolve = mocker.patch('app.utils.rdns.dns.resolver.resolve')
    mock_resolve.return_value = ['1.1.1.1', '8.8.8.8']

    result = get_a_records("google.com")

    assert isinstance(result, list)
    assert "1.1.1.1" in result
    assert len(result) == 2

def test_get_a_records_fail(mocker):
    mocker.patch('app.utils.rdns.dns.resolver.resolve', side_effect=Exception("DNS Timeout"))

    result = get_a_records("this-domain-does-not-exist.com")

    assert result is None

def test_get_mx_records_success(mocker):
    #MX records have an 'exchange' attribute in dns.resolver
    mock_mx1 = mocker.Mock()
    mock_mx1.exchange = "mail.example.com"
    mock_mx2 = mocker.Mock()
    mock_mx2.exchange = "backup-mail.example.com"

    mock_resolve = mocker.patch('app.utils.rdns.dns.resolver.resolve')
    mock_resolve.return_value = [mock_mx1, mock_mx2]

    result = get_mx_records("example.com")

    assert result == ["mail.example.com", "backup-mail.example.com"]

def test_get_mx_records_fail(mocker):
    mocker.patch('app.utils.rdns.dns.resolver.resolve', side_effect=Exception("No MX records"))

    result = get_mx_records("example.com")

    assert result is None