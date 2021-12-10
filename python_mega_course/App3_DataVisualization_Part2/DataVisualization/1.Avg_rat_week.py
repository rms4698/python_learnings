import justpy as jp
import os
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
from pytz import utc

dirname = os.path.dirname(__file__)
input_dir = os.path.join(dirname, '../InputFiles')
data = pandas.read_csv(input_dir + r"\reviews.csv", parse_dates=["Timestamp"])


data['Week'] = data["Timestamp"].dt.strftime("%Y - %U")
average = data.groupby('Week').mean()


chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Ratings", classes='text-h3 text-center q-pa-md')
    hc = jp.HighCharts(a=wp, options = chart_def)
    hc.options.title.text = "Average Ratings per Day"
    hc.options.xAxis.categories = list(average.index)
    # x_axis = list(average.index)
    y_axis = list(average['Rating'])
    hc.options.series[0].data = y_axis

    return wp

jp.justpy(app, port=8001)