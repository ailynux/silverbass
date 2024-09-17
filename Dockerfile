FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install pyyaml jinja2

# Ensure correct permissions
RUN chmod -R 777 /app

ENTRYPOINT ["python", "main.py"]
