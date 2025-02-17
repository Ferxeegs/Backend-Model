from flask import Flask, request, jsonify
from routes.predict import predict_bp
import logging

# Setup logging untuk debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    app.logger.info("Start /predict route")  # Log untuk memulai proses prediksi

    # Memeriksa apakah gambar ada dalam request
    if 'image' not in request.files:
        app.logger.error('No image part in the request')  # Log jika tidak ada bagian gambar
        return jsonify({'success': False, 'message': 'No image provided'}), 400

    image = request.files['image']
    
    # Log nama file gambar yang diterima
    app.logger.info(f"Received image: {image.filename}")

    # Cek apakah file gambar ada
    if image.filename == '':
        app.logger.error('No selected file')  # Log jika tidak ada file yang dipilih
        return jsonify({'success': False, 'message': 'No selected file'}), 400

    try:
        app.logger.info('Processing image with predict_bp...')  # Log sebelum memproses gambar
        result = predict_bp(image)  # Mengirim gambar dalam format file ke fungsi predict_bp

        # Log hasil prediksi
        app.logger.info(f"Prediction result: {result}")
        
        return jsonify(result)

    except Exception as e:
        # Log jika ada error saat pemrosesan
        app.logger.error(f"Error processing image: {str(e)}")
        return jsonify({'success': False, 'message': f"Error processing image: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
