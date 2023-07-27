import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    
    image = cv2.imread(image_path)
    
    decoded_objects = decode(image)
    
    if not decoded_objects:
        print("No se encontró ningún código QR en la imagen.")
        return None
    
    qr_data = decoded_objects[0].data.decode('utf-8')
    
    return qr_data

if __name__ == "__main__":
    
    PATH_QR_1 = "QRs/qr_rocha_richard.jpg"
    imagen_codigo_qr = PATH_QR_1
    
    
    datos_qr = read_qr_code(imagen_codigo_qr)
    
    if datos_qr:
        print("Datos del código QR:")
        print(datos_qr)
