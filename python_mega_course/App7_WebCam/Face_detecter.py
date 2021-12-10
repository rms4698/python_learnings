import cv2

face_cascase = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")

# Resize it
img = cv2.resize(img, dsize=((img.shape)[1]//2, (img.shape)[0]//2))

gray_img = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)

faces = face_cascase.detectMultiScale(
    gray_img, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    face_img = cv2.rectangle(img, (x, y), (x+w, y+h),
                             color=(0, 255, 0), thickness=2)

print(faces)

cv2.imshow("Gray img", face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
