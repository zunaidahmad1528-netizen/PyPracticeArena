FROM python:3.12-slim

WORKDIR /app
COPY projects/ ./projects/

CMD ["python", "projects/scientific_calculator.py"]