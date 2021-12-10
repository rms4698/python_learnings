import cv2

video = cv2.VideoCapture(0)

check, frame = video.read()

cv2.imwrite("Backgorung.jpg", frame)

video.release()
