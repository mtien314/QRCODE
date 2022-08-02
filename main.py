import qrcode

data = 'https://www.youtube.com'

qr = qrcode.QRCode(version = 2, box_size= 10,border=5)
qr.make(fit = True)

qr.add_data(data)
img = qr.make_image(fill_color = 'blue' ,back_color = 'black')

img.save("C:/Users/User/Pictures/Camera Roll/myqrcode3.png")

