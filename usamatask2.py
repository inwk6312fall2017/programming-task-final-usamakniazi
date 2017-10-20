from weather import Weather
weather = Weather()
# Lookup via location name.
location = weather.lookup_by_location('halifax')
condition = location.condition()
print (condition['text'])
#Gives you all the days inside
a list and the days will be of sublists
all_days=[]
i=0
    for forecasts in location.forecast():
    if i<5:
    daily = []
    daily.append(forecasts['text'])
    daily.append(forecasts['date'])
    daily.append(forecasts['high'])
    daily.append(forecasts['low'])
    all_days.append(daily)
   i+=1
print(all_days)
#Day has the highest temp
maxT=0
    for day in all_days:
     if int(day[2])>int(maxT):
     maxT=day[2]
     that_day = day[1]
print("The
hottest day is on "+that_day +' and the temparature is '+
maxT)
least=10000#Some
random high number just for comparing sake
      for day in all_days:
       if int(day[3])<int(least):
     least=day[3]
     that_day=day[1]
print("The
coldest day is on "+that_day+' and the tempearature is '+least)
     for day in all_days:
     if day[0]=='Cloudy':
     that_day=day[1]
print("The
chances that it may rain on "+day[1]+" is more since it is "+day[0])
else:
pass
