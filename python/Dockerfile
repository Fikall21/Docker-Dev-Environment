FROM python:3.11-slim

WORKDIR /app

# Copy daftar dependensi dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode aplikasi dari folder python/app
COPY app/ .

# Jalankan server Uvicorn di port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]