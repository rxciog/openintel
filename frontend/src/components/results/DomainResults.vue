<template>
  <div class="stack">
    <SummaryCard
      type="domain"
      :value="domain"
      :data="result"
    />

    <NetworkCard
      v-if="result.ip_intel"
      :data="result.ip_intel"
    />
  </div>
</template>

<script setup lang="ts">
import SummaryCard from "../cards/SummaryCard.vue"
import NetworkCard from "../cards/NetworkCard.vue"

defineProps<{
  domain: string
  result: any
}>()
</script>

<style scoped>
.stack {
  display: grid;
  gap: 16px;
}
</style>
