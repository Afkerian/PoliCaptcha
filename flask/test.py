from read_qr_code import read_qr_code, parse_qr_data
import cv2
import chardet

image = cv2.imread('test.jpg')
response = read_qr_code(image)

print(response)

response = parse_qr_data(response)

print(response)