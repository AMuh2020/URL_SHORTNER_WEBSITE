# function to generate qr code
import qrcode
import os 
from io import BytesIO

def generate_qr(url, short_code):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    print("IN QR GEN")
    img = qrcode.make(url)
    print(img)
    
    qr_file_path = dir_path + "/static/url_redirect/qr_codes/" + str(short_code) + ".png"
    # print(qr_file_path)
    img.save(qr_file_path)

    print(f"Created qr code for {short_code}")
    return qr_file_path
    #modified for file object 
    

def delete_qr(short_code):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    qr_file_path = dir_path + "/static/url_redirect/qr_codes/" + str(short_code) + ".png"
    if os.path.exists(qr_file_path):
        os.remove(qr_file_path)
        print(f"Deleted qr code for {short_code}")

# FIX STATIC FILE STUFFS FOR DEPLOYMENT
# CREATE CODE TO CLEAN UP QR CODES AFTER URL OBJECT DELETION

#NEW METHOD CONVERT QR CODE INTO BYTES USING STRING IO, WHEN RENDERED BY HTML IT IS AN IIMAGE

# generate_qr("https://www.google.com", "test")