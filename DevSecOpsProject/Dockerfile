# Base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy application files to the container
COPY app/ /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the application port
EXPOSE 8000

# Set the command to run the application
CMD ["python3", "/app/main.py"]
