<script setup lang="ts">
import SummaryCard from "./cards/SummaryCard.vue"
import NetworkCard from "./cards//NetworkCard.vue"
import DNSCard from "./cards/DNSCard.vue"
import SSLCard from "./cards/SSLCard.vue"
import LoadingSpinner from "./LoadingSpinner.vue"


defineProps<{
  loading: boolean
  error: string | null
  result: {
    kind: 'ip' | 'domain'
    data: any
  } | null
}>()
</script>

<template>
  <section class="results">
    <LoadingSpinner v-if="loading" />

    <div v-else-if="error" class="error-container">
      <div class="error-content">
        <span class="error-icon">⚠️</span>
        <p>{{ error }}</p>
      </div>
    </div>
    
    <div v-else-if="result">
      <h3>{{ result.kind.toUpperCase() }} Analysis</h3>
      <div class="cards">
        <!-- Always show summary -->
        <SummaryCard
          :type="result.kind"
          :value="result.kind === 'ip' ? result.data.ip : result.data.domain"
          :data="result.data"
        />
        <!-- IP-specific -->
        <NetworkCard
          v-if="result.kind === 'ip'"
          :data="result.data"
        />
  
        <!-- Domain-specific -->
        <NetworkCard
          v-else-if="result.kind === 'domain' && result.data.ip_intel"
          :data="result.data.ip_intel"
        />
        
        <SSLCard
          v-if="result.data.ssl"
          :issuer="result.data.ssl.issuer"
          :subject="result.data.ssl.subject"
          :expires="result.data.ssl.expires"
          :version="result.data.ssl.version"
        />

        <DNSCard 
          v-if="result.kind === 'domain' && result.data.dns"
          :ips="result.data.dns.ips"
          :mx="result.data.dns.mx"
        />
  
        
      </div>  
      
    </div>

    <p v-else class="placeholder">Results will appear here</p>
  </section>
</template>


<style scoped>
.results {
  border: 1px solid #3a3939;
  border-radius: .5rem;
  padding: 1rem;
  min-height: 200px;
  max-width: 1200px;
  margin: 0 auto
}

.placeholder {
  color: #888;
  font-style: italic;
}

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.error-container {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.error-content {
  background: rgba(220, 38, 38, 0.1);
  border: 1px solid rgba(220, 38, 38, 0.4);
  color: #fca5a5;
  padding: 1rem 2rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 0 15px rgba(220, 38, 38, 0.2);
}

.error-icon {
  font-size: 1.2rem;
}
</style>
