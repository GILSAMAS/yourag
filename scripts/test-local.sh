#!/bin/bash
# Local testing script to run before pushing changes

set -e

echo "🔍 Running local tests..."

# Sync dependencies
echo "📦 Syncing dependencies..."
uv sync --dev

# Run tests with coverage
echo "🧪 Running tests with coverage..."
uv run pytest --cov=src/yourag --cov-report=term-missing --cov-fail-under=80

# Build package
echo "🏗️  Building package..."
uv build

# Verify package contents
echo "📋 Package contents:"
uv run python -c "import tarfile; t = tarfile.open('dist/yourag-0.1.0.tar.gz'); print('\\n'.join(t.getnames()))"

echo "✅ All checks passed! Ready to push."