import csv
import collections
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
germany_data = os.path.join(THIS_FOLDER, 'weather_data_Germany.csv')
ireland_data = os.path.join(THIS_FOLDER, 'weather_data_Ireland.csv')

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

'''
# Round to lessen printed
def roundNum(x):
  return int(x//1 + ((x%1)/0.5)//1)
'''

# Get Median
def median(x):
  x.sort() #sort list
  y = len(x)%2 #get remainder
  z = len(x)/2 #get answer from dividing
  if y == 0: #Remainder is 0, thus number of values is EVEN 
    z = int(z) #Turn into integer
    print("Median:" ,(x[z-1]+x[z])/2) #Add middle two values, then divide by two
  else: #Remainder is a float, thus number of values is ODD
    z = int(z+.5) #To turn into integer
    print("Median: ", x[z-1]) 

# Get Frequency
def frequency(x):
  for i in range(0,len(x)-1):
    print(x[i],"appears",x.count(x[i]),"times")

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

#MONTHLY AVERAGE IRELAND
with open(ireland_data) as csv_file: #opens file
  csv_reader = csv.reader(csv_file, delimiter=',') #Row separated by ','
  monthly_avg_temps_IR = [] #makes a list
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
      monthly_avg_temps_IR.append(temperature) #Add to list
      total_temp = float(row[4]) #Reset total since month has changed
      number_of_readings = 1 #Reset values
      prev_month = this_month #New month
  temperature = (total_temp/number_of_readings) #Last month average
  monthly_avg_temps_IR.append(temperature) #Add to list

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

##MONTHLY AVG GERMANY
with open(germany_data) as csv_file:
  csv_reader = csv.reader(csv_file,delimiter = ',')
  monthly_avg_temps_GM = []
  prev_month = 1
  temperature = 0
  for row in csv_reader:
    this_month = getMM_GM(row[0])
    if this_month == prev_month:
      temperature = temperature + float(row[2])
    else: 
      monthly_avg_temps_GM.append(temperature)
      temperature = float(row[2])
      prev_month = this_month
  monthly_avg_temps_GM.append(temperature)

print("Hypothesis: Is Ireland's weather moderate throughout the year?")
print("Germany's data is used to compare whether Ireland's temperature is moderate throughout the year, as it is surrounded by water, wherein Germany is in mainland, thus the bigger fluctuation of temperature throughout the year.")

##IRELAND AVERAGE INTERFACE
user_average_IR = input("Would you like to get a list of averages for Ireland? : ") #Userinput available if user wants to see the lists
while user_average_IR =='yes': 
  user_date_IR = input("Would you like to choose 'daily' , 'monthly' , or 'yearly'?: ") #Options are given
  if user_date_IR == 'daily':
    print("Daily average temps for Ireland: " , daily_avg_temps_IR) #Prints list 
    print("Value of list: " , len(daily_avg_temps_IR)) #Prints the amt of values
  elif user_date_IR == 'monthly':
    print("Monthly average temps for Ireland: " , monthly_avg_temps_IR) #Prints list
    print("Value of list: ", len(monthly_avg_temps_IR)) #Prints the amt of values
  elif user_date_IR =='yearly':
    print("Yearly average temps for Ireland: " , yearly_avg_temps_IR) #Prints list
    print("Value of list: ", len(yearly_avg_temps_IR)) #Prints the amt of values
  else:
    user_date_IR = input("You must input 'daily' , 'monthly' , or 'yearly': ")
  user_average_IR = input("Would you like to get another list?: ")

##IRELAND MEDIAN INTERFACE
user_median_IR = input("Would you like to get a median for Ireland?: ")
while user_median_IR == 'yes':
  user_date2_IR = input("'daily','monthly', or 'yearly': ")
  if user_date2_IR == 'daily':
    median(daily_avg_temps_IR)   
  elif user_date2_IR == 'monthly':
    median(monthly_avg_temps_IR)   
  elif user_date2_IR == 'yearly':
    median(yearly_avg_temps_IR)
  else:
    user_date2_IR = input("You must input 'daily',monthly', or 'yearly': ")
  user_median_IR = input("Would you like to get a different median?: ")

#mode = max(set(daily_avg_temps),key=daily_avg_temps.count)

