import pyqrcode

b = pyqrcode.QRCode("URL")

b.png('ファイル名(なんでもいい)',scale=6)