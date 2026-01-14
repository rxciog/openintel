from ..utils.rdap.ip import look_up_rdap_ip
from ..utils.rdns import reverse_dns_lookup, extract_base_domain
from .cache import cache
import logging
logger = logging.getLogger(__name__)
IP_TTL = 60 * 60

async def analyze_ip(ip: str) -> dict:
    """
    Perform passive OSINT enrichment on an IP address
    """
    result = {}
    cache_key = f"ip:{ip}"
    cached = cache.get(cache_key)
    if cached:
        logger.info(f"Cache hit for IP: {ip}")
        return cached
    
    rdap_data = await look_up_rdap_ip(ip)
    if rdap_data:
        result.update(rdap_data)

    ptr = reverse_dns_lookup(ip)
    result["ptr"] = ptr
    result["ptr_domain"] = extract_base_domain(ptr)
    result["rdns_available"] = ptr is not None

    cache.set(cache_key, result, IP_TTL)
    return result


