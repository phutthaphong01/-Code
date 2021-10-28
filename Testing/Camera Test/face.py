import cv2

cap = cv2.VideoCapture(0)
casc_file = 'haarcascade_frontalface_default.xml'

frontal_face = cv2.CascadeClassifier(casc_file)

if(cap.isOpened() == False):
    print("Could not open the VDO file")

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        bBoxes = frontal_face.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))
        
        for(x, y, w, h) in bBoxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow("MyWin", frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
