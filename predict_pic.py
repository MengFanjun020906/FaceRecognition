import cv2
from retinaface import Retinaface


def detect_pic(image_path):
    retinaface = Retinaface()

    image = cv2.imread(image_path)

    if image is None:
        print('Open Error! Try again!')
        return None

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    r_image = retinaface.detect_image(image)
    r_image = cv2.cvtColor(r_image, cv2.COLOR_RGB2BGR)
    cv2.imshow("after", r_image)
    cv2.waitKey(0)

if __name__ == "__main__":
    detect_pic(pick_pic())
