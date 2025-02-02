# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy backend dependencies
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application files
COPY backend /app

# Copy the frontend static files
COPY frontend/web /app/frontend/web

# Set environment variables for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8008
ENV FLASK_ENV=development

# Expose the Flask port
EXPOSE 8008

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8008"]
