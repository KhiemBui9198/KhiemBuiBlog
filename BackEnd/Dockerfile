# backend/Dockerfile

FROM python:3.11-slim

# Không tạo file .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Hiển thị log ngay lập tức
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Cài package cần thiết
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements trước để tận dụng Docker cache
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 8000

# Chạy Gunicorn
CMD ["gunicorn", "BackEnd.wsgi:application", "--bind", "0.0.0.0:8000"]