import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

data = 'https://www.youtube.com/watch?v=U573mlR4rYw&list=RDU573mlR4rYw&start_radio=1'

qr = qrcode.QRCode(version = 3,error_correction=qrcode.constants.ERROR_CORRECT_L ,box_size=10,border=5)

qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(image_factory=StyledPilImage,fill_color = 'black', back_color = 'white',
                    color_mask=RadialGradiantColorMask())

img.save("C:/Users/User/Pictures/Camera Roll/myqrcode6.png")
