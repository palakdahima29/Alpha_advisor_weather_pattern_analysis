import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data = {
    "Month": months,
    "Region A Temp (°C)": [15, 16, 18, 20, 22, 25, 28, 28, 25, 22, 18, 16],
    "Region A Humidity (%)": [80, 78, 75, 72, 70, 68, 65, 65, 70, 75, 78, 80],
    "Region A Rainfall (mm)": [50, 45, 60, 80, 100, 120, 140, 120, 90, 70, 60, 50],
    
    "Region B Temp (°C)": [5, 6, 8, 12, 15, 18, 20, 20, 18, 14, 10, 6],
    "Region B Humidity (%)": [85, 83, 80, 78, 75, 73, 70, 70, 72, 75, 78, 82],
    "Region B Rainfall (mm)": [120, 110, 100, 120, 150, 180, 190, 180, 140, 120, 100, 110],
    
    "Region C Temp (°C)": [30, 31, 32, 34, 36, 38, 40, 39, 38, 36, 32, 30],
    "Region C Humidity (%)": [50, 52, 55, 58, 60, 65, 68, 65, 60, 58, 55, 52],
    "Region C Rainfall (mm)": [10, 15, 30, 40, 50, 60, 70, 65, 50, 40, 30, 15],
}

df = pd.DataFrame(data)
df.set_index("Month", inplace=True)

fig, ax = plt.subplots(3, 1, figsize=(10, 12))

ax[0].plot(df.index, df['Region A Temp (°C)'], label='Region A', marker='o')
ax[0].plot(df.index, df['Region B Temp (°C)'], label='Region B', marker='s')
ax[0].plot(df.index, df['Region C Temp (°C)'], label='Region C', marker='^')
ax[0].set_title("Monthly Temperature Trends")
ax[0].set_ylabel("Temperature (°C)")
ax[0].legend()

ax[1].plot(df.index, df['Region A Humidity (%)'], label='Region A', marker='o')
ax[1].plot(df.index, df['Region B Humidity (%)'], label='Region B', marker='s')
ax[1].plot(df.index, df['Region C Humidity (%)'], label='Region C', marker='^')
ax[1].set_title("Monthly Humidity Trends")
ax[1].set_ylabel("Humidity (%)")
ax[1].legend()

ax[2].plot(df.index, df['Region A Rainfall (mm)'], label='Region A', marker='o')
ax[2].plot(df.index, df['Region B Rainfall (mm)'], label='Region B', marker='s')
ax[2].plot(df.index, df['Region C Rainfall (mm)'], label='Region C', marker='^')
ax[2].set_title("Monthly Rainfall Trends")
ax[2].set_ylabel("Rainfall (mm)")
ax[2].legend()

plt.tight_layout()
plt.show()
