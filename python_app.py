# QR Code Generator
# By Keegan Hugh Kelly @14:30 Aug 31 2022

### Whiteboard:

# Install all the libraries needed.
# Create a function that collects a text and converts it into a QRCode.
# Save the QR Code as an image.
# Run the function.

# Install the QRCODE Image: pip3 install qrcode Image, in your console.

from nturl2path import url2pathname
import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(img_save_name + ".png")

img_save_name = input("Enter the name of the QR Code: ") #Enter the desired name of the file.
url = input("Enter the URL: ") # Enter the URL that you would like to turn into a QR Code Image.
generate_qrcode(url) # Generates and saves the QR Code in the current file being used.

