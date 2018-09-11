#!/usr/bin/python

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

def import_data():
    try:
        df = pd.read_csv("indicators.csv")
        print("File imported")

    except FileNotFoundError:
        print("File not imported, pulling from web")
        df = pd.read_csv(
            "https://gist.githubusercontent.com/chriddyp/" +
            "cb5392c35661370d95f300086accea51/raw/" +
            "8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/" +
            "indicators.csv")

        df.to_csv("indicators.csv")    
        print("File downloaded")

    return df

df = import_data()
#print(df)
