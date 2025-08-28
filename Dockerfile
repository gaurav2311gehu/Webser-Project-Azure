# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ ./app

# Set environment variable
ENV FLASK_APP=app/server.py

# Expose port
EXPOSE 5000

# Run server
CMD ["python", "app/server.py"]
