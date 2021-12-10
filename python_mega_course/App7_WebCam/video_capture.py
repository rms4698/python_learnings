import cv2
import datetime
import pandas

video = cv2.VideoCapture(0)
first_frame = None
previous_status = 0
status_list = []
timestamps = []

while True:
    check, frame = video.read()

    status = 0

    gray_img = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, ksize=(21, 21), sigmaX=0)

    if first_frame is None:
        first_frame = gray_img
        continue

    delta_frame = cv2.absdiff(first_frame, gray_img)

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (conts, _) = cv2.findContours(thresh_frame,
                                  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cont in conts:
        if cv2.contourArea(cont) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(cont)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Capturing", gray_img)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Thereshold", thresh_frame)
    cv2.imshow("Color Frame", frame)

    if status < previous_status:
        print("Motion stopped", datetime.datetime.now())
        timestamps.append(datetime.datetime.now())
    elif status > previous_status:
        print("Motion started", datetime.datetime.now())
        timestamps.append(datetime.datetime.now())

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            timestamps.append(datetime.datetime.now())
        break

    previous_status = status

video.release()
cv2.destroyAllWindows()


df = pandas.DataFrame(columns=["Start Time", "End Time"])

start_time = []
end_time = []
print("len of timestamps", len(timestamps))
for i in range(0, len(timestamps), 2):
    start_time.append(timestamps[i])
    end_time.append(timestamps[i+1])

df["Start Time"] = start_time
df["End Time"] = end_time

df.to_csv("MotionDetector.csv")
