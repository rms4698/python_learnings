import justpy as jp
import os
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
from pandas.core import series
from pytz import utc

dirname = os.path.dirname(__file__)
input_dir = os.path.join(dirname, '../InputFiles')
data = pandas.read_csv(input_dir + r"\reviews.csv", parse_dates=["Timestamp"])

share = data.groupby(['Course Name'])['Rating'].count()
print(share.head())

chart_def = """
 {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Ratings',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Ratings",
                 classes='text-h3 text-center q-pa-md')
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Ratings per Day"
    hc.options.series[0].data = [{'name':course, 'y':percent} for course, percent in zip(share.index, list(share))]
    return wp


jp.justpy(app, port=8001)
 