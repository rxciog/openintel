<template>
  <div class="result-card">
    <div class="header">
      <h3 class="title">{{ title }}</h3>
      <span v-if="subtitle" class="subtitle">{{ subtitle }}</span>
    </div>

    <div class="content">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  subtitle?: string
}>()
</script>

<style scoped>
.result-card {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 16px;
  background: #ffffff;
}

.header {
  margin-bottom: 12px;
}

.title {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  color: #111827;
}

.subtitle {
  display: block;
  margin-top: 2px;
  font-size: 0.85rem;
  color: #6b7280;
}

.content {
  font-size: 0.9rem;
  color: #374151;
}
</style>
