<template>
  <ResultCard title="Network & Infrastructure">
    <template #icon>
        <svg 
          xmlns="http://www.w3.org/2000/svg" 
          width="20" 
          height="20" 
          viewBox="0 0 24 24" 
          fill="none" 
          stroke="currentColor" 
          stroke-width="2" 
          stroke-linecap="round" 
          stroke-linejoin="round" 
          class="glow-icon"
        >
          <circle cx="12" cy="12" r="3"/>
          <line x1="19.4" y1="4.6" x2="14.1" y2="9.9"/>
          <line x1="21" y1="12" x2="15" y2="12"/>
          <line x1="19.4" y1="19.4" x2="14.1" y2="14.1"/>
          <line x1="12" y1="21" x2="12" y2="15"/>
          <line x1="4.6" y1="19.4" x2="9.9" y2="14.1"/>
          <line x1="3" y1="12" x2="9" y2="12"/>
          <line x1="4.6" y1="4.6" x2="9.9" y2="9.9"/>
          <line x1="12" y1="3" x2="12" y2="9"/>
        </svg>
    </template>
    <div class="network-grid">
      <div v-if="asn" class="row">
        <span class="label">ASN</span>
        <span class="value">{{ asn }}</span>
      </div>

      <div v-if="org" class="row">
        <span class="label">Organization</span>
        <span class="value">{{ org }}</span>
      </div>

      <div v-if="networkName" class="row">
        <span class="label">Network</span>
        <span class="value">{{ networkName }}</span>
      </div>

      <div v-if="cidr" class="row">
        <span class="label">CIDR</span>
        <span class="value monospace">{{ cidr }}</span>
      </div>

      <div v-if="country" class="row">
        <span class="label">Country</span>
        <span class="value">{{ country }}</span>
      </div>

      <div v-if="source" class="row">
        <span class="label">Registry</span>
        <span class="value">{{ source.toUpperCase() }}</span>
      </div>
    </div>
  </ResultCard>
</template>

<script setup lang="ts">
import { computed } from "vue"
import ResultCard from "./ResultCard.vue"

/**
 * data can be:
 * - IP analysis result
 * - domain.ip_intel
 */
const props = defineProps<{
  data: any
}>()

const asn = computed(() => props.data?.asn ?? null)
const org = computed(() => props.data?.asn_description ?? null)
const country = computed(() => props.data?.country ?? null)
const source = computed(() => props.data?.source ?? null)

const networkName = computed(() => props.data?.network?.name ?? null)
const cidr = computed(() => props.data?.network?.cidr ?? null)
</script>


