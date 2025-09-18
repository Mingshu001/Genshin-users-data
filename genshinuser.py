import plotly.graph_objs as go
import pandas as pd

# Genshin Impact monthly active player data (from prioridata.com, sample selection)
data = [
	["September 2020", 16535456],
	["November 2020", 18578549],
	["January 2021", 26408972],
	["March 2021", 29550149],
	["May 2021", 39855016],
	["July 2021", 43660144],
	["September 2021", 50188791],
	["November 2021", 56022479],
	["January 2022", 57850014],
	["March 2022", 61023770],
	["May 2022", 62021146],
	["July 2022", 62750449],
	["September 2022", 63014545],
	["November 2022", 65014545],
	["January 2023", 65521480],
	["March 2023", 65039242],
	["May 2023", 65706117],
	["July 2023", 63956502],
	["September 2023", 65682295],
	["November 2023", 63593682],
	["January 2024", 65720592],
	["March 2024", 65200000],
	["May 2024", 65706117],
	["July 2024", 63956502],
	["September 2024", 65682295],
]

df = pd.DataFrame(data, columns=["Month", "Monthly Active Players"])
df["Month"] = pd.to_datetime(df["Month"], format="%B %Y")
df = df.sort_values("Month")

fig = go.Figure()
fig.add_trace(go.Scatter(
	x=df["Month"],
	y=df["Monthly Active Players"],
	mode="lines+markers",
	line=dict(color="royalblue", width=3),
	marker=dict(size=8),
	name="Monthly Active Players"
))
fig.update_layout(
	title="Genshin Impact Monthly Active Players (2020-2024)",
	xaxis_title="Month",
	yaxis_title="Players",
	hovermode="x unified",
	template="plotly_white"
)
fig.show()