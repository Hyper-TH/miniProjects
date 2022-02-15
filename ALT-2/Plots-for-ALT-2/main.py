import csv 
import collections
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
germany_data = os.path.join(THIS_FOLDER, 'weather_data_Germany.csv')
ireland_data = os.path.join(THIS_FOLDER, 'weather_data_Ireland.csv')

import plotly as py
import plotly.graph_objs as go

# Extract the month from a date string e.g. '01/02/1988 05:00' will return 2
def getMM_IR(dateStr):
  return int(dateStr[3:5]) #indicates specific month, 4th and 5th number

# Extract the year from a date string
def getYY_IR(dateStr):
  return int(dateStr[6:10])

# Extract the day from a date string
def getDD_IR(dateStr):
  return int(dateStr[0:2])

def getMM_GM(dateStr):
  return int(dateStr[0:2])

def getYY_GM(dateStr):
  return int(dateStr[0:4])

##MONTHLY AVG GERMANY
with open(germany_data) as csv_file:
  csv_reader = csv.reader(csv_file,delimiter = ',')
  monthlyavgtempsGM = []
  prev_month = 1
  temperature = 0
  for row in csv_reader:
    this_month = getMM_GM(row[0])
    if this_month == prev_month:
      temperature = temperature + float(row[2])
    else: 
      monthlyavgtempsGM.append(temperature)
      temperature = float(row[2])
      prev_month = this_month
  monthlyavgtempsGM.append(temperature)

#MONTHLY AVERAGE IRELAND
with open(ireland_data) as csv_file: #opens file
  csv_reader = csv.reader(csv_file, delimiter=',') #Row separated by ','
  monthlyavgtempsIR = [] #makes a list
  total_temp = 0 #total temp of a month
  prev_month = 1 #Starting month
  number_of_readings = 0  #sets number of reading to 0 
  temperature = 0 #Total temp
  for row in csv_reader: #For each row
    this_month = getMM_IR(row[0]) #Current month
    if this_month == prev_month: #While on same month
      number_of_readings = number_of_readings + 1 #List value increases
      total_temp = total_temp + float(row[4]) #Get temp from row 4
    else: #New month
      temperature = (total_temp/number_of_readings) #Get average
      monthlyavgtempsIR.append(temperature) #Add to list
      total_temp = float(row[4]) #Reset total since month has changed
      number_of_readings = 1 #Reset values
      prev_month = this_month #New month
  temperature = (total_temp/number_of_readings) #Last month average
  monthlyavgtempsIR.append(temperature) #Add to list

#DAILY AVERAGE IRELAND
with open(ireland_data) as csv_file: #opens file
  csv_reader = csv.reader(csv_file, delimiter=',') #Each row separated by ','
  daily_avg_temps_IR = [] #Makes a list
  total_temp = 0 #Total
  prev_day = 1 #First day
  number_of_readings = 0 #Value for a day
  temperature = 0 #Final temp
  for row in csv_reader: #For every row (separated by ',')
    this_day = getDD_IR(row[0]) #Current day
    if this_day == prev_day: #While on same day
      number_of_readings = number_of_readings + 1 #List value increases
      total_temp = total_temp +float(row[4]) #Get temp from row 4 
    else: #If new day
      temperature = (total_temp/number_of_readings) #Get average for the day
      daily_avg_temps_IR.append(temperature) #Append to list
      total_temp = float(row[4]) #Reset total
      number_of_readings = 1 #Restart value for the day
      prev_day = this_day #New day
  temperature = (total_temp/number_of_readings) #Last day average
  daily_avg_temps_IR.append(temperature) #Add to list

#YEARLY AVERAGE IRELAND
with open(ireland_data) as csv_file: #opens file
  csv_reader = csv.reader(csv_file, delimiter=',') #Each row separated by ','
  yearly_avg_temps_IR = [] #Makes a list
  total_temp = 0 #Total
  prev_year = 1988 #First year
  number_of_readings = 0 #Value for a year
  temperature = 0 #Final temp
  for row in csv_reader: #For every row (separated by ',')
    this_year = getYY_IR(row[0]) #Current year
    if this_year == prev_year: #While on same year
      number_of_readings = number_of_readings + 1 #List value increases
      total_temp = total_temp +float(row[4]) #Get temp from row 4
    else: #If new year
      temperature = (total_temp/number_of_readings) #Get average for the year
      yearly_avg_temps_IR.append(temperature) #Append to list
      total_temp = float(row[4]) #Reset total
      number_of_readings = 1 #Reset value for the year
      prev_year = this_year #New year
    temperature = (total_temp/number_of_readings) #Last year average
  yearly_avg_temps_IR.append(temperature) #Add to list

