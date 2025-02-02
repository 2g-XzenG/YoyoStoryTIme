# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment variables
ENV DOCKERIZED=true
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8008
ENV FLASK_ENV=development

# Expose the Flask port
EXPOSE 8008

# Run Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8008"]
