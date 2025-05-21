import torch
from ultralytics import YOLO

# Path model (sesuaikan dengan lokasi modelmu)
model_path = 'model/speciesv4.pt'

def load_model():
    # Load model menggunakan YOLO dari Ultralytics
    model = YOLO(model_path)
    model.eval()  # Set model ke evaluasi mode (non-training mode)
    return model

# Coba memuat model
model = load_model()
print("Model berhasil dimuat:", model)
