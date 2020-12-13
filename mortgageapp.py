import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from mortgagecalc import linearmortgage, annuity
import dash_table 
import pandas
import pdb
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#["style.css"]
#external_stylesheets = ['https://codepen.io/zootia/pen/MweMmB']

df = pandas.DataFrame()
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#df = pandas.DataFrame()

app.layout = html.Div( className='test',
            children=
        [    
        html.Label('Mortgage Amount', id='mortamount'),
        dcc.Input(value=0, id="mortgageamount", type='number'),
        html.Label('Interest Rate', id='intrate'),
        dcc.Input(value=1.9, id='interestrate', type='number'),
        html.Label('Years of repayment', id='yearrepay'),
        dcc.Input(value=30, id='repaymentyears', type='number', debounce=True)]
        +[html.Label('Total Interest'), html.Div(id='total_interest')]
        + [html.Label('First Monthly Payment'), html.Div(id='first_monthly_payment')]
        + [html.Label('Last Monthly Payment'), html.Div(id='last_monthly_payment')]

#+ [html.Label(''), html.Div(id='test')]
        #+[dcc.Graph(id='graph', )]
      #+ [dcc.Graph(id='linebar', figure={go.})]
)

#pdb.set_trace()

@app.callback(
   # Output("table", "data"),
    Output("total_interest", "children"),
    Output("first_monthly_payment", "children"),
    Output("last_monthly_payment", "children"),
    
   # Output("table", "rows"),
    [Input("mortgageamount", "value"), Input('interestrate', "value"), 
        Input('repaymentyears', "value") ]
    
)
def cb_render(mortgageamount,interestrate, repaymentyears):
    print(mortgageamount)
    if mortgageamount is None or mortgageamount == 0:
        print("It also enters here")
        return 0, 0, 0 
    else:
        df = pandas.DataFrame(linearmortgage(mortgageamount, rate=interestrate, time=repaymentyears)).T
        df.columns = ['principal', 'rprincipal', 'fixedpayment', 
                        'monthlyinterest', 'monthlypayment']
        print("here we are ")
        print(df)
        return df['monthlyinterest'].sum(), df['monthlypayment'][0], df['monthlypayment'].iloc[-1]



if __name__ == '__main__':
    app.run_server(debug=True)