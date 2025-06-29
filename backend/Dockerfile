# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Don't write pycache files to disk
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install uv for dependency management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install production dependencies only
RUN uv sync --frozen --no-dev

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# ✅ Set cache dir and make it writable by appuser
ENV UV_CACHE_DIR=/tmp/.cache/uv
RUN mkdir -p /tmp/.cache/uv && chown -R appuser:appuser /tmp/.cache

# Copy application code
COPY . .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port 8000 
EXPOSE 8000

# Command to run the application
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]