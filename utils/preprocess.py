from torchvision import transforms
from PIL import Image

# Transformasi gambar agar sesuai dengan model
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Ubah ukuran gambar
    transforms.ToTensor(),           # Konversi ke Tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalisasi
])

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)  # Tambahkan dimensi batch
    return image
