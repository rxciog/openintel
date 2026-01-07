# Frontend (OpenIntel UI)

This directory contains the **frontend web application** for OpenIntel.

## Tech Stack
- Node.js 20
- Vite
- Vue 3
- Nginx
- Docker

---

## Running with Docker (Recommended)

From the **project root**:

```bash
docker compose up --build frontend
```

Or from this directory:

```bash
docker build -t openintel-frontend .
docker run -p 80:80 openintel-frontend
```

The app will be available at:

```
http://localhost
```

---

## Frontend → Backend Communication

The frontend **does not talk directly to the backend**.

All API requests are sent to:

```
/api/ip
/api/domain
```

These are proxied by **Nginx** to the backend service.

---

## Local Development (Optional)

```bash
npm install
npm run dev
```

This starts a local dev server (not Docker-based).

---

## Build Output

The production build is generated into:

```
dist/
```

and served by Nginx inside the container.
