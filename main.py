from scanner import decode
import cv2
from glob import glob

if __name__ == '__main__':
    barcodes = glob("barcode\\barcode*.*")

    print(barcodes)

    for barcode_file in barcodes:
        # загружаем изображение в opencv
        img = cv2.imread(barcode_file)
        # декодировать обнаруженные штрих-коды и получить изображение
        # нарисованный
        img = decode(img)
        # показать изображение
        cv2.imshow("img", img)
        cv2.waitKey(0)
