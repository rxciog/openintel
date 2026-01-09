# OpenIntel

OpenIntel is a containerized web application for IP and domain
intelligence analysis.\
It consists of a FastAPI backend, a frontend UI, and an Nginx reverse
proxy, all orchestrated using Docker Compose.

------------------------------------------------------------------------

## Architecture

    Browser
       ↓
    Nginx (port 80)
       ├── Frontend (static files)
       └── /api/* → Backend (FastAPI, port 8000)

-   **Single public entry point** (Nginx)
-   **Backend is private** (only accessible inside Docker network)
-   **Frontend communicates with backend via `/api`**
-   Suitable for local development and cloud deployment (e.g. AWS EC2)

------------------------------------------------------------------------

## Prerequisites

-   Docker (\>= 20.x)
-   Docker Compose v2

Verify installation:

``` bash
docker --version
docker compose version
```

------------------------------------------------------------------------

## Clone the Repository

``` bash
git clone <REPOSITORY_URL>
cd openintel
```

------------------------------------------------------------------------

## Project Structure

    .
    ├── backend/              # FastAPI backend
    │   ├── Dockerfile
    │   └── app/
    ├── frontend/             # Frontend application
    │   ├── Dockerfile
    │   └── nginx.conf
    ├── nginx/
    │   └── nginx.conf        # Reverse proxy configuration
    ├── docker-compose.yml
    └── README.md

------------------------------------------------------------------------

## Running the Application

From the project root:

``` bash
docker compose up --build
```

The application will be available at:

-   **Frontend:** http://localhost\
-   **Backend (via proxy):**
    -   http://localhost/api/ip
    -   http://localhost/api/domain

> The backend is intentionally **not exposed directly**.

------------------------------------------------------------------------

## Stopping the Application

``` bash
docker compose down
```

Clean rebuild:

``` bash
docker compose down -v
docker compose up --build
```

------------------------------------------------------------------------

## Environment Notes

-   Containers communicate using Docker service names (`backend`,
    `frontend`)
-   No hardcoded IPs
-   Safe to use on cloud instances with changing public IPs
-   CORS should be configured for same-origin requests via Nginx

------------------------------------------------------------------------

## Useful Commands

View logs:

``` bash
docker compose logs -f
```

List containers:

``` bash
docker compose ps
```

Shell into backend:

``` bash
docker exec -it openintel-backend sh
```

------------------------------------------------------------------------

## Roadmap

-   Automated backend testing (pytest)
-   CI/CD pipeline (Jenkins) 
-   HTTPS with Certbot + Nginx
-   Image versioning and tagging

------------------------------------------------------------------------

## License

MIT License
