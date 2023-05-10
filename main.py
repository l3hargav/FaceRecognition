import cv2

stream = cv2.VideoCapture(0)

while(True):
    (grabbed, frame) = stream.read()
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break