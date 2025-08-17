FROM python:3.13-slim

WORKDIR /church

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y \
    build-essential \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxss1 \
    libxtst6 \
    libxcb1 \
    libx11-6 \
    libglib2.0-0 \
    libgdk-pixbuf-2.0-0 \
    libfontconfig1 \
    libcairo2 \
    libjpeg62-turbo \
    fonts-unifont \
    curl \
    wget \
    unzip \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instala navegadores do Playwright (sem --with-deps pois já instalamos as libs)
RUN playwright install

EXPOSE 8000
