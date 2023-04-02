import dash
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div([
    html.H1('Data visualization in Python',
            style={'color':'blue'})
])

if __name__ == '__main__':
    app.run_server(port=8002, host='127.0.0.1', debug=True)