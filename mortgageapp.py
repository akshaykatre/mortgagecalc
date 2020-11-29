import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from mortgagecalc import linearmortgage
import dash_table 
import pandas

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#df = pandas.DataFrame()

app.layout = html.Div(children=[
    html.Label('Text Input'),
    dcc.Input(value=0, id="input_number", type='number', debounce=True),
    #dash_table.DataTable(id="table")
        ]
#+ [html.Div(id="out-all-types")]
+ [dash_table.DataTable(
  #  data=[],
    #columns=[],
    columns=[{'id': c, 'name': c} for c in ['x','y','z','a','b']],
 #   page_size=10,
    id='table'
)]
)


@app.callback(
    Output("table", "data"),
   # Output("table", "rows"),
    [Input("input_number", "value") ]
)
def cb_render(input_number):
    if input_number != 0:
        df = pandas.DataFrame(linearmortgage(input_number)).T
        print("here we are ")
        print(df)
        return df.iloc[0:100].to_dict('records')
    else:
        return 


if __name__ == '__main__':
    app.run_server(debug=True)