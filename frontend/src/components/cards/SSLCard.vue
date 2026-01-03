<script setup lang="ts">
defineProps<{
  issuer: string
  subject: string
  expires: string
  version: string
}>()
</script>


<template>
  <div class="card">
    <h3>SSL Certificate</h3>

    <div class="row">
      <span class="label">Issuer</span>
      <span class="value">{{ issuer }}</span>
    </div>

    <div class="row">
      <span class="label">Subject</span>
      <span class="value">{{ subject }}</span>
    </div>

    <div class="row">
      <span class="label">Expires</span>
      <span class="value">{{ expires }}</span>
    </div>

    <div class="row">
      <span class="label">Version</span>
      <span class="value">{{ version }}</span>
    </div>
  </div>
</template>

