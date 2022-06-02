from pyzbar import pyzbar
import cv2


def stream_scan():
    cap = cv2.VideoCapture(0)
    while True:
        # read the frame from the camera
        _, frame = cap.read()
        # decode detected barcodes & get the image
        # that is drawn
        frame = decode(frame)
        # show the image in the window
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break


def decode(image):
    # decodes all barcodes from an image

    # print("DECODE WORKS")

    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print(f"Обнаружен штрих-код:\n{obj}")
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
