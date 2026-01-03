<script setup lang="ts">
import SearchBox from '../components/SearchBox.vue'
import ResultPanel from '../components/ResultPanel.vue'
import { ref } from 'vue'
import { analyze } from '../services/api'

const loading = ref(false)
const error = ref<string | null>(null)
const result = ref<any>(null)

async function onSearch(query: string) {
  loading.value = true
  error.value = null
  result.value = null

  try {
    result.value = await analyze(query)
  } catch (e: any) {
    error.value = e.message ?? 'Analysis failed'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <main class="container">
    <h1>OpenIntel</h1>
    <div class="info">
        <SearchBox @search="onSearch" />

        <ResultPanel
          :loading="loading"
          :error="error"
          :result="result"
        />
    </div>
    
  </main>
</template>

<style scoped>
.container {
  margin: 2rem auto;
  padding: 1rem;
}

h1 {
    margin-bottom: 2rem;
}
.info {
    margin: auto;
    max-width: 800px;
}
.subtitle {
  color: #555;
  margin-bottom: 1.5rem;
}
</style>