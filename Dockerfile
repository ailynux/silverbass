# Use Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Update the system and install Python3 and pip3
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip

# Install required Python packages
RUN pip3 install pyyaml jinja2

# Copy your project files into the container
COPY . .

# Ensure correct permissions
RUN chmod -R 777 /app

# Set the entry point to run your Python script
ENTRYPOINT ["python3", "main.py"]
