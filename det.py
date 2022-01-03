import paddlehub as hub
import cv2

object_detector = hub.Module(name="yolov3_resnet50_vd_coco2017")
result = object_detector.object_detection(images=[cv2.imread("phone.jpg")])
print(result)
