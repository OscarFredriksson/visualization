from bokeh.plotting import figure, show, curdoc
from bokeh.models import Slider, ColumnDataSource, HoverTool
from bokeh.layouts import layout, gridplot
from bokeh.models.glyphs import Circle

from collections import defaultdict
import math
import pandas as pd


df = pd.read_csv("datasets/IMDB_movies/imdb_movie_metadata.csv")

df = df.filter(["imdb_score", "gross", "budget", "movie_title", "title_year"])

df = df[df.gross > 0]  # Filter out rows without gross data
df = df[df.imdb_score > 0]  # Filter out rows without score data
df = df[df.budget > 0]  # Filter out rows without budget data

df = df.sort_values("imdb_score")

print(df)

source = ColumnDataSource(
    data=dict(
        score=df["imdb_score"],
        gross=df["gross"],
        budget=df["budget"],
        title=df["movie_title"],
        year=df["title_year"],
    )
)

hover_tool = HoverTool(
    tooltips=[
        ("Title", "@title"),
        ("Year", "@year"),
        ("Gross", "$@gross"),
        ("Budget", "$@budget"),
        ("Imdb score", "@{score}{0.1f}"),
    ]
)

tools = "box_select,box_zoom,reset"

fill_color = "red"
line_color = "red"
fill_color = "gray"
graph_size = 600
circle_size = 8

selection_glyph = Circle(fill_color=fill_color, fill_alpha=1, line_color=line_color)
nonselection_glyph = Circle(fill_color=fill_color, fill_alpha=0.1, line_color=None)


# # create a new plot with a title and axis labels
left = figure(
    tools=tools,
    title="",
    # y_range=source.data["y"],
    x_axis_label="IMDB Score (0-10)",
    y_axis_label="Gross",
    plot_width=graph_size,
    plot_height=graph_size,
)

left_circle = left.circle(
    x="score",
    y="gross",
    source=source,
    fill_alpha=0.5,
    fill_color=fill_color,
    line_color=line_color,
    size=circle_size,
)

left.left[0].formatter.use_scientific = False
left_circle.selection_glyph = selection_glyph
left_circle.nonselection_glyph = nonselection_glyph

left.add_tools(hover_tool)

right = figure(
    tools=tools,
    title="",
    # y_range=source.data["y"],
    x_axis_label="Year",
    y_axis_label="Budget",
    plot_width=graph_size,
    plot_height=graph_size,
)

right_circle = right.circle(
    x="year",
    y="budget",
    source=source,
    fill_alpha=0.5,
    fill_color=fill_color,
    line_color=line_color,
    size=circle_size,
)

right.left[0].formatter.use_scientific = False
right_circle.selection_glyph = selection_glyph
right_circle.nonselection_glyph = nonselection_glyph

right.add_tools(hover_tool)

p = gridplot([[left, right]])

show(p)
# p.circle()