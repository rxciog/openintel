from ipwhois import IPWhois
from ipwhois.exceptions import IPDefinedError


async def look_up_rdap_ip(ip: str) -> dict | None:
    try:
        obj = IPWhois(ip, timeout=5)
        result = obj.lookup_rdap()

        network = result.get("network", {})

        return {
            "asn": result.get("asn"),
            "asn_description": result.get("asn_description"),
            "country": result.get("asn_country_code"),
            "network": {
                "name": network.get("name"),
                "cidr": network.get("cidr"),
                "start_address": network.get("start_address"),
                "end_address": network.get("end_address"),
            },
            "source": result.get("asn_registry")
        }
    except IPDefinedError:
        return None
    except Exception as e:
        return None




