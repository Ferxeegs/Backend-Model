# Gunakan Python base image yang ringan
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies OS yang dibutuhkan OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Salin file requirements.txt
COPY requirements.txt .

# Install PyTorch CPU dan Python packages lainnya
RUN pip install --no-cache-dir torch==2.1.0+cpu torchvision==0.16.0+cpu --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# Salin semua file project ke dalam container
COPY . .

# Ekspose port Flask
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