##IRELAND MODE INTERFACE
user_mode_IR = input("Would you like to get a mode for Ireland?: ")
while user_mode_IR == 'yes':
  user_date3_IR = input("'daily' , 'monthly' , or 'yearly': ")
  if user_date3_IR == 'daily':
    daily_mode_IR = max(set(daily_avg_temps_IR),key=daily_avg_temps_IR.count) 
    print("Mode of this list: " , daily_mode_IR)
  elif user_date3_IR == 'monthly':
    monthly_mode_IR = max(set(monthly_avg_temps_IR),key=monthly_avg_temps_IR.count)
    print("Mode of this list: " , monthly_mode_IR)
  elif user_date3_IR == 'yearly':
    yearly_mode_IR = max(yearly_avg_temps_IR,key=yearly_avg_temps_IR.count)
    print("Mode of this list: " , yearly_mode_IR)
  else:
    user_date3_IR = input("You must input 'daily' , 'monthly ' , or 'yearly': ")
  user_mode_IR = input("Would you like to get a different mode?: ")

##IRELAND FREQUENCY INTERFACE
user_frequency_IR = input("Would you like to get the frequencies for Ireland?: ")
while user_frequency_IR == 'yes':
  user_date4_IR = input("'daily ' , 'monthly' , or 'yearly': ")
  if user_date4_IR == 'daily':
    daily_frequency_IR = frequency(daily_avg_temps_IR)
    print("Daily frequenct=y list for Ireland:" , daily_frequency_IR)
  elif user_date4_IR == 'monthly':
    monthly_frequency_IR = frequency(monthly_avg_temps_IR)
    print("Monthly frequency list for Ireland: " , monthly_frequency_IR)
  elif user_date4_IR == 'yearly':
    yearly_frequency_IR = frequency(yearly_avg_temps_IR)
    print("Yearly frequency list for Ireland:" , yearly_frequency_IR)
  else:
    user_date_IR = input("You must input 'daily' , 'monthly' , or 'yearly': ")
  user_frequency_IR = input("Would you like to get a different frequency?: ")
 
##GERMANY AVERAGE INTERFACE
user_average_GM = input("Would you like to get a list of averages for Germany?: ") #Userinput available if user wants to see the lists
while user_average_GM =='yes': 
  user_date_GM = input("Would you like to choose 'monthly' or 'yearly'?: ") #Options are given
  if user_date_GM == 'monthly':
    print("Monthly average temps for Germany: " , monthly_avg_temps_GM) #Prints list
    print("Value of list: ", len(monthly_avg_temps_GM)) #Prints the amt of values
  elif user_date_GM =='yearly':
    print("Yearly average temps for Germany: " , yearly_avg_temps_GM) #Prints list
    print("Value of list: ", len(yearly_avg_temps_GM)) #Prints the amt of values
  else:
    user_date_GM = input("You must input 'monthly' or 'yearly': ")
  user_average_GM = input("Would you like to get another list?: ")

##GERMANY MEDIAN INTERFACE
user_median_GM = input("Would you like to get a median for Germany?: ")
while user_median_GM == 'yes':
  user_date2_GM = input("'monthly', or 'yearly': ")
  if user_date2_GM == 'monthly':
    median(monthly_avg_temps_GM)   
  elif user_date2_GM == 'yearly':
    median(yearly_avg_temps_GM)
  else:
    user_date2_GM = input("You must input 'daily',monthly', or 'yearly': ")
  user_median_GM = input("Would you like to get a different median?: ")

##GERMANY MODE INTERFACE
user_mode_GM = input("Would you like to get a mode for Germany?: ")
while user_mode_GM == 'yes':
  user_date3_GM = input("'monthly' or 'yearly': ")
  if user_date3_GM == 'monthly':
    monthly_mode_GM = max(monthly_avg_temps_GM,key=monthly_avg_temps_GM.count)
    print("Mode of this list: " , monthly_mode_GM)
  elif user_date3_GM == 'yearly':
    yearly_mode_GM = max(yearly_avg_temps_GM,key=yearly_avg_temps_GM.count)
    print("Mode of this list: " , yearly_mode_GM)
  else:
    user_date3_GM = input("You must input 'monthly ' or 'yearly': ")
  user_mode_GM = input("Would you like to get a different mode?: ")


