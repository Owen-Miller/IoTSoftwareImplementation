from django.http import HttpResponse, HttpResponseRedirect
import csv
import urllib.request
import codecs
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
from django.shortcuts import render
import matplotlib.dates as md
import datetime as dt
import csv
import time


def home(request):
    return render(request, 'index.html')


def latest(request):
    # Use bigsense API to download last [n] data points
    startnumber = 50
    url = 'http://206.189.227.139:8181/Query/Latest/'+str(startnumber)+'.csv?RelayID=pIoT&Units=Standard'
    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    data = []

    if request.method == 'POST':
        number = request.POST.get('number')
        url = 'http://206.189.227.139:8181/Query/Latest/' + str(number) + '.csv?RelayID=pIoT&Units=Standard'
        return HttpResponseRedirect(url)

    try:
        for column in csvfile:
            # From the downloaded csv use the 2nd and 7th column, data and temp respectively
            data.append((column[1], column[6]))
    except IndexError:
        pass

    # Massaging the data for formatting when plotted
    response = MakeGraph(data)

    return response


def daterange(request):
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        start = str(start).replace('-', '')
        end = str(end).replace('-', '')
        checkbox = request.POST.getlist('Check1')

        url = 'http://206.189.227.139:8181/Query/DateRange/' + start + '/' + end + '.csv?Units=Standard'

        ftpstream = urllib.request.urlopen(url)
        csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
        data = []

        for x in checkbox:
            if x:
                return HttpResponseRedirect(url)
        try:
            for column in csvfile:
                # From the downloaded csv use the 2nd and 7th column, data and temp respectively
                data.append((column[1], column[6]))
        except IndexError:
            pass

        response = MakeGraph(data)
        return response


def MakeGraph(data):
    # Remove colume headings from the data
    data = data[1:]

    # Reversed the data so time flows in positive direction
    data.reverse()

    y = [x[1] for x in data]
    y = [float(s) for s in y]
    x = [x[0] for x in data]

    x = [dt.datetime.strptime(y, '%Y-%m-%d %H:%M:%S.%f') for y in x]
    x = md.date2num(x)

    fig = plt.figure(figsize=(12, 7.5))
    ax = fig.add_subplot(111)

    ax.plot_date(x, y, xdate=True)
    # xfmt = md.DateFormatter('%m-%d %H:%M')

    # ax.xaxis.set_major_formatter(xfmt)
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature [F]')

    # Rotate the ticks on X axis for readability
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

    buf = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buf)

    return HttpResponse(buf.getvalue(), content_type='image/png')
