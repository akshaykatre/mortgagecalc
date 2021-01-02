import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from mortgagecalc import linearmortgage, annuity, interestbounds
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
        html.Label('Every month I can contribute the following amount towards my mortgage', id='contributionheader'),
        dcc.Input(value=0, id='mip'),
        html.Label('That amount can vary by', id='variation'),
        dcc.Input(value=0, id='limits'),
        html.Label('The house I want to buy costs (assume 100% mortgage)', id='mortamount'),
        dcc.Input(value=0, id="mortgageamount", type='number'),
        #html.Label('Interest Rate', id='intrate'),
        #dcc.Input(value=1.9, id='interestrate', type='number'),
        html.Label('I want a term of', id='yearrepay'),
        dcc.Input(value=30, id='repaymentyears', type='number', debounce=True)]
        +[html.Label('Your options are:'), html.Div(id='information')]
        #+ [html.Label('First Monthly Payment'), html.Div(id='first_monthly_payment')]
        #+ [html.Label('Last Monthly Payment'), html.Div(id='last_monthly_payment')]

#+ [html.Label(''), html.Div(id='test')]
        #+[dcc.Graph(id='graph', )]
      #+ [dcc.Graph(id='linebar', figure={go.})]
)

#pdb.set_trace()

@app.callback(
   # Output("table", "data"),
    Output("information", "children"),
  #  Output("first_monthly_payment", "children"),
  #  Output("last_monthly_payment", "children"),
    
   # Output("table", "rows"),
    [Input("mortgageamount", "value"), Input('mip', "value"), Input('limits', "value"),
        Input('repaymentyears', "value") ]
    
)
def cb_render(mortgageamount,mip, repaymentyears, limits):
    print(mortgageamount)
    mip = float(mip)
    mortgageamount = float(mortgageamount)
    repaymentyears = int(float(repaymentyears))
    limits= float(limits)
    if mortgageamount is None or mortgageamount == 0:
        print("It also enters here")
        return 0, 0, 0 
    else:
        df = pandas.DataFrame(interestbounds(mortgageamount, repaymentyears, mip, limits))
        #df.columns = ['principal', 'rprincipal', 'fixedpayment', 
        #                'monthlyinterest', 'monthlypayment']

        print("here we are ")
        return df.iloc[0]
        #return df['monthlyinterest'].sum(), df['monthlypayment'][0], df['monthlypayment'].iloc[-1]



if __name__ == '__main__':
    app.run_server(debug=True)