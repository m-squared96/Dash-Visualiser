#!/usr/bin/python

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

def generate_table(data, max_rows):
    return html.Table(
        [html.Tr([html.Th(col) for col in data.columns])] +
        [html.Tr([
            html.Td(data.iloc[i][col]) for col in data.columns
        ]) for i in range(min(len(data), max_rows))]
    )

df = pd.read_csv("train.csv")

app = dash.Dash()

app.layout = html.Div(children=[
    html.H4(children='Ames, Iowa, Property Data'),
    generate_table(df, 10)
])

if __name__ == '__main__':
    app.run_server(debug=True)
