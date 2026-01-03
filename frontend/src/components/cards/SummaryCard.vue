<template>
  <ResultCard :title="title" :subtitle="subtitle">
    <div class="summary-grid">
      <div class="row">
        <span class="label">Type</span>
        <span class="value">{{ typeLabel }}</span>
      </div>

      <div v-if="provider" class="row">
        <span class="label">Provider</span>
        <span class="value">{{ provider }}</span>
      </div>

      <div v-if="country" class="row">
        <span class="label">Country</span>
        <span class="value">{{ country }}</span>
      </div>

      <div v-if="ptrDomain" class="row">
        <span class="label">Reverse DNS</span>
        <span class="value monospace">{{ ptrDomain }}</span>
      </div>

      <div v-if="sslStatus" class="row">
        <span class="label">TLS</span>
        <span
          class="value"
          :class="sslStatus === 'Valid' ? 'ok' : 'bad'"
        >
          {{ sslStatus }}
        </span>
      </div>
    </div>
  </ResultCard>
</template>

<script setup lang="ts">
import { computed } from "vue"
import ResultCard from "./ResultCard.vue"

const props = defineProps<{
  type: "ip" | "domain"
  value: string
  data: any
}>()

const title = computed(() =>
  props.type === "ip" ? "IP Summary" : "Domain Summary"
)

const subtitle = computed(() => props.value)

const typeLabel = computed(() =>
  props.type === "ip" ? "IP Address" : "Domain"
)

const provider = computed(() => {
  if (props.type === "ip") {
    return props.data?.asn_description ?? null
  }
  return props.data?.ip_intel?.asn_description ?? null
})

const country = computed(() => {
  if (props.type === "ip") {
    return props.data?.country ?? null
  }
  return props.data?.ip_intel?.country ?? null
})

const ptrDomain = computed(() => {
  if (props.type !== "ip") return null
  return props.data?.ptr_domain ?? null
})

const sslStatus = computed(() => {
  if (props.type !== "domain") return null
  if (!props.data?.ssl) return null
  return props.data.ssl.valid ? "Valid" : "Invalid"
})
</script>

<style scoped>
.ok {
  color: #059669;
}

.bad {
  color: #dc2626;
}
</style>
