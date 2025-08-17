FROM --platform=$BUILDPLATFORM python:3.11.1 AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

EXPOSE 7860

CMD ["gunicorn", "app:app", "--timeout", "300", "--bind", "0.0.0.0:7860"]