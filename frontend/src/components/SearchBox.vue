<script setup lang="ts">
import { ref } from 'vue'

const query = ref('')
const emit = defineEmits<{
  (e: 'search', value: string): void
}>()

function submit() {
  if (!query.value.trim()) return
  emit('search', query.value.trim())
}
</script>

<template>
  <div class="input-row">
    <input
      v-model="query"
      placeholder="Enter domain or IP"
      @keyup.enter="submit"
    />
    <button @click="submit">Analyze</button>
  </div>
</template>

<style scoped>
.input-row {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

input {
  flex: 1;
  padding: 0.6rem;
  font-size: 1rem;
  border-radius: 0.5rem;
}

button {
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
  cursor: pointer;
}
</style>
