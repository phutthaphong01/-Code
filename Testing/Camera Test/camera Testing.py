import cv2
source = 0
cap = cv2.VideoCapture(source)
if cap is None or not cap.isOpened():
    print("could not open vdo source: ",source)
else:
    print("vdo source OK ->",source)
    cap.release()