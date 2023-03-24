from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from layouts import layout1, layout2, layout3,layout4, layout5
import callbacks

# version en cours

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server
colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'fontSize': 30 
}

app.layout = dbc.Container([
     dcc.Location(id='url', refresh=True),
     html.H1('Projet Blanc Groupe 1 : Rida, Ryad, Julie et Aliyasin'),
     html.Div(children=[dcc.Link('Go to Page 1', href='/page1')], style={'textAlign': 'center', 'color': colors['text'], 'fontSize':colors['fontSize']}),
     html.Div(children=[dcc.Link('Go to Page 2', href='/page2')], style={'textAlign': 'center', 'color': colors['text'], 'fontSize':colors['fontSize']}),
     html.Div(children=[dcc.Link('Indicateurs économiques', href='/Indicateurs-divers')], style={'textAlign': 'center', 'color': colors['text'], 'fontSize':colors['fontSize']}),
     html.Div(children=[dcc.Link('Chômage', href='/chomage')], style={'textAlign': 'center', 'color': colors['text'], 'fontSize':colors['fontSize']}),
     html.Div(children=[dcc.Link('Entreprises de France', href='/Entreprises')], style={'textAlign': 'center', 'color': colors['text'], 'fontSize':colors['fontSize']}),
     html.Div(id='page-content')
])
@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))


# dcc.Link('Go to Page 2', href='/page2', style={'display': 'block'}) 



def display_page(pathname):
    if pathname == '/page1':
         return layout1
    elif pathname == '/page2':
         return layout2
    elif pathname == '/Indicateurs-divers':
         return layout3
    elif pathname == '/chomage':
         return layout4
    elif pathname == '/Entreprises':
         return layout5
    else:
        return html.Div([html.H1('Projet Blanc Groupe 1 : Rida, Ryad, Ru et Aliyasin') ], style={'width': '4000px', 'height': '100px','font-size': '38px'})

if __name__ == '__main__':
    app.run_server(debug=True)

 #html.Div('Projet Blanc Groupe 1 : Rida, Ryad, Julie et Aliyasin ', style={'font-size': '28px'})
#html.H1('Projet Blanc Groupe 1 : Rida, Ryad, Julie et Aliyasin ', style={'font-size': '48px','text_align': 'center'}) 'width': '4000px', 'height': '10000px',