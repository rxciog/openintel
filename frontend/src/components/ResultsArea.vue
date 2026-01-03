<template>
  <div v-if="result" class="results">
    <IPResults
      v-if="type === 'ip'"
      :ip="query"
      :result="result"
    />

    <DomainResults
      v-else-if="type === 'domain'"
      :domain="query"
      :result="result"
    />
  </div>
</template>

<script setup lang="ts">
import IPResults from "./results/IPResults.vue"
import DomainResults from "./results/DomainResults.vue"

defineProps<{
  result: any
  type: "ip" | "domain"
  query: string
}>()
</script>

<style scoped>
.results {
  margin-top: 24px;
}
</style>
