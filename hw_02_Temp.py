#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt 
import json


with open('Crimes_/global_temp_anomaly.json', encoding='ascii') as f:
    text = f.read()
global_temp_anomaly = json.loads(text)
#print('crime dates = ', crime_dates[0])

x1 = []
for value in global_temp_anomaly['data']:
    x1.append(value)
    x1.sort()

y1 = []
for key in global_temp_anomaly['data'].keys():
    y1.append(global_temp_anomaly['data'][key])
    y1.sort()

with open('Crimes_/global_temp_anomaly.json', encoding='ascii') as f:
    text = f.read()
global_temp_anomaly = json.loads(text)
#print('crime dates = ', crime_dates[0])

x2 = []
for value in global_temp_anomaly['data1']:
    x2.append(value)
    x2.sort()

y2 = []
for key in global_temp_anomaly['data1'].keys():
    y2.append(global_temp_anomaly['data1'][key])
    y2.sort()

plt.figure(figsize = (17,8))
plt.subplot()
plot1 = plt.plot(x1,y1, color='blue', label = 'Global temperature anomalys' )
plot2 = plt.plot(x2,y2, color='red', label = 'USA temperature anomalys' )

plt.xticks(rotation = 90)
plt.legend()
plt.title("Temperature anomalys at different years")

plt.xlabel("Year")

plt.ylabel("Temperature anomalys", )
plt.rcParams.update({'font.size': 24})

spacing = 0.700

plt.subplots_adjust(bottom=spacing)

plt.tick_params(axis='x', which='major', labelsize=10)
plt.tick_params(axis='y', width= 1, which='major', labelsize=8)



plt.tight_layout()

plt.show()