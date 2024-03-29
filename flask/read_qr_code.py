import chardet
from pyzbar.pyzbar import decode
import cv2

def read_qr_code(image):
    decoded_objects = decode(image)
    
    if not decoded_objects:
        print("No se encontró ningún código QR en la imagen.")
        return "NO es un QR VALIDO"
    
    # Obtener la data cruda (bytes)
    raw_data = decoded_objects[0].data

    # Detectar la codificación
    detected_encoding = chardet.detect(raw_data)
    
    # Decodificar usando la codificación detectada
    qr_data = raw_data.decode(detected_encoding['encoding'])

    return qr_data


def parse_qr_data(qr_data):
    data_parts = qr_data.split('/')
    
    # Verificar que haya al menos 4 partes en los datos (código, nombres, carrera, periodo)
    if len(data_parts) < 4:
        print("Datos del código QR incompletos o en un formato no esperado.")
        return "NO es un QR VALIDO"
    
    codigo_unico = data_parts[0]
    nombres = data_parts[1]
    carrera = data_parts[2]
    periodo_activo = data_parts[3]
    
    return {
        "CÓDIGO UNICO": codigo_unico,
        "NOMBRES": nombres,
        "CARRERA": carrera,
        "PERIODO ACTIVO": periodo_activo
    }

"""if __name__ == "__main__":
    PATH_QR_1 = "../QRs/qr_rocha_richard.jpg"
    imagen_codigo_qr = PATH_QR_1
    
    datos_qr = read_qr_code(imagen_codigo_qr)
    
    if datos_qr:
        print("Datos del código QR:")
        print(datos_qr)
        
        parsed_data = parse_qr_data(datos_qr)
        if parsed_data:
            print("\nInformación estructurada:")
            for key, value in parsed_data.items():
                print(f"{key}: {value}")"""
