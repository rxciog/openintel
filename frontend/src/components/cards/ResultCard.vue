<template>
  <div class="result-card">
    <div class="header">
      <slot name="icon"></slot><h3 class="title">{{ title }}</h3>
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
  background: rgba(28, 31, 38, 0.8); /* Semi-transparent for glass effect */
  backdrop-filter: blur(8px);      
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 16px;
  padding: 20px;
  
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.4), 
              0 0 15px rgba(59, 130, 246, 0.05); 
  
  transition: all 0.3s ease;
}

.result-card:hover {
  border-color: rgba(59, 130, 246, 0.5);
  box-shadow: 0 0 30px rgba(59, 130, 246, 0.15);
  transform: translateY(-2px);
}

.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 12px;
}

.title-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.title {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-main);
}

.subtitle {
  color: var(--text-muted);
  font-size: 0.8rem;
  display: block;
  margin-top: 4px;
}

.glow-icon {
  color: #3b82f6; 
  filter: drop-shadow(0 0 5px rgba(59, 130, 246, 0.6));
  flex-shrink: 0;
  margin-right: 8px; 
}

.title-row {
  display: flex;
  align-items: center;
}
</style>
