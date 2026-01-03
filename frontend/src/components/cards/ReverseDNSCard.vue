<script setup lang="ts">
defineProps<{
  hostnames: string[]
}>()
</script>

<template>
  <div class="card">
    <h4>Reverse DNS</h4>

    <ul v-if="hostnames.length">
      <li v-for="h in hostnames" :key="h">{{ h }}</li>
    </ul>

    <p v-else class="muted">No reverse DNS found</p>
  </div>
</template>