#YEARLY AVERAGE GERMANY
with open(germany_data) as csv_file: #opens file
  csv_reader = csv.reader(csv_file, delimiter=',') #Each row separated by ','
  yearly_avg_temps_GM = [] #Makes a list
  total_temp = 0 #Total
  prev_year = 1985 #First year
  number_of_readings = 0 #Value for a year
  temperature = 0 #Final temp
  for row in csv_reader: #For every row (separated by ',')
    this_year = getYY_GM(row[1]) #Current year
    if this_year == prev_year: #While on same year
      number_of_readings = number_of_readings + 1 #List value increases
      total_temp = total_temp + float(row[2]) #Get temp from row 2
    else: #If new day
      temperature = (total_temp/number_of_readings) #Get average for the year
      yearly_avg_temps_GM.append(temperature) #Append to list
      total_temp = float(row[2]) #Reset total
      number_of_readings = 1 #Restart value for the day
      prev_year = this_year #New day
  temperature = (total_temp/number_of_readings) #Last day average
  yearly_avg_temps_GM.append(temperature) #Add to list


month =["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]

'''
    #1988 Germany and Ireland
    Germany1988 = go.Scatter(
      x= month,
      y=monthlyavgtempsGM[36:48],
      name = 'Germany '
    )
    Ireland1988 = go.Scatter(
        x=month,
        y=monthlyavgtempsIR[0:12],
        name = 'Ireland '
    )
    data = [Germany1988, Ireland1988]
    layout = go.Layout(
        title=go.layout.Title(
            text='Germany and Ireland 1988',
            xref='paper',
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Month',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Temperature in Celsius',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='Germany and Ireland 1988.html')


    #2015 Germany and Ireland
    Germany2015 = go.Scatter(
      x = month,
      y = monthlyavgtempsGM[360:372],
      name = 'Germany',
    )
    Ireland2015 = go.Scatter(
      x = month,
      y = monthlyavgtempsIR[324:336],
      name = 'Ireland',
    )
    data = [Germany2015, Ireland2015]
    layout = go.Layout(
        title=go.layout.Title(
            text='Germany and Ireland 2015',
            xref='paper',
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Month',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Temperature in Celsius',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='Germany and Ireland 2015.html')

    #1988 and 2015 
    Germany1988 = go.Scatter(
      x= month,
      y=monthlyavgtempsGM[36:48],
      name = 'Germany 1988'
    )
    Ireland1988 = go.Scatter(
        x=month,
        y=monthlyavgtempsIR[0:12],
        name = 'Ireland 1988'
    )
    Germany2015 = go.Scatter(
      x = month,
      y = monthlyavgtempsGM[360:372],
      name = 'Germany 2015'
    )
    Ireland2015 = go.Scatter(
      x = month,
      y = monthlyavgtempsIR[324:336],
      name = 'Ireland 2015'
    )
    data = [Germany1988, Ireland1988,Germany2015, Ireland2015]
    layout = go.Layout(
        title=go.layout.Title(
            text='Germany and Ireland 2015 and 2018',
            xref='paper',
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Month',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Temperature in Celsius',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='Germany and Ireland 1988 and 2015.html')

    #1988 and 2015 Ireland
    Ireland1988 = go.Scatter(
        x=month,
        y=monthlyavgtempsIR[0:12],
        name = 'Ireland 1988'
    )
    Ireland2015 = go.Scatter(
      x = month,
      y = monthlyavgtempsIR[324:336],
      name = 'Ireland 2015',
    )
    data = [Ireland1988, Ireland2015]
    layout = go.Layout(
        title=go.layout.Title(
            text='Ireland 1988 and 2015',
            xref='paper',
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Month',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Temperature in Celsius',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.plot(fig, filename='Ireland 2015 and 2018.html')
'''
print(len(yearly_avg_temps_IR))

x = 1988
year = []
while x != 2019:
  year.append(x)
  x = x + 1

print(year)
print(len(year))

#1988 and 2015 Ireland
IrelandYearly = go.Scatter(
    x=year,
    y=yearly_avg_temps_IR,
    name = 'Ireland'
)
data = [IrelandYearly]
layout = go.Layout(
    title=go.layout.Title(
        text='Ireland Yearly',
        xref='paper',
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='Year',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='Temperature in Celsius',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
)
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='Ireland Yearly.html')
