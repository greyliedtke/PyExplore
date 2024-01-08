
import cv2


# detect cameras 
cap = cv2.VideoCapture(0)

for c in range(0,10):

    cap = cv2.VideoCapture(c)
    test, frame = cap.read()
    print(f'{test}, {frame}')