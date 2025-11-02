# GitHub Actions CI/CD Setup

This repository uses GitHub Actions for continuous integration and deployment. The workflow automatically:

## For all branches:
- Runs tests with pytest
- Checks code coverage (minimum 80%)
- Caches dependencies for faster builds

## For `develop` branch:
- Only runs tests and coverage checks
- No publishing or tagging

## For `main` branch (after PR merge):
- Runs all tests
- Builds the package
- Publishes to PyPI using trusted publishing
- Creates a GitHub release with automatic tagging

## Setup Requirements

### 1. PyPI Trusted Publishing

To enable automatic PyPI publishing, you need to configure trusted publishing:

1. Go to [PyPI](https://pypi.org) and log in to your account
2. Navigate to your account settings
3. Go to "Publishing" → "Add a new pending publisher"
4. Fill in the details:
   - **PyPI Project Name**: `yourag`
   - **Owner**: `GILSAMAS`
   - **Repository name**: `yourag`
   - **Workflow filename**: `ci.yml`
   - **Environment name**: `pypi`

### 2. GitHub Repository Settings

1. Go to your repository settings
2. Navigate to "Environments"
3. Create a new environment called `pypi`
4. Add protection rules:
   - Required reviewers (optional but recommended)
   - Restrict to selected branches: `main`

### 3. Optional: Codecov Integration

For coverage reporting:

1. Go to [Codecov](https://codecov.io)
2. Connect your GitHub repository
3. Get your repository token
4. Add it as a repository secret: `CODECOV_TOKEN`

## Workflow Triggers

- **Push to `main`**: Full CI/CD pipeline (test → build → publish → release)
- **Push to `develop`**: Tests and coverage only
- **Pull Requests**: Tests and coverage only

## Version Management

The workflow automatically:
- Extracts version from `pyproject.toml`
- Creates a git tag (e.g., `v0.1.0`)
- Creates a GitHub release
- Publishes to PyPI

To release a new version:
1. Update the version in `pyproject.toml`
2. Merge to `main` branch
3. The workflow handles the rest automatically

## Testing Locally

Run tests locally before pushing:

```bash
# Install dependencies
uv sync --dev

# Run tests with coverage
uv run pytest --cov=src/yourag --cov-report=term-missing

# Build package
uv build
```

## Security Notes

- Uses OpenID Connect (OIDC) for PyPI publishing (no API tokens needed)
- Environment protection for production deployments
- Secrets are handled securely through GitHub Actions