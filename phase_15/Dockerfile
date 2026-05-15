# Use official Python lightweight image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Expose the default port (can be overridden by .env)
EXPOSE 8000

# By default, load production environment settings
ENV APP_ENV=production

# Run the application
CMD ["python", "main.py"]
