import telebot
import configparser
import os
from config import cargar_configuracion
from read_qr_code import read_qr_code, parse_qr_data
import cv2

config = cargar_configuracion()
apy_key = config.get('API_KEY', 'KEY')

bot = telebot.TeleBot(apy_key)

@bot.message_handler(commands=['start'])
def enviar(message):
    bot.reply_to(message, "Hola! ¿Como puedo ayudarte?")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    # Obtener la ID del archivo del video
    video_id = message.video.file_id

    # Descargar el video
    file_info = bot.get_file(video_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Guardar el video en el servidor local
    with open("video.mp4", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "¡Video recibido y guardado!")

    

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Las fotos en Telegram pueden tener diferentes resoluciones. 
    # Elegimos la de más alta resolución (la última en la lista).
    photo = message.photo[-1]

    # Obtener la ID del archivo de la foto
    photo_id = photo.file_id

    # Descargar la foto
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Guardar la foto en el servidor local
    name = photo_id+'photo.jpg'
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "¡Foto recibida y guardada!")

    image = cv2.imread(name)
    response = ""
    qr_data = read_qr_code(image)
    if qr_data == "NO es un QR VALIDO":
        response = "NO es un QR VALIDO"
    else:
        qr_data = parse_qr_data(qr_data)
        if qr_data == "NO es un QR VALIDO":
            reponse = "NO es un QR VALIDO"
    #qr_data = str(qr_data)
    
    response += "DATOS QR: \n"

    if "CÓDIGO UNICO" in qr_data:
        response += "CÓDIGO UNICO: " + str(qr_data["CÓDIGO UNICO"]) + "\n"
        
    if "NOMBRES" in qr_data:
        response += "NOMBRES: " + str(qr_data["NOMBRES"]) + "\n"
        
    if "CARRERA" in qr_data:
        response += "CARRERA: " + str(qr_data["CARRERA"]) + "\n"
        
    if "PERIODO ACTIVO" in qr_data:
        response += "PERIODO ACTIVO: " + str(qr_data["PERIODO ACTIVO"]) + "\n"

    # Si no encuentra ningún dato, puedes añadir un mensaje adicional
    if response == "DATOS QR: \n":
        response = "No se encontraron datos en el QR."


    bot.reply_to(message, response)


@bot.message_handler(func=lambda message: True)
def mensaje(message):
    print(f'Usuario: {message.from_user.first_name} \nGPT: {message.text}')
    bot.reply_to(message, message.text)

bot.polling()
