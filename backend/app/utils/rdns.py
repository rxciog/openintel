import socket
import dns.resolver

def reverse_dns_lookup(ip: str) -> str | None:
    try: 
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    #except (socket.error, socket.gaierror, TimeoutError):
    except Exception  as e:
        print(e)
        return None
    
def extract_base_domain(hostname: str) -> str | None:
    if not hostname:
        return None
    
    parts = hostname.split(".")
    if len(parts) < 2:
        return None
    
    return ".".join(parts[-2:])

def dns_lookup(domain: str) -> str | None:
    try: 
        ip, _, _ = socket.gethostbyname(domain)
        return ip
    except (socket.error, socket.gaierror, TimeoutError):
        return None
    
def get_a_records(domain: str) -> list | str :
    try: 
        a_records = dns.resolver.resolve(domain, 'A')

        result = [str(ip) for ip in a_records]
    
    except Exception as e:
        result = f"DNS Error: {str(e)}"

    return result

def get_mx_records(domain: str) -> list | None :
    try:  
        mx_records = dns.resolver.resolve(domain, 'MX')

        result = [str(mx.exchange) for mx in mx_records]
    except Exception as e:
        result = f"DNS Error: {str(e)}"

    return result

