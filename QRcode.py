import cv2
import numpy as np
from pyzbar.pyzbar import decode

#QRコードのコントラスト調整用の関数
def edit_contrast(image, gamma):
    """コントラスト調整"""
    look_up_table = [np.uint8(255.0 / (1 + np.exp(-gamma * (i - 128.) / 255.)))
        for i in range(256)]
    result_image = np.array([look_up_table[value]
                             for value in image.flat], dtype=np.uint8)
    result_image = result_image.reshape(image.shape)
    return result_image

#カメラ認識
cap_cam = cv2.VideoCapture(0)
cv2.namedWindow('frame')
# カメラが接続できない場合は、exit
if not cap_cam.isOpened():
    print("カメラを開けません")
    exit()

while True:
    # フレームごとにキャプチャ
    ret, frame = cap_cam.read()
    #フレームが正しく読み取られた場合、retはTrue
    if not ret:
        print("フレームは受信できません。終了しています...")
        break

    # グレースケール化してコントラストを調整する
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image = edit_contrast(gray_scale, 5)

    # 結果のフレーム表示
    cv2.imshow('frame',gray_scale)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 加工した画像からフレームQRコードを取得してデコードする
    codes = decode(image)
    if len(codes) > 0:
        output = codes[0][0].decode('utf-8', 'ignore')
        print(output)
        if 'output' != None:
            #cap_cam.read()
            cap_cam.release()

# すべて完了したらキャプチャーを解放する
#cap_cam.release()
cv2.destroyAllWindows()