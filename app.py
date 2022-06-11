from flask import Flask, url_for, redirect, make_response
 
import sys
import random
import pandas as pd
import quandl
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

quandl.ApiConfig.api_key = 'Kxj1hKpiLH4vM5KTCBs9'

data = quandl.Dataset('WIKI/AMZN').data().to_pandas()


class ReverseProxied(object):
    def __init__(self, app):
        self.app = app
 
    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]
        return self.app(environ, start_response)
 
 
app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)
 
 
@app.route('/')
def index_page():
    msg = "A call to flask's url_for('another_page') returns <a href=\"" + url_for('another_page') + "\">" + url_for('another_page') + "</a> (which has the 'r/notebookSession' component).<br/><br/>" + \
          "A link to a redirect 'redirect_test' which then goes to url_for('another_page'): <a href=\"" + url_for('redirect_test') + "\">" + url_for('redirect_test') + "</a>.<br/><br/>" + \
          "A link to a Plot which uses quandl: <a href=\"" + url_for('plot') + "\">" + url_for('plot') + "</a>.<br/><br/>"
    return msg
 
@app.route('/redirect_test')
def redirect_test():
    return redirect( url_for('another_page') )
 
 
@app.route('/another_page')
def another_page():
    msg = "You made it with redirect( url_for('another_page') ).<br/><br/>" + \
          "A call to flask's url_for('index_page') returns <a href=\"" + url_for('index_page') + "\">" + url_for('index_page') + "</a>."
    return msg
    
@app.route('/plot.png')
def plot():
  fig = Figure()  
  p = fig.add_subplot(1, 1, 1)
  close = data['Adj. Close']
  p.plot(close)

  canvas = FigureCanvas(fig)
  output = BytesIO()
  canvas.print_png(output)
  response = make_response(output.getvalue())
  response.mimetype = 'image/png'
  return response