# function to generate qr code
import qrcode
import os 

def generate_qr(url, short_code):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("IN QR GEN")
    img = qrcode.make(url)
    print("1")
    qr_file_path = dir_path + "/static/url_redirect/qr_codes/" + str(short_code) + ".png"
    print("2")
    print(qr_file_path)
    img.save(qr_file_path)
    print("3")
    print(f"Created qr code for{short_code}")

def delete_qr(short_code):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    qr_file_path = dir_path + "/static/url_redirect/qr_codes/" + str(short_code) + ".png"
    if os.path.exists(qr_file_path):
        os.remove(qr_file_path)

# FIX STATIC FILE STUFFS FOR DEPLOYMENT
# CREATE CODE TO CLEAN UP QR CODES AFTER URL OBJECT DELETION