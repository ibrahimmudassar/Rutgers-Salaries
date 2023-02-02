import plotly.express as px
import pandas as pd

df = pd.read_csv("rutgers_salaries.csv")

# If you want to filter by people with the professor title in their name
# df = df[df["Title"].str.contains("PROF")]

fig = px.treemap(df,
                 path=[px.Constant("All"), "Campus", "Depart", "Name"],
                 values="Total Pay",
                 color="Total Pay",
                 color_continuous_scale="Reds",
                 hover_data=['Name', "Title"])

fig.update_traces(root_color="grey")

fig.update_layout(title={
    'text': "Rutgers Salaries Sorted by Campus and Department", "x": 0.5, "xanchor": "center"})

# Attribution
fig.add_annotation(text="By: Ibrahim Mudassar",
                   xref="paper", yref="paper",
                   x=1, y=-0.14,
                   showarrow=False,
                   align="center",
                   font=dict(size=9))

fig.show()

fig1 = px.histogram(df, x="Total Pay")
fig1.show()

fig2 = px.box(df, x="Total Pay", y="Campus", color="Campus", points=False,  # no data points
              hover_data=["Name", "Campus", "Depart"])
fig2.show()
