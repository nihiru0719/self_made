from pyzbar.pyzbar import decode
from PIL import Image

img = "ファイル名(write.pyと同じにする)"

data = decode(Image.open(img))

print(data[0][0].decode('utf-8', 'ignore'))