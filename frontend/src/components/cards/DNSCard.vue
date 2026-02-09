<script setup lang="ts">
import ResultCard from "./ResultCard.vue"
defineProps<{
  ips?: string[]
  mx?: string[]
}>()
</script>


<template>
  <ResultCard title="DNS Records">
    <template #icon>
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="glow-icon">
        <rect x="2" y="2" width="20" height="8" rx="2" ry="2"/>
        <rect x="2" y="14" width="20" height="8" rx="2" ry="2"/>
        <line x1="6" y1="6" x2="6" y2="6"/>
        <line x1="6" y1="18" x2="6" y2="18"/>
      </svg>
    </template>
    <div class="network-grid">
      <div v-if="ips?.length" class="row-group">
        <div class="row" v-for="ip in ips" :key="ip">
          <span class="label">A RECORD</span>
          <span class="value monospace">{{ ip }}</span>
        </div>
      </div>

      <div v-if="mx?.length" class="row-group">
        <div class="row" v-for="record in mx" :key="record">
          <span class="label">MX RECORD</span>
          <span class="value monospace">{{ record }}</span>
        </div>
      </div>
    </div>
  </ResultCard>
</template>

