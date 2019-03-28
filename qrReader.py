import pyqrcode

keyword = 'Unladden swallow'
qr = pyqrcode.create(keyword)
qr.png('famous-joke.png', scale=1)
print(qr.terminal(quiet_zone=1))

from PIL import Image
from pyzbar.pyzbar import decode

results = decode(Image.open('famous-joke.png'))
for key in results:
    print('Type: ', key.type)
    print('Data: ', key.data.decode("utf-8"), '\n')
    data = key.data.decode("utf-8")

if data == keyword:
    print("Let this muthafucka in")
