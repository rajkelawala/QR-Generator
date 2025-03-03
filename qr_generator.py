import qrcode

data = "Change this to your desired text or URL"  


qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10, 
    border=4, 
)

qr.add_data(data)
qr.make(fit=True)

qr_image = qr.make_image(fill="black", back_color="white")

qr_image.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")
