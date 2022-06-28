import matplotlib.pyplot as plt
import numpy as np
import cv2
from pylibdmtx.pylibdmtx import decode


def datamatrixTrue():
    # data = decode(cv2.imread('C:/test8.png'))
    # print(data)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        data = decode(frame)
        print(data)
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow("img", frame)


def datamatrix():
    well = plt.imread('https://i.stack.imgur.com/kqHkw.png')
    well = cv2.cvtColor(well, cv2.COLOR_BGRA2GRAY)
    plt.subplot(151); plt.title('A')
    plt.imshow(well)

    harris = cv2.cornerHarris(well,4, 1,0.00)
    plt.subplot(152); plt.title('B')
    plt.imshow(harris)


    x, thr = cv2.threshold(harris, 0.1 * harris.max(), 255, cv2.THRESH_BINARY)
    thr = thr.astype('uint8')
    plt.subplot(153); plt.title('C')
    plt.imshow(thr)
    print(thr.copy())

    contours, hierarchy = cv2.findContours(thr.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    areas = map(lambda x: cv2.contourArea(cv2.convexHull(x)), contours)
    areas = list(areas)
    max_i = areas.index(max(areas))

    #areas = map(lambda x: cv2.contourArea(cv2.convexHull(x)), contours)
    #max_i = areas.index(max(areas))
    d = cv2.drawContours(np.zeros_like(thr), contours, max_i, 255, 1)
    plt.subplot(154); plt.title('D')
    plt.imshow(d)

    rect = cv2.minAreaRect(contours[max_i])
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    e= cv2.drawContours(well,[box],0,1,1)
    plt.subplot(155); plt.title('E')
    plt.imshow(e)

    plt.show()