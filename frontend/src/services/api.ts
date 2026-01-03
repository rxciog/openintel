const API_BASE = 'http://localhost:8000'

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

  const res = await fetch(`${API_BASE}${endpoint}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  })

  if (!res.ok) {
    const text = await res.text()
    throw new Error(text || 'Request failed')
  }

  return {
    kind: isIP ? 'ip' : 'domain',
    data: await res.json()
  }
}
