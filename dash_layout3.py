#!/usr/bin/python

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

def import_data():
    try:
        df = pd.read_csv("gdp.csv")

    except FileNotFoundError:
        df = pd.read_csv(
            'https://gist.githubusercontent.com/chriddyp/' +
            '5d1ea79569ed194d432e56108a04d188/raw/' +
            'a9f9e8076b837d541398e999dcbac2b282a81f8/' +
            'gdp-life-exp-2007.csv')

        df.to_csv('gdp.csv')

    return df

def main():
    df = import_data()

if __name__ == '__main__':
    main()
