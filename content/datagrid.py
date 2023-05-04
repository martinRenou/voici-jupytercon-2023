from bqplot import LinearScale, ColorScale, OrdinalColorScale, OrdinalScale
from json import loads
from requests import get
import pandas as pd
from ipydatagrid import DataGrid, TextRenderer, BarRenderer, Expr
renderers = {
    "Acceleration": BarRenderer(horizontal_alignment="center",
                                bar_color=ColorScale(min=0, max=20, scheme="viridis"),
                                bar_value=LinearScale(min=0, max=20)),
    "Miles_per_Gallon": TextRenderer(background_color=Expr('"grey" if cell.value is None else default_value')),
    "Origin": TextRenderer(text_color="black",
                           background_color=OrdinalColorScale(domain=["USA", "Japan", "Europe"]),
                           horizontal_alignment=Expr("'right' if cell.value in ['USA', 'Japan'] else 'left'"))
}