# GitHub Container Registry (GHCR) Setup and Troubleshooting

This document explains how to resolve the "installation not allowed to Create organization package" error when pushing Docker images to GitHub Container Registry.

## The Problem

The error occurs when:
1. Your repository is under an organization (not a personal account)
2. The organization has restrictions on package creation
3. The `GITHUB_TOKEN` doesn't have sufficient permissions

## Solutions

### Solution 1: Organization Package Settings (Recommended)

1. **Organization Owner Action Required**:
   - Go to your GitHub organization settings
   - Navigate to "Packages" in the left sidebar
   - Under "Package creation", ensure the setting allows members to create packages
   - Or specifically allow your repository to create packages

2. **Repository Package Permissions**:
   - Go to your repository Settings → Actions → General
   - Under "Workflow permissions", ensure "Read and write permissions" is selected
   - Check "Allow GitHub Actions to create and approve pull requests"

### Solution 2: Use Personal Access Token (Alternative)

If organization settings cannot be changed:

1. **Create a Personal Access Token**:
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate a new token with these scopes:
     - `write:packages`
     - `read:packages`
     - `delete:packages` (optional)

2. **Add Token as Repository Secret**:
   - Go to repository Settings → Secrets and variables → Actions
   - Add new secret: `GHCR_TOKEN` with your personal access token

3. **Update Workflow** (if using this approach):
   ```yaml
   - name: Log in to GitHub Container Registry
     uses: docker/login-action@v3
     with:
       registry: ${{ env.REGISTRY }}
       username: ${{ github.actor }}
       password: ${{ secrets.GHCR_TOKEN }}
   ```

### Solution 3: Docker Hub Only (Current Implementation)

The workflow has been updated to:
- Continue on error if GHCR login fails
- Always push to Docker Hub successfully
- Attempt GHCR push but don't fail the build if it doesn't work

This ensures your CI/CD pipeline continues to work while the GHCR permissions are being resolved.

## Current Workflow Behavior

✅ **Docker Hub**: Images will always be published to `docker.io/yourusername/collatz-data-science`

⚠️ **GHCR**: Images will be published to `ghcr.io/yourusername/collatz-data-science` only if permissions allow

## Verification

After implementing a solution:

1. **Check Docker Hub**: Visit https://hub.docker.com/r/yourusername/collatz-data-science
2. **Check GHCR**: Visit https://github.com/yourusername/collatz-data-science/pkgs/container/collatz-data-science
3. **Monitor Actions**: Check the GitHub Actions logs for successful pushes

## Required Secrets

Ensure these secrets are configured in your repository:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub access token
- `GHCR_TOKEN`: (Optional) Personal access token for GHCR if using Solution 2

## Next Steps

1. **Immediate**: The workflow will now succeed and push to Docker Hub
2. **Short-term**: Contact your organization owner to enable package creation
3. **Long-term**: Consider using Solution 2 if organization settings cannot be changed

## Testing

To test the fix:
```bash
git add .
git commit -m "Fix GHCR permission issue"
git push origin main
```

The workflow should now complete successfully, publishing to Docker Hub and attempting GHCR without failing.