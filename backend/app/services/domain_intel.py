from urllib.parse import urlparse
from ..utils.rdap.ip import look_up_rdap_ip
from ..utils.rdap.domain import look_up_radp_domain
from ..utils.rdns import get_a_records, get_mx_records
from ..utils.ssl_checker import get_ssl_certificate_info
from .cache import cache
import logging

logger = logging.getLogger(__name__)

DOMAIN_TTL = 60 * 60

def extract_domain(value: str) -> str | None:
    value = value.strip()

    if not value:
        return None
    
    parsed = urlparse(value)

    if not parsed.hostname:
        parsed = urlparse(f"http://{value}")
    
    host = parsed.hostname
    if not host:
        return None
    
    return host.lower().strip('www.')

async def analyze_domain(input_value: str):
    domain = extract_domain(input_value)


    if not domain:
        return {
            "valid": False,
            "message": "Could not extract domain"
        }

    cache_key = f"domain:{domain}"
    cached = cache.get(cache_key)
    if cached: 
        logger.info(f"Cache hit for domain: {domain}")
        return cached

    results = {
        "domain": domain,
        "dns": {},
        "registration": {},
        "ip_intel": [],
        "ssl": {}
    }
    
    # DNs Lookup (A, MX, NS)
    # A records (IPs)
    results["dns"]["ips"] = get_a_records(domain)

    # Mail Servers 
    results["dns"]["ms"] = get_mx_records(domain)
    
    # Domain RDAP
    try:
        results["registration"] = await look_up_radp_domain(domain)
    except Exception as e:
        results["registration"]["error"] = f"{str(e)}"

    if results["dns"].get("ips"):
        primary_ip = results["dns"]["ips"][0]
        results["ip_intel"] = await look_up_rdap_ip(primary_ip)
    
    results["ssl"] = get_ssl_certificate_info(domain)
    
    cache.set(cache_key, results, DOMAIN_TTL)
    return results



