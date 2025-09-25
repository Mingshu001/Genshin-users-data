import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.basemap import Basemap
import numpy as np

# Placeholder: Replace with actual data fetching/parsing from MMO Population
# For demo, we use random data for 12 months and 5 regions
regions = [
    {"name": "North America", "lat": 40, "lon": -100},
    {"name": "Europe", "lat": 50, "lon": 10},
    {"name": "Asia", "lat": 30, "lon": 110},
    {"name": "South America", "lat": -15, "lon": -60},
    {"name": "Oceania", "lat": -25, "lon": 135},
]
months = pd.date_range(end=pd.Timestamp.today(), periods=12, freq='M')
np.random.seed(42)
data = [
    {"month": m, **{r["name"]: np.random.randint(10000, 1000000) for r in regions}}
    for m in months
]
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 6))
m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, ax=ax)
m.drawcoastlines()
m.drawcountries()

scatters = []
colors = ['red', 'blue', 'green', 'orange', 'purple']

for i, region in enumerate(regions):
    x, y = m(region["lon"], region["lat"])
    scat = ax.scatter([], [], s=[], color=colors[i], label=region["name"], alpha=0.7)
    scatters.append(scat)

month_text = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center', fontsize=16)

ax.legend(loc='upper left')

# Animation function
def animate(i):
    month = df.iloc[i]["month"].strftime('%B %Y')
    month_text.set_text(f"Month: {month}")
    for j, region in enumerate(regions):
        x, y = m(region["lon"], region["lat"])
        size = df.iloc[i][region["name"]] / 1000  # scale for visibility
        scatters[j].set_offsets([[x, y]])
        scatters[j].set_sizes([size])
    return scatters + [month_text]

ani = animation.FuncAnimation(fig, animate, frames=len(df), interval=1000, blit=True, repeat=True)
plt.title('Genshin Impact Daily Active Players by Region (Animated)')
plt.tight_layout()
plt.show()
