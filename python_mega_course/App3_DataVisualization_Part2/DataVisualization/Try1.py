import justpy as jp
from pandas.core.dtypes.common import classes

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="This is My heading", classes='text-h1 text-center')
    p1 = jp.QDiv(a=wp, text="This is My Paragraph", classes='text-h2')
    return wp

jp.justpy(app, port=8001)