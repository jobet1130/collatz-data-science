# Docker Hub Integration Setup

This document explains how to configure Docker Hub integration for automatic image publishing.

## Required GitHub Secrets

To enable Docker Hub publishing, you need to add the following secrets to your GitHub repository:

### 1. DOCKER_USERNAME
- **Description**: Your Docker Hub username
- **Value**: Your Docker Hub account username (e.g., `yourusername`)

### 2. DOCKER_PASSWORD
- **Description**: Docker Hub access token for authentication
- **How to create**:
  1. Log in to [Docker Hub](https://hub.docker.com/)
  2. Go to Account Settings → Security
  3. Click "New Access Token"
  4. Give it a descriptive name (e.g., "GitHub Actions")
  5. Select appropriate permissions (Read, Write, Delete)
  6. Copy the generated token

## Adding Secrets to GitHub

1. Go to your GitHub repository
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add each secret:
   - Name: `DOCKER_USERNAME`, Value: your Docker Hub username
   - Name: `DOCKER_PASSWORD`, Value: your Docker Hub access token

## Docker Hub Repository

Make sure you have a repository on Docker Hub named `collatz-data-science` or update the `DOCKERHUB_IMAGE_NAME` in the workflow file to match your desired repository name.

## What Gets Published

The workflow will automatically publish Docker images to both:
- **GitHub Container Registry**: `ghcr.io/yourusername/collatz-data-science`
- **Docker Hub**: `yourusername/collatz-data-science`

### Image Tags

Images are tagged with:
- Branch names (e.g., `main`, `develop`)
- Pull request numbers (e.g., `pr-123`)
- Semantic version tags (e.g., `v1.0.0`, `1.0`)
- Commit SHA with branch prefix (e.g., `main-abc1234`)
- `latest` tag for main branch (Docker Hub only)

## Verification

After setting up the secrets and pushing code:
1. Check the Actions tab for successful workflow runs
2. Verify images appear in both GitHub Packages and Docker Hub
3. Test pulling images: `docker pull yourusername/collatz-data-science:latest`