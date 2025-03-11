# Docker Configuration for OpenAI Agents Quickstart

This directory contains Docker configurations for running the OpenAI Agents use case examples.

## Structure

- `docker-compose.yml` - Main configuration to run all use cases
- `Dockerfile.base` - Base image with Python 3.11 and common dependencies
- `use_case_1/` - Dockerfile for use case 1
- `use_case_2/` - Dockerfile for use case 2

## Running with Docker

### Running All Services

To run all the use cases and the Jupyter notebook service:

```bash
cd /path/to/project
docker-compose -f docker/docker-compose.yml up
```

### Running Individual Services

To run a specific use case:

```bash
cd /path/to/project
docker-compose -f docker/docker-compose.yml up use_case_1
```

Or for the Jupyter notebook service:

```bash
cd /path/to/project
docker-compose -f docker/docker-compose.yml up jupyter
```

## Access Points

- Use Case 1: http://localhost:5001
- Use Case 2: http://localhost:5002
- Jupyter Notebook: http://localhost:8888

## Adding New Use Cases

To add a new use case:

1. Create a new directory in `docker/` (e.g., `use_case_3/`)
2. Create a Dockerfile that extends the base image or defines a custom setup
3. Add the service to `docker-compose.yml`

## Environment Variables

Make sure to create a `.env` file in the project root based on the `.env.example` template:

```bash
cp .env.example .env
# Edit .env to add your API keys
``` 