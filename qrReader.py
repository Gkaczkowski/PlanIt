import pyqrcode

qr = pyqrcode.create('Unladden swallow')
qr.png('famous-joke.png', scale=1)
print(qr.terminal(quiet_zone=1))

from PIL import Image
from pyzbar.pyzbar import decode

print(decode(Image.open('famous-joke.png')))
