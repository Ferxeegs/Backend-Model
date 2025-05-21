from ultralytics import YOLO

model_path = "model/speciesv4.pt"  # Sesuaikan path model kamu

# Load model menggunakan Ultralytics API
model = YOLO(model_path)

# Periksa apakah model berhasil dimuat
print("Model berhasil dimuat:", model)
