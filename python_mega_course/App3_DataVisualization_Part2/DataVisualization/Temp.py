import justpy as jp
import os
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
from pytz import utc

dirname = os.path.dirname(__file__)
input_dir = os.path.join(dirname, '../InputFiles')
data = pandas.read_csv(input_dir + r"\reviews.csv", parse_dates=["Timestamp"])
