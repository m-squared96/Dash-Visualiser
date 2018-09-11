#!/usr/bin/python

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

x_vals = list(i for i in range(1,11))
sf_vals = [2,3,1,5,6,7,5,4,7,8]
mon_vals = [3,3,4,5,7,7,8,10,9,11]

colours = {
    'background':'#111111',
    'text':'#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor':colours['background']},children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign':'center',
            'color':colours['text']
        }
    ),

    html.Div(
        children='''
            Trying out a data-centric web framework
        ''',
        style={
            'textAlign':'center',
            'color':colours['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x':x_vals,'y':sf_vals,'type':'bar','name':'SF'},
                {'x':x_vals,'y':mon_vals,'type':'bar','name':u'Montreal'}
            ],
            'layout':{
                'title':'Dash Data Visualisation',
                'plot_bgcolor':colours['background'],
                'paper_bgcolor':colours['background'],
                'font':{
                    'color':colours['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
