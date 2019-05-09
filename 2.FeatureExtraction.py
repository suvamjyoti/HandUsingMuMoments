import cv2
import math


def moments(a):
    d = ""
    grey = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grey, 130, 255, cv2.THRESH_BINARY)

    # Calculate Moments
    mnts = cv2.moments(thresh)

    # Calculate Hu Moments
    huMoments = cv2.HuMoments(mnts)

    for k in range(len(huMoments)):
        d += str(-1 * math.copysign(1.0, huMoments[k]) * math.log(abs(huMoments[k]))) + ","

    return d


# iteration process for calculating of each image
for i in range(3):
    for j in range(30):
        path = "KB" + "/" + str(i) + "/" + str(j) + ".jpg"
        image1 = cv2.imread(path)
        b = moments(image1)
        # creation of file
        path1 = "KB" + "/" + str(i) + "/" + str(i) + str(j) + ".txt"
        f1 = open(path1, "w+")
        f1.write(b)

