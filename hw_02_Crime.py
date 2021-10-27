
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt 


with open('Crimes_/crimes_street_dates.json', encoding='ascii') as f:
    text = f.read()
import json
crime_dates = json.loads(text)

#print('crime dates = ', crime_dates[0])

x = []
for index in crime_dates:
    x.append(index['date'])

y = []
for index in crime_dates:
    y.append(len(index["stop-and-search"]))


plt.figure(figsize = (15,6))
plt.bar(x,y, color="orange")
plt.xticks(rotation = 90)

plt.legend()

plt.title("Crime dates and number of cities the crimes took place in")

plt.xlabel("Date of the crime")

plt.ylabel("Number of cities the crime took place in")
spacing = 0.100

plt.subplots_adjust(bottom=spacing)

plt.tick_params(axis='x', which='major', labelsize=10)

plt.tight_layout()

plt.show()

