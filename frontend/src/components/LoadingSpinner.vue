<template>
  <div class="loader-container">
    <div class="radar-wrapper">
      <div class="circle"></div>
      <div class="scanner-line"></div>
      <div class="center-point"></div>
    </div>
    <p class="loading-text">Performing Network Scan...</p>
  </div>
</template>

<style scoped>
.loader-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem;
}

.radar-wrapper {
  position: relative;
  width: 80px;
  height: 80px;
  margin-bottom: 2rem;
}

.circle {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  border: 2px solid rgba(59, 130, 246, 0.2);
  border-radius: 50%;
  box-shadow: inset 0 0 15px rgba(59, 130, 246, 0.1),
              0 0 10px rgba(59, 130, 246, 0.1);
}

.scanner-line {
  position: absolute;
  width: 100%;
  height: 2px;
  background: linear-gradient(
    to bottom,
    transparent,
    rgba(59, 130, 246, 0.8),
    transparent
  );
  box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
  top: 0;
  animation: scan 2s ease-in-out infinite;
}

.center-point {
  position: absolute;
  top: 50%; left: 50%;
  width: 4px; height: 4px;
  background: #3b82f6;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 8px #3b82f6;
}

.loading-text {
  color: #3b82f6;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  letter-spacing: 3px;
  text-transform: uppercase;
  text-shadow: 0 0 5px rgba(59, 130, 246, 0.5);
  animation: flicker 1.5s infinite;
}

@keyframes scan {
  0% { top: 0%; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

@keyframes flicker {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}
</style>