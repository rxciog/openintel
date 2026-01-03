<script setup lang="ts">
defineProps<{
  ips?: string[]
  mx?: string[]
}>()
</script>


<template>
  <div class="card">
    <h3>DNS Records</h3>

    <div v-if="ips?.length" class="row-group">
      <div class="row" v-for="ip in ips" :key="ip">
        <span class="label">A</span>
        <span class="value">{{ ip }}</span>
      </div>
    </div>

    <div v-if="mx?.length" class="row-group">
      <div class="row" v-for="record in mx" :key="record">
        <span class="label">MX</span>
        <span class="value">{{ record }}</span>
      </div>
    </div>
  </div>
</template>

