# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files (handle potentially empty directories)
RUN mkdir -p src tests notebooks dashboard

# Copy individual files and directories that exist
COPY src/__init__.py ./src/__init__.py
COPY src/collatz/ ./src/collatz/
COPY dashboard/ ./dashboard/
COPY tests/__init__.py ./tests/__init__.py
COPY notebooks/.gitkeep ./notebooks/.gitkeep

# Create directories for data and outputs
RUN mkdir -p data/raw data/processed reports

# Set Python path
ENV PYTHONPATH=/app

# Expose port for dashboard/web applications
EXPOSE 8080

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# Default command
CMD ["python", "-m", "dashboard"]