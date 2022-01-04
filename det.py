import time

import cv2
import paddlex as pdx

predictor = pdx.deploy.Predictor("./inference_model/inference_model")

tic = time.time()
fps = 10
itv = 1 / fps
cam = cv2.VideoCapture(0)

while True:
    ret_val, img = cam.read()
    if cv2.waitKey(1) == 27:
        break  # esc to quit

    if time.time() - tic > itv:
        h, w, _ = img.shape
        tic = time.time()
        result = predictor.predict(img)
        print(result)
        img = pdx.det.visualize(img, result, threshold=0.00001, save_dir=None)
        cv2.imshow("detection", img)

        f = open("bb.txt", "w")
        if len(result) != 0:
            for r in result:
                p = r["bbox"]
                print(
                    p[0] / w,
                    p[1] / h,
                    (p[0] + p[2]) / w,
                    (p[1] + p[3]) / h,
                    r["score"],
                    file=f,
                )
            f.flush()
            input("here")


cv2.destroyAllWindows()
