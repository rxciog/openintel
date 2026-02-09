
function isIp(value: string): boolean {
  // IPv4 or IPv6 
  return /^[0-9.:]+$/.test(value)
}

function normalizeDomain(input: string): string {
  try {
    if (input.startsWith('http')) {
      return new URL(input).hostname
    }
  } catch {
    // fall through
  }
  return input
}

export async function analyze(query: string) {
  const isIP = isIp(query)
  const endpoint = isIP ? '/ip' : '/domain'
  const payload = isIP
    ? { ip: query }
    : { domain: normalizeDomain(query) }

  const res = await fetch(`api/${endpoint}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  })

  if (!res.ok) {
    let errorMessage = 'Request failed';
    try {
      const errorData = await res.json();
      
      // Check if it's a validation error (e.g., from FastAPI/Pydantic)
      if (errorData.detail && Array.isArray(errorData.detail)) {
        // Extract the first error message (e.g., "value is not a valid IPv4 address")
        errorMessage = errorData.detail[0].msg || 'Invalid input format';
      } else {
        errorMessage = errorData.message || errorData.error || errorMessage;
      }
    } catch {
      const text = await res.text();
      errorMessage = text || errorMessage;
    }
    throw new Error(errorMessage);
  }

  return {
    kind: isIP ? 'ip' : 'domain',
    data: await res.json()
  }
}
