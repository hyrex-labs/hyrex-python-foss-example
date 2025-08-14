# Hyrex Docker Compose Example

A Hyrex application with PostgreSQL database running in Docker containers.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone the repository and navigate to the project directory

2. Build and start the services:
   ```bash
   docker compose up --build
   ```

   Or run in detached mode:
   ```bash
   docker compose up -d --build
   ```

3. The application will be available with:
   - PostgreSQL database on `u:5432`
   - Hyrex worker running and connected to the database
   - Hyrex Studio UI on `https//local.hyrex.studio`

## Configuration

### Database Connection

The application connects to PostgreSQL using the following default credentials:
- **Database:** `hyrex_db`
- **User:** `hyrex_user`
- **Password:** `hyrex_password`
- **Host:** `localhost` (from host machine) or `postgres` (from within Docker network)
- **Port:** `5432`

### Environment Variables

Copy `.env.example` to `.env` to customize configuration:
```bash
cp .env.example .env
```

## Docker Commands

### Start services
```bash
docker compose up
```

### Stop services
```bash
docker compose down
```

### Stop and remove volumes
```bash
docker compose down -v
```

### View logs
```bash
docker compose logs -f
```

### View specific service logs
```bash
docker compose logs -f app
docker compose logs -f postgres
docker compose logs -f studio
```

### Rebuild containers
```bash
docker compose build
```

## Development

### Local Development

For local development without Docker:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your local database configuration
   ```

4. Run the Hyrex worker:
   ```bash
   hyrex run-worker hyrex_app:app
   ```

### Project Structure

```
.
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Docker Compose services configuration
├── hyrex_app.py        # Main Hyrex application
├── tasks.py            # Task definitions
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
└── README.md          # This file
```

## Troubleshooting

### Database connection issues
- Ensure PostgreSQL container is healthy: `docker compose ps`
- Check logs: `docker compose logs postgres`
- Verify environment variables in `.env` file

### Container not starting
- Check Docker daemon is running
- Review logs: `docker compose logs`
- Ensure ports 5432 is not already in use

### Reset everything
```bash
docker compose down -v
docker compose up --build
```