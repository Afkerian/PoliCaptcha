from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64
from read_qr_code import read_qr_code  # Asegúrate de reemplazar 'my_module' con el nombre de tu archivo

app = Flask(__name__)

@app.route('/readQR', methods=['POST'])
def handle_request():
    image_b64 = request.json['image']
    if image_b64:
        image_bytes = base64.b64decode(image_b64)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        qr_data = read_qr_code(image)
        return jsonify({'qr_data': qr_data})
    else:
        return jsonify({'error': 'No image data provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
