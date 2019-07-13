from flask import Flask,render_template
import plotly
import plotly.graph_objs as go
import statistics

import numpy as np
import json
app = Flask(__name__)

@app.route("/")
def plotgraph():

    with open('quaninf_arch1_waac.json') as json_file:
        data = json.load(json_file)
        psnr,bpp=[],[]


        for p in data:
            psnr.append(p['psnr'])
            bpp.append(p['bpp'])


        print("x",psnr)
        print("y",bpp)
    mean_x,mean_y=[],[]
    i=0
    while(i<len(psnr)):

        mean_x.append(statistics.mean(psnr[i]))
        mean_y.append(statistics.mean(bpp[i]))
        i=i+1

    print("mean_x",mean_x)
    print("mean_y",mean_y)

    trace0 = go.Scatter(
        x = mean_x,
        y = mean_y,
        mode = 'lines+markers',
        name = 'zeroth'

    )
    data=[trace0]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                               graphJSON=graphJSON)
