from pyzbar import pyzbar
import cv2


def stream_scan():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        # # read the frame from the camera
        # # decode detected barcodes & get the image
        # # that is drawn
        ret, frame = cap.read()
        # # decode detected barcodes & get the image
        # # that is drawn
        image = decode(frame)
        if cv2.waitKey(1) == ord('q'):
            break
        # # show the image in the window
        cv2.imshow("img", image)


def decode(image):
    # decodes all barcodes from an image

    # print("DECODE WORKS"
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print(f"Обнаружен код:\n{obj}")
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Тип:", obj.type)
        print("Данные:", obj.data)
        print()
    return image


def draw_barcode(decoded, image):
    # нарисовать прямоугольник
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                          (decoded.rect.left + decoded.rect.width,
                           decoded.rect.top + decoded.rect.height),
                          color=(0, 255, 0),
                          thickness=5)
    return image
