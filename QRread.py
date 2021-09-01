import cv2
import threading
from pyzbar.pyzbar import decode

def qr_read():
    while True:
        order = input()
        if order == 'read':
            d = decode(frame)
        
            for QRcode in d:
                QRData = QRcode.data.decode('utf-8')
                print('読み込んだ文字は ' + QRData + ' です。')

qr_read_thread = threading.Thread(target=qr_read, args=())
qr_read_thread.daemon = True
qr_read_thread.start()

cap = cv2.VideoCapture(0)
print(cap.isOpened())

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release
cv2.destroyAllWindows()