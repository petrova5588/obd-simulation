import pandas as pd
import random
from datetime import datetime,timedelta
data=[]
start=datetime.now()

for i in range(100):
    time=start+timedelta(seconds=i*5)
    rpm=random.randint(800,4000)
    speed=random.randint(0,200)
    heat=random.randint(70,100)
    data.append([time,rpm,speed,heat])
df=pd.DataFrame(data,columns=["Time","RPM","Speed","Heat"])

df.to_csv("obd_simulation.csv",index=False)

import matplotlib.pyplot as plt 
df=pd.read_csv("obd_simulation.csv")
df["Time"]=pd.to_datetime(df["Time"])

plt.figure(figsize=(14,8))

plt.subplot(3,1,1)
plt.plot(df["Time"],df["RPM"],color="red")
plt.title("Engine Speed(RPM)")
plt.ylabel("RPM")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(df["Time"],df["Speed"],color="blue")
plt.title("Car Speed")
plt.ylabel("Speed(km/h)")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(df["Time"],df["Heat"],color="green")
plt.title("Heat")
plt.ylabel("Heat(C)")
plt.xlabel("Time")
plt.grid(True)

plt.tight_layout()
plt.show()
