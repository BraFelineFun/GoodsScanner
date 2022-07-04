import cv2
from pylibdmtx.pylibdmtx import decode


def datamatrix(image):
     #pass
     data = decode(cv2.imread(image))
     return data
    # cap = cv2.VideoCapture(0)
    # while True:
    #     ret, frame = cap.read()
    #     data = decode(frame)
    #     print(data)
    #     if cv2.waitKey(1) == ord('q'):
    #         break
    #     cv2.imshow("img", frame)
