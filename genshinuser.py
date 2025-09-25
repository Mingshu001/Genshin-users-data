import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.animation as animation

# Top countries by player count (from website)
countries = [
    {"name": "China", "lat": 35, "lon": 105, "players": 2736000, "color": "red"},
    {"name": "United States", "lat": 38, "lon": -97, "players": 2554000, "color": "blue"},
    {"name": "Japan", "lat": 36, "lon": 138, "players": 1368000, "color": "orange"},
    {"name": "South Korea", "lat": 37, "lon": 127, "players": 684000, "color": "green"},
    {"name": "Germany", "lat": 51, "lon": 10, "players": 479000, "color": "purple"},
    {"name": "United Kingdom", "lat": 55, "lon": -3, "players": 383000, "color": "cyan"},
    {"name": "France", "lat": 46, "lon": 2, "players": 351000, "color": "magenta"},
    {"name": "Brazil", "lat": -14, "lon": -51, "players": 328000, "color": "yellow"},
    {"name": "Canada", "lat": 56, "lon": -106, "players": 292000, "color": "brown"},
    {"name": "Taiwan", "lat": 23.5, "lon": 121, "players": 274000, "color": "lime"},
]

# Demographics (global, for display)
demographics = {
    "Male": (55, 8360000),
    "Female": (45, 6840000),
    "Under 25 Years": (27, 4104000),
    "25-35 Years": (38, 5776000),
    "Over 35 Years": (35, 5320000),
    "Average User Age": (None, 35)
}

fig, ax = plt.subplots(figsize=(12, 6))

def animate(i):
    ax.clear()
    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, ax=ax)
    m.drawcoastlines()
    m.drawcountries()
    country = countries[i]

    # Plot all countries as faint background
    for c in countries:
        x_bg, y_bg = m(c["lon"], c["lat"])
        ax.scatter(x_bg, y_bg, s=c["players"] / 2000, color=c["color"], alpha=0.2, edgecolors='gray', linewidths=0.5)

    # Highlight current country
    x, y = m(country["lon"], country["lat"])
    ax.scatter(x, y, s=country["players"] / 1000, color=country["color"], alpha=0.85, edgecolors='black', linewidths=2, zorder=5)

    # Title and country info
    ax.set_title('Genshin Impact Top Country Player Counts (Animated)', fontsize=16, pad=20)
    ax.text(0.5, 1.08, f"{country['name']}\nPlayers: {country['players']:,}", transform=ax.transAxes, ha='center', fontsize=16, fontweight='bold')

    # Demographics info
    demo_str = "Player Demographics Profile\n" + "\n".join([
        f"{k}: {v[0]}% ({v[1]:,})" if v[0] is not None else f"{k}: {v[1]} years" for k, v in demographics.items()
    ])
    ax.text(1.02, 0.5, demo_str, transform=ax.transAxes, va='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8), clip_on=False)

    # Zoom effect: convert lon/lat to projected x/y for axis limits
    margin = 30
    x0, y0 = m(country["lon"] - margin, country["lat"] - margin)
    x1, y1 = m(country["lon"] + margin, country["lat"] + margin)
    ax.set_xlim(min(x0, x1), max(x0, x1))
    ax.set_ylim(min(y0, y1), max(y0, y1))

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    return ax,

ani = animation.FuncAnimation(fig, animate, frames=len(countries), interval=1800, blit=False, repeat=True)
plt.tight_layout()
plt.show()