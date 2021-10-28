import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#can'n open camera print
if(cap.isOpened()==False):
    print("Could not open VDO source")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("MyCamera", frame)
        if cv2.waitKey(3) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()