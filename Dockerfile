FROM python:3.11-slim

WORKDIR /app

COPY text_analyzer.py initializers.py main.py ./

ENV PYTHONUNBUFFERED=1

CMD ["python3", "main.py"]
