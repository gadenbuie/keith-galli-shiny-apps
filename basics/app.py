from pathlib import Path

import pandas as pd

from shiny import reactive
from shiny.express import render, ui, input

from shinywidgets import render_plotly
import plotly.express as px

@reactive.calc
def dat():
    infile = Path(__file__).parent / "data/sales_with_coords.csv"
    return pd.read_csv(infile)

ui.input_numeric("item_count", "Number of items to show", 1, min=1, max=20)  

@render_plotly
def top_sellers():
    df = dat()
    top_5_products = df.groupby("product")["quantity_ordered"].sum().nlargest(input.item_count()).reset_index()
    fig = px.bar(top_5_products, x="product", y="quantity_ordered")
    return fig