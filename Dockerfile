# Use the official Python image, which already has Python3 and pip
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Python dependencies with pip3
RUN pip install --upgrade pip \
    && pip install PyYAML jinja2

# Copy the application files to the container
COPY . .

# Ensure correct permissions for the app directory
RUN chmod -R 777 /app

# Set the entry point to run your Python script
ENTRYPOINT ["python3", "main.py"]
