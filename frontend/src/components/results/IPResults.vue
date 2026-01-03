<template>
  <div class="stack">
    <SummaryCard
      type="ip"
      :value="ip"
      :data="result"
    />

    <NetworkCard :data="result" />
  </div>
</template>

<script setup lang="ts">
import SummaryCard from "../cards/SummaryCard.vue"
import NetworkCard from "../cards/NetworkCard.vue"

defineProps<{
  ip: string
  result: any
}>()
</script>

<style scoped>
.stack {
  display: grid;
  gap: 16px;
}
</style>
