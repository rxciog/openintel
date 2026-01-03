<template>
  <ResultCard title="Network & Infrastructure">
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


