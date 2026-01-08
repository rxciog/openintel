import ssl
import socket
from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_ssl_certificate_info(target: str, port: int = 443):
    context = ssl.create_default_context()

    # Allow self signed or expired certs
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        with socket.create_connection((target,port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                bin_cert = ssock.getpeercert(binary_form=True)
                cert = x509.load_der_x509_certificate(bin_cert, default_backend())

                issuer = cert.issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME)
                subject = cert.issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME)

                expires = cert.not_valid_after_utc
                now = datetime.now(timezone.utc)
                is_valid = (
                    cert.not_valid_before_utc <= now <= cert.not_valid_after_utc
                )


                return {
                    "issuer": issuer[0].value if issuer else "Unknown",
                    "subject": subject[0].value if subject else "Unknown",
                    "expires": expires.isoformat(),
                    "version": ssock.version(),
                    "valid": is_valid,
                    "error": None
                }

    except Exception as e:
        return {
            "issuer": None,
            "subject": None,
            "expires": None,
            "version": None,
            "valid": False,
            "error": str(e)
        }