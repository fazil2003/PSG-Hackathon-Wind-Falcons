from flask import Flask, request, render_template
# from backend import get_shops
# from dataFile import dataCoordinates
from mongoAccess import accessRoute

import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["APPLICATION_ROOT"] = "/"

@app.route('/')
def loc():
    return render_template('index.html')

@app.route('/senddata', methods=["GET", "POST"])
async def sendData():
    startingLocation = request.form["start"]
    destinationLocation = request.form["end"]
    # print(startingLocation)
    # print(destinationLocation)
    dataCoordinates = accessRoute(startingLocation, destinationLocation)

    data = []
    if (len(dataCoordinates)>1000):
        dataCoordinates = dataCoordinates[::100]

    for i in dataCoordinates:
        data.append([i[1], i[0]])

    polyLine = "L.polyline({data}).addTo(map).bindPopup('popup').openPopup();".format(data = data)

    # Render the page with the map
    return render_template('results.html', district = startingLocation, markers=polyLine, lat=data[0][0], lon=data[0][1])


def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    
    flike = io.BytesIO()
    plt.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()
    # plt.show()
    return b64
    
@app.route('/plot', methods=["GET", "POST"])
def getDetails():

    districtName = request.args['district']

    mergedDf = pd.read_csv('final_file.csv')

    districtNameUpper = districtName.upper()

    yearsCol = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"]
    li = []
    for year in yearsCol:
        li.append(mergedDf.query("DISTRICT == '" + districtNameUpper + "'")[year].values.tolist()[0])
    
    yearSeries = pd.Series(li)

    title = "Total IPC Crimes by Year in city " + districtNameUpper
    
    imageFile = plot_df(mergedDf, x = yearsCol, y = yearSeries, title=title )

    return render_template('plot.html', plottingImage=imageFile)


if __name__ == '__main__':
    app.run(debug = True) 