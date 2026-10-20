import qrcode
url = input("Enter the URL or text to generate QR code: ").strip()
file_path = "C:\\Users\\ravic\\OneDrive\\Desktop\\qr_code.png"
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)
print("QR code generated and saved to:", file_path)

