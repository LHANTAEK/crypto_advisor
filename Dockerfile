FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
ENV POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH" \
    POETRY_VIRTUALENVS_CREATE=false

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false

# Copy dependency files
COPY poetry.lock pyproject.toml ./

# Install dependencies as root
RUN poetry install --no-interaction --no-ansi --no-root

# Create non-root user
RUN useradd -m appuser && \
    chown -R appuser:appuser /app

# Copy the rest of the application code
COPY --chown=appuser:appuser . .

# 프로젝트 설치
RUN poetry install --no-interaction --no-ansi

# Switch to non-root user
USER appuser

# Expose port for Gradio
EXPOSE 7860

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the application with full path to ensure correct Python environment
CMD ["/opt/poetry/bin/poetry", "run", "python", "app.py"]