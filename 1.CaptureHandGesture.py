import cv2
import numpy as np
import math

def Cstr(d):
    s = ""
    for a in range(len(d)):
        x = str(d[a])+","
        y = x.split(".")
        s += str(y[0]) + ","

    return s


f1 = open("0.txt", "w+")

huMoments = []
cap = cv2.VideoCapture(0)
i = 0


while i < 30:
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # drawing rectangle
    cv2.rectangle(grey, (400, 70), (600, 400), (0, 255, 0), 1)
    # capturing the region of interest
    roi = grey[100:400, 410:600]
    blur = cv2.blur(roi, (7, 7))

    # display windows
    cv2.imshow('picture', grey)
    cv2.imshow('grey', blur)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Log scale hu moments
        path = str(i) + ".jpg"
        cv2.imwrite(path, blur)
        i = i + 1

cap.release()
cv2.destroyAllWindows()