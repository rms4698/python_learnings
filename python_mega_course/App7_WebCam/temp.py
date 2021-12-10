import pandas
import datetime

df = pandas.DataFrame(columns=["Start Time", "End Time"])

timestamps = [datetime.datetime(2021, 5, 28, 16, 33, 43, 312553), datetime.datetime(2021, 5, 28, 16, 33, 44, 419563), datetime.datetime(
    2021, 5, 28, 16, 33, 44, 854186), datetime.datetime(2021, 5, 28, 16, 33, 45, 719279)]

start_time = []
end_time = []
for i in range(0, len(timestamps), 2):
    start_time.append(str(timestamps[i]))
    end_time.append(str(timestamps[i]))

df["Start Time"] = start_time
df["End Time"] = end_time

df.to_csv("MotionDetector.csv")

# plt.hist(timestamps, status_list)
