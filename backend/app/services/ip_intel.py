from ..utils.rdap.ip import look_up_rdap_ip
from ..utils.rdns import reverse_dns_lookup, extract_base_domain

async def analyze_ip(ip: str) -> dict:
    """
    Perform passive OSINT enrichment on an IP address
    """
    result = {}

    rdap_data = await look_up_rdap_ip(ip)
    if rdap_data:
        result.update(rdap_data)

    ptr = reverse_dns_lookup(ip)
    result["ptr"] = ptr
    result["ptr_domain"] = extract_base_domain(ptr)
    result["rdns_available"] = ptr is not None

    return result


