import cv2
import numpy as np

from func import getArea, showCentroidAndAxisAndEccentricity, VossEdgeTracing, getCurvature, distanceTransform, houghTransform


def convert_to_grayscale(image_path: str)-> np.ndarray | None:
    image: np.ndarray = cv2.imread(image_path)

    if image is None:
        print("Помилка: не вийшло завантажити зображення.")
        return None

    res_image: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return res_image


def test(choose: int):
    if 1 <= choose <= 5:
        gray_image = convert_to_grayscale('img.png')
    elif choose == 6:
        gray_image = convert_to_grayscale('img1.png')
    else:
        print("Некоректний вибір, спробуйте знову.")
        return

    if gray_image is not None:
        cv2.imshow('Gray Image', gray_image)
        if(choose == 1):            #Площа
            print("=== Коло ===\n")
            print("Площа ділянки:", getArea(gray_image, (500, 300)))
        elif (choose == 2):         #центроїд, головна вісь та ексцентриситет
            print("=== Коло ===\n")
            showCentroidAndAxisAndEccentricity(gray_image, (500, 300))
            #print("=== Лінія ===\n")
            #showCentroidAndAxisAndEccentricity(gray_image, (883, 147))
            #print("=== Еліпс ===\n")
            #showCentroidAndAxisAndEccentricity(gray_image, (1048, 132))
        elif (choose == 3):
            edge = VossEdgeTracing(gray_image, (1151, 251), True)
            cv2.imshow('Edge', edge)
            # 356, 173
            # 986, 125
            # 993, 85
            # 951, 131
            # 1151, 251
        elif (choose == 4):
            curv = getCurvature(gray_image, VossEdgeTracing(gray_image, (356, 173), False), 50)
            cv2.imshow('Curv', curv)

        elif (choose == 5):
            distance_map = distanceTransform(gray_image, (500, 300))
            cv2.imshow('Distance Transformation for Object', distance_map)

        elif (choose == 6):
            lines_image = houghTransform(gray_image)
            cv2.imshow('Detected Lines with Hough Transform', lines_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':

    print("=== Меню ===")
    print("1: Знайти площу ділянки")
    print("2: Знайти та вивести центроїд, головна вісь та ексцентриситет")
    print("3: Виконати трасування краю ділянки")
    print("4: Оцінити кривизну контуру в різних точках.")
    print("5: Дистанційне перетворення для об'єкта")
    print("6: Знайти та візуалізувати лінії на зображенні за допомогою перетворення Хафа")
    try:
        choose = int(input("Оберіть номер операції: "))
        test(choose)
    except ValueError:
        print("Будь ласка, введіть коректний номер.")

