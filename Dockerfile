FROM python:3.9

WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install pyyaml jinja2

# Run the Python script
ENTRYPOINT ["python", "main.py"]
