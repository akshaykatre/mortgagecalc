import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc



app = dash.Dash(__name__)

PAGE_SIZE = 5

app.layout = html.Div(children=[html.Div(id='test')]+[dcc.Input(id='datatable-paging')])

@app.callback(
    Output('test', 'children'),
    Input('datatable-paging', "page_current")
 #   Input('datatable-paging', "page_size"))
    )
def update_table(page_current,page_size):
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

    df[' index'] = range(1, len(df) + 1)

    print(df)
    return dash_table.DataTable(
    id='test',
    data = df.iloc[:].to_dict('records'),
    page_current=0,
    page_size=PAGE_SIZE,
    page_action='custom'
)


if __name__ == '__main__':
    app.run_server(debug=True)