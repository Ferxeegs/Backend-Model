from flask import Flask, request, jsonify
from routes.predict import predict_bp

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['image']
    result = predict_bp(image)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
