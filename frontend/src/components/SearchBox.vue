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
  align-items: center;
}

input {
  flex: 1;
  background: rgb(218, 211, 211);
  border: 1px solid rgb(54, 54, 201);
  border-radius: 1rem;
  color: rgb(64, 64, 65);
  padding: 12px;
  font-size: 1rem;
  font-weight: 600;
  outline: none;
}

button {
  background: var(--accent-blue);
  color: white;
  border: 1px solid rgb(69, 131, 202);
  padding: 13px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.2s;
}

button:hover {
  opacity: 0.9;
  border: 1px solid rgb(69, 202, 191);
}
</style>
