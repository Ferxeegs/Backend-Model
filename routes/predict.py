from model.model_loader import model
import numpy as np
from PIL import Image
from io import BytesIO

def predict_image(image, score_threshold=0.4):
    # Mengonversi image dari format file (PIL) ke format numpy array yang diterima model
    img = Image.open(image)  # Membuka gambar dari file input
    img = np.array(img)  # Mengonversi gambar ke numpy array

    # Prediksi dengan model YOLO
    results = model(img)

    # Menyimpan hasil prediksi, menggunakan .boxes untuk akses bounding boxes
    predictions = results[0].boxes.xywh.cpu().numpy()  # Mengambil bounding boxes dalam bentuk array numpy
    confidences = results[0].boxes.conf.cpu().numpy()  # Mengambil confidence score
    classes = results[0].boxes.cls.cpu().numpy()  # Mengambil ID kelas

    # Definisikan daftar nama kelas (sesuaikan dengan kelas yang digunakan model Anda)
    class_names = ["Ikan Bawal", "Ikan Gurame", "Ikan Lele", "Ikan Nila", "Ikan Tuna"]  # Contoh class names

    # Konversi hasil prediksi menjadi dict untuk memudahkan akses dan serialisasi ke JSON
    predictions_dict = []

    for prediction, confidence, class_id in zip(predictions, confidences, classes):
        # Pastikan class_id adalah integer
        class_id = int(class_id)  # Konversi class_id ke integer

        # Validasi untuk memastikan class_id valid
        if confidence > score_threshold:  # Hanya menampilkan prediksi dengan confidence lebih tinggi dari threshold
            if 0 <= class_id < len(class_names):  # Memastikan class_id berada dalam jangkauan class_names
                # Print ID kelas, nama kelas, dan confidence untuk debugging
                print(f"Class ID: {class_id}, Class Name: {class_names[class_id]}, Confidence: {confidence}")
                prediction_dict = {
                    "center_x": float(prediction[0]),  # Convert to float
                    "center_y": float(prediction[1]),  # Convert to float
                    "width": float(prediction[2]),     # Convert to float
                    "height": float(prediction[3]),    # Convert to float
                    "confidence": float(confidence),   # Menyertakan confidence score
                    "class_name": class_names[class_id]  # Menambahkan nama kelas ikan
                }
                predictions_dict.append(prediction_dict)
            else:
                # Jika class_id tidak valid, beri peringatan
                print(f"Warning: Invalid class_id {class_id} received. Skipping this prediction.")
        else:
            # Jika confidence kurang dari threshold, beri peringatan
            print(f"Confidence {confidence} below threshold. Skipping this prediction.")

    return predictions_dict
