FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]