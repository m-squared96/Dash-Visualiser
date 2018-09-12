#!/usr/bin/python

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
all_options = {
    'Amercia':['New York','San Fran','Washington'],
    'Canada':['Montreal','Toronto','Ottawa'],
    'Ireland':['Dublin','Cork','Limerick']
}
app.layout = html.Div([
    dcc.RadioItems(
        id='countries-dropdown',
        options=[{'label':k,'value':k} for k in all_options.keys()],
        value='America'
    ),

    html.Hr(),
    dcc.RadioItems(id='cities-dropdown'),

    html.Hr(),
    html.Div(id='display-selected-values')
])

@app.callback(
    Output('cities-dropdown','options'),
    [Input('countries-dropdown','value')])
def set_cities_options(selected_country):
    return [{'label':i,'value':i} for i in all_options[selected_country]]

@app.callback(
    Output('cities-dropdown','value'),
    [Input('cities-dropdown','options')])
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('display-selected-values','children'),
    [Input('countries-dropdown','value'),
    Input('cities-dropdown','value')])
def set_display_children(selected_country,selected_city):
    return u'{} is a city in {}'.format(
        selected_city,selected_country)

if __name__=='__main__':
    app.run_server(debug=True)
