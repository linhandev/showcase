import time
from time import strftime
import os.path as osp
import os

import cv2


opd = "./dataset/img"
if not osp.exists(opd):
    os.makedirs(opd)

cap = cv2.VideoCapture(0)
tic = start = time.time()

while 1:
    ret, frame = cap.read()
    frame = frame[:, ::-1, :]
    cv2.imshow("Camera", frame)

    if time.time() - start > 4 and time.time() - tic > 1:
        print("capture")
        os.system("play -q -n synth 0.08 sin 880 || echo -e '\a'")
        cv2.imwrite(osp.join(opd, f"{strftime('%H_%M_%S')}.png"), frame)
        tic = time.time()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# release the camera from video capture
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
