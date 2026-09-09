FROM python:3.12-slim

WORKDIR /app
COPY . .

CMD ["python", "python_power_demo.py"]