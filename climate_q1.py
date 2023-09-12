import matplotlib.pyplot as plt

import sqlite3

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

years = []
co2 = []
temp = []

cursor.execute("SELECT Year FROM ClimateData")
print("fetchall:")
result = cursor.fetchall()
for y in result:
    years.append(y)

cursor.execute("SELECT CO2 FROM ClimateData")
print("fetchall:")
result = cursor.fetchall()
for c in result:
    co2.append(c)

cursor.execute("SELECT Temperature FROM ClimateData")
print("fetchall:")
result = cursor.fetchall()
for t in result:
    temp.append(t)

connection.commit()
connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
