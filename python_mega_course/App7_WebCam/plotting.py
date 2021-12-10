from bokeh.models.annotations import Tooltip
from bokeh.models.sources import ColumnarDataSource
from numpy import source
from video_capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df['Start_string'] = df["Start Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
df['End_string'] = df["End Time"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

print(df.head())

p = figure(x_axis_type="datetime", height=100, width=500,
           sizing_mode="scale_both", title="Motion Graph")

hover = HoverTool(
    tooltips=[("Start Time", "@Start_string"), ("End Time", "@End_string")])

p.add_tools(hover)

p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1

p.quad("Start Time", right="End Time",
       bottom=0,  top=1, color='green', source=cds)

output_file("Motion Graph.html")
show(p)
