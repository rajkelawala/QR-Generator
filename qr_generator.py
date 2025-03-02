import qrcode

# Data to be encoded in the QR code
data = "wa.me/+919328341465"  # Change this to your desired text or URL

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border thickness (default is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
qr_image = qr.make_image(fill="black", back_color="white")

# Save the QR code image
qr_image.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")
