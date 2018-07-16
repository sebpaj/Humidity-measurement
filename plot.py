import matplotlib.pyplot as plt
import datetime

sorted_data = []
dht11_humidity = []
time = []

with open("output.txt","r") as file:
    data = file.readlines()

for var in data:
    if len(var) == 90:
        sorted_data.append(var)

for var in sorted_data:
    time.append(datetime.datetime.strptime(var[81:89], "%H:%M:%S"))
    dht11_humidity.append(var[43:49])

figPres = plt.figure(figsize=(12,8.5))
axPres = figPres.add_subplot(111)
plt.plot(time, dht11_humidity)
plt.title("Humidity sensor", fontsize=18)
axPres.yaxis.set_label_coords(-0.02,1.02)
axPres.xaxis.set_label_coords(1.0275, -0.005)
plt.ylabel("[%]", fontsize=14, rotation=0)
plt.xlabel("[t]", fontsize=14)
plt.savefig("diagram.png")
