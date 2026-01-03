<script setup lang="ts">
import SummaryCard from "./cards/SummaryCard.vue"
import NetworkCard from "./cards//NetworkCard.vue"
import DNSCard from "./cards/DNSCard.vue"
import SSLCard from "./cards/SSLCard.vue"


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
    <p v-if="loading">Analyzing…</p>

    <p v-else-if="error" class="error">{{ error }}</p>
    
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
           :records="result.data.dns"
         />
  
        
      </div>  
      
    </div>

    <p v-else class="placeholder">Results will appear here</p>
  </section>
</template>


<style scoped>
.results {
  border: 1px solid #ddd;
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

</style>
