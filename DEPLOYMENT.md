# Environment Deployment Guide

This guide explains how to deploy the Collatz Data Science application across different environments (QA, UAT) based on the CI/CD pipeline branches.

## Available Environments

### Sandbox Environment
- **Branch**: `develop` or feature branches
- **Purpose**: Experimental development and testing
- **Configuration**: `.env.sandbox`
- **Docker Compose**: `docker-compose.sandbox.yml`
- **Ports**: App (8083), Jupyter (8891), Database (5435), Redis (6379)

### QA Environment
- **Branch**: `qa`
- **Purpose**: Quality Assurance testing
- **Configuration**: `.env.qa`
- **Docker Compose**: `docker-compose.qa.yml`
- **Ports**: App (8081), Jupyter (8889), Database (5433)

### UAT Environment
- **Branch**: `uat`
- **Purpose**: User Acceptance Testing
- **Configuration**: `.env.uat`
- **Docker Compose**: `docker-compose.uat.yml`
- **Ports**: App (8082), Jupyter (8890), Database (5434)

## Deployment Methods

### 1. Local Development

```bash
# Development environment
docker-compose up -d

# Sandbox environment (experimental)
docker-compose -f docker-compose.yml -f docker-compose.sandbox.yml up -d

# QA environment
docker-compose -f docker-compose.yml -f docker-compose.qa.yml up -d

# UAT environment
docker-compose -f docker-compose.yml -f docker-compose.uat.yml up -d
```

### 2. Using Environment Files

```bash
# Copy the appropriate environment file
cp .env.qa .env  # For QA
cp .env.uat .env  # For UAT

# Then run normally
docker-compose up -d
```

### 3. CI/CD Automatic Deployment

The CI/CD pipeline automatically deploys based on branch:
- Push to `qa` branch → Deploys to QA environment
- Push to `uat` branch → Deploys to UAT environment
- Push to `main` branch → Deploys to Production environment

## Environment Configuration

### Sandbox Environment Features
- Debug mode enabled
- Experimental features enabled
- All external APIs mocked
- Hot reload for development
- Redis caching for experiments
- Mock API server available
- Development tools container
- Verbose logging and profiling
- Sample data only

### QA Environment Features
- Debug mode disabled
- Test data enabled
- Mock external APIs
- Performance monitoring
- Separate database instance

### UAT Environment Features
- Production-like configuration
- Real external API connections
- Load testing capabilities
- Enhanced resource limits
- User acceptance testing tools

## Database Setup

Each environment uses its own database:

```bash
# Sandbox Database
DB_NAME=collatz_db_sandbox
DB_PORT=5435

# QA Database
DB_NAME=collatz_db_qa
DB_PORT=5433

# UAT Database
DB_NAME=collatz_db_uat
DB_PORT=5434
```

## Additional Services

### Sandbox Environment Services

```bash
# Start with development tools
docker-compose -f docker-compose.yml -f docker-compose.sandbox.yml --profile dev-tools up -d

# Start with mock API services
docker-compose -f docker-compose.yml -f docker-compose.sandbox.yml --profile mock-services up -d

# Redis for caching experiments
# Available at: localhost:6379

# Mock API server for testing external integrations
# Available at: localhost:1080
```

## Load Testing (UAT Only)

UAT environment includes load testing capabilities:

```bash
# Run load tests
docker-compose -f docker-compose.yml -f docker-compose.uat.yml --profile load-testing up
```

## Health Checks

All environments include health checks:
- **Endpoint**: `http://localhost:<port>/health`
- **Sandbox**: http://localhost:8083/health
- **QA**: http://localhost:8081/health
- **UAT**: http://localhost:8082/health

## Environment Variables

### Required Variables
- `ENVIRONMENT`: Environment name (qa, uat, production)
- `DB_PASSWORD`: Database password for the environment
- `SECRET_KEY`: Application secret key
- `JUPYTER_TOKEN`: Jupyter access token

### Optional Variables
- `OPENAI_API_KEY`: OpenAI API key
- `WANDB_API_KEY`: Weights & Biases API key
- `NEPTUNE_API_TOKEN`: Neptune ML API token

## Security Considerations

1. **Never commit real passwords** to version control
2. Use different secrets for each environment
3. Rotate secrets regularly
4. Use environment-specific API keys
5. Limit network access per environment

## Monitoring and Logging

- **QA**: INFO level logging
- **UAT**: WARN level logging
- **Production**: ERROR level logging

All environments include performance monitoring and can be integrated with external monitoring tools.

## Troubleshooting

### Port Conflicts
If ports are already in use, modify the port mappings in the respective `docker-compose.<env>.yml` files.

### Database Connection Issues
Ensure the database passwords in the environment files match the actual database configuration.

### Container Health
Check container health status:
```bash
docker ps
docker logs <container_name>
```

## Next Steps

1. Configure your CI/CD secrets in GitHub
2. Set up monitoring and alerting
3. Create environment-specific test suites
4. Configure backup strategies for each environment