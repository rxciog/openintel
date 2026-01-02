
import whoisit

# Whoisit initialize
whoisit.bootstrap()

async def look_up_radp_domain(domain: str) -> dict | None:
    try:
        domain_info = whoisit.domain(domain)

        return {
            "registrar_name": domain_info['entities']['registrar'][0]['name'],
            "registration_date": domain_info.get('registration_date'),
            "last_changed_date": domain_info.get("last_changed_date"),
            "expires": domain_info.get('expiration_date'),
            "name_servers": domain_info.get('nameservers'),
            "status": domain_info.get('status'),
            "raw_url": domain_info.get('url')
        }
    except Exception as e:
        return None