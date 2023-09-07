from PIL import Image, ImageDraw
import qrcode

def create_bookmark_with_qr(bookmark_path, qr_data, output_path, position=(50, 50)):
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Abrir la imagen del marcador
    bookmark_img = Image.open(bookmark_path)
    
    # Pegar el código QR en el marcador
    bookmark_img.paste(qr_img, position)
    
    # Guardar la imagen resultante
    bookmark_img.save(output_path)

# Crear un ejemplo usando un marcador en blanco
bookmark_img_path = "path_to_your_bookmark_image.png"  # Cambia esto por la ruta de tu imagen de marcador
output_img_path = "path_where_you_want_to_save.png"    # Cambia esto por la ruta donde quieres guardar el resultado

# Si quieres un marcador en blanco como en el ejemplo:
img = Image.new("RGB", (200, 600), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Marcador", fill=(0, 0, 0))
img.save(bookmark_img_path)

# Crear el marcador con el QR
create_bookmark_with_qr(bookmark_img_path, 'https://www.openai.com/', output_img_path)
