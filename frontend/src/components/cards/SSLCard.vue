<script setup lang="ts">
import ResultCard from "./ResultCard.vue"

defineProps<{
  issuer: string
  subject: string
  expires: string
  version: string
}>()
</script>


<template>
  <ResultCard title="SSL Certificate">
    <template #icon>
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="glow-icon">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
      </svg>
    </template>
    <div class="network-grid">
      <div class="row">
        <span class="label">Issuer</span>
        <span class="value">{{ issuer }}</span>
      </div>

      <div class="row">
        <span class="label">Subject</span>
        <span class="value">{{ subject }}</span>
      </div>

      <div class="row">
        <span class="label">Expires</span>
        <span class="value monospace">{{ expires }}</span>
      </div>

      <div class="row">
        <span class="label">Version</span>
        <span class="value">{{ version }}</span>
      </div>
    </div>
  </ResultCard>
</template>

