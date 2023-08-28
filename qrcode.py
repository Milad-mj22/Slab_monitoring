# Import QRCode from pyqrcode
# import pyqrcode
# import png
# from pyqrcode import QRCode


# String which represents the QR code
# s = "www.geeksforgeeks.org"

# # Generate QR code
# url = pyqrcode.create(s)

# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale = 8)

# # Create and save the png file naming "myqr.png"
# url.png('myqr.png', scale = 6)
from MyQR import myqr as mq
mq.run(words = 'https://dorsa-co.ir/',
  version = 6,
  picture = 'G:\work\PySide-Responsive-ui-master\images\dorsa (1).bmp',
  colorized = True,
  save_name = 'topcoder.png')
