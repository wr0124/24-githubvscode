from dash import dcc, html, Dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots  
import os
import dash_bootstrap_components as dbc
from Figures_Aliyasin import *

# version en cours
colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'fontSize': 30 
}

#####page3#####page3#####page3#####page3#####page3#####page3#####page3
##################    Figure 1    #################################
merge_year = pd.read_csv("./GDP_3rate.csv")
gdp = go.Scatter(x=merge_year['year'], y=merge_year['GDPPerCapiGrowth'], name="GDPPerCapiGrowthRate")
purcha = go.Scatter(x=merge_year['year'], y=merge_year['purchas'], name="Purchasing power rate")
save = go.Scatter(x=merge_year['year'], y=merge_year['saving'], name="Saving rate")
inflation = go.Scatter(x=merge_year['year'], y=merge_year['Infla_rate'], name="Inflation rate")

# define the layout
layout = go.Layout(title='Economic index rate evolution', xaxis=dict(title='year'), yaxis=dict(title='rate'))

# create the figure
fig1 = go.Figure(data=[gdp, purcha, save, inflation], layout=layout)

##################    Figure 2    #################################
#####fig2 correction
filename2 = 'GDP_3rate_corr.csv'
corGDP4 = pd.read_csv(filename2)
fig2 = go.Figure()
fig2.add_trace(
    go.Heatmap(
        x = corGDP4.columns,
        y = corGDP4.index,
        z = np.array(corGDP4),
        text=corGDP4.values,
        texttemplate='%{text:.2f}'
    )
)

  
#fig2=px.imshow(corGDP4)
fig2.update_layout(  title='pearson standard correlation coefficient between Annual growth rate of real GDP per capita, purchasing power, saving rate and inflation rate'  )
######ENdendendpage3#####page3#####page3#####page3#####page3#####page3#####page3



##################    Figure 3    #################################

filename3 = 'HFCS_unployment.csv'
#####page4#####page4#####page4#####page4#####page4#####page4#####page4#####page4#####page4#####page4
final_df = pd.read_csv(filename3)

HFCS = go.Scatter(x=final_df['YM'], y=final_df['HFCS'], name="HFCS of France")
Femunploy= go.Scatter(x=final_df['YM'], y=final_df['Femmes'], name="unployment female")
Malunploy= go.Scatter(x=final_df['YM'], y=final_df['Hommes'], name="unployment male")
 
# define the layout
layout = go.Layout(title='Evolution of Rescaled HFCS and unployment rate in France', xaxis=dict(title='year'), yaxis=dict(title='Rescaled values'))

# create the figure
fig3 = go.Figure(data=[HFCS, Femunploy,Malunploy], layout=layout)

##################    Figure 4    #################################
filename4 = 'HFCS_unployment_corr.csv'
corHFCSUnployment = pd.read_csv(filename4)
fig4 = go.Figure()
fig4.add_trace(
    go.Heatmap(
        x = corHFCSUnployment.columns,
        y = corHFCSUnployment.index,
        z = np.array(corHFCSUnployment),
        text=corHFCSUnployment.values,
        texttemplate='%{text:.2f}'
    )
)
fig4.update_layout(  title='Pearson standard correlation coefficient between unployment by gendre and HFCS'  )


#####ENdendendpage4#####page4#####page4#####page4#####page4#####page4#####page4#####page4#####page4#####page4#####page4





layout1 = html.Div([
    html.H3('Page 1'),
    dcc.Graph(id='page-1-display-value')
])

layout2 = html.Div([
    html.H3('Page 2'),
    dcc.Graph(id='page-2-display-value')
    #html.Div(id='page-2-display-value')
])

layout3= html.Div([ 
    html.H3('Page 3'),


    html.Div(children=[ html.Span('GDPPerCapiGrowthRate', style={'color': 'black','font-size': '16px'}),
    ''': Annual growth rate of real Gross Domestic Product (GDP) per capita is calculated as the percentage change in the real GDP per capita between two consecutive years. Real GDP per capita is calculated by dividing GDP at constant prices by the population of a country or area.
    '''
    ] ,style={'font-size': '12px', 'font-family': 'Arial','margin-bottom': '20px'}),

    html.Div(children=[ html.Span('Purchasing power rate', style={'color': 'black','font-size': '16px'}),
    ''': The Purchasing Power of Gross Disposable Income refers to the amount of goods and services that can be purchased with an individual or household's after-tax income. Gross Disposable Income (GDI) is the amount of income that an individual or household has available for spending or saving after taxes have been paid. The Purchasing Power of GDI takes into account the cost of living, inflation, and other factors that affect the real value of income.
    '''
    ] ,style={'font-size': '12px', 'font-family': 'Arial','margin-bottom': '20px'}),


    html.Div(children=[ html.Span('Saving rate', style={'color': 'black','font-size': '16px'}),
    ''': Annual growth rate of real Gross Domestic Product (GDP) per capita is calculated as the percentage change in the real GDP per capita between two consecutive years. Real GDP per capita is calculated by dividing GDP at constant prices by the population of a country or area.
    '''
    ] ,style={'font-size': '12px', 'font-family': 'Arial','margin-bottom': '20px'}),

    html.Div(children=[ html.Span('Inflation rate', style={'color': 'black','font-size': '16px'}),
    ''': Financial savings in household saving refers to the portion of household income that is saved or invested in financial assets, such as savings accounts, stocks, bonds, mutual funds, and other financial instruments. It is the difference between disposable income (income after taxes) and consumption expenditure (spending on goods and services).
    '''
    ] ,style={'font-size': '12px', 'font-family': 'Arial','margin-bottom': '20px'}),

    dcc.Graph(
        id='example-graph-1',
        figure=fig1
    ),

    html.Div(children='''
         The correlation heatmap
    '''),

    dcc.Graph(
        figure=fig2,
        id='page-3-display-value'
    ),

    html.Div(children=[ html.Span('Summary', style={'color': 'black','font-size': '20px'}),
    ''': GDP Per Captical Growth rate can be partely explained by saving rate and purchasing power according to the correlation coefficient, while the inflation rate is more correlated with saving rate than other two rates. During the covid year(2020), the GDPPperCapiGrowthRate and saving rate reache double changement.
    '''
    ] ,style={'font-size': '16px', 'font-family': 'Arial','margin-bottom': '20px'})

])

layout4= html.Div([ 
    html.H3('Page 4'),

    html.Div(children=[ html.Span('Household Finance and Consumption Survey(HFCS)', style={'color': 'black','font-size': '16px'}),
    ''': consumer confidence indicator provides an indication of future developments of households’ consumption and saving, based upon answers regarding their expected financial situation, their sentiment about the general economic situation, unemployment and capability of savings. An indicator above 100 signals a boost in the consumers’ confidence towards the future economic situation, as a consequence of which they are less prone to save, and more inclined to spend money on major purchases in the next 12 months. Values below 100 indicate a pessimistic attitude towards future developments in the economy, possibly resulting in a tendency to save more and consume less. 
    '''
    ] ,style={'font-size': '12px', 'font-family': 'Arial','margin-bottom': '20px'}),

    html.Div(children=[ html.Span('Unployment rate', style={'color': 'black','font-size': '16px'}),
    ''': The unemployment rate is the percentage of unemployed people in the labour force (occupied labour force + the unemployed).
    '''
    ] ,style={'font-size': '12px', 'font-family': 'Arial','margin-bottom': '20px'}),

    dcc.Graph(
        id='example-graph',
        figure=fig3
    ),

    html.Div(children='''
        The correlation heatmap
    '''),

    dcc.Graph(
        figure=fig4,
        id='page-4-display-value'
    ),
    
    html.Div(children=[ html.Span('Summary', style={'color': 'black','font-size': '20px'}),
    ''': HFCS and unployment are colsely related according to the correlation matrix. Both HFCS and unployment have the tendency after the covid year(2000)
    '''
    ] ,style={'font-size': '16px', 'font-family': 'Arial','margin-bottom': '20px'})
])





layout5= html.Div([ 
    html.H3('Impact de la crise sanitaire de 2020 sur les entreprises en France'),

    html.Div(children='''
        Blabla, Blabla, Blabla, création des entreprises.
    '''),
    dcc.Graph(
        figure=fig5
    ),
    dbc.Tabs(
            [
                dbc.Tab(label="Créations", tab_id="creation"),
                dbc.Tab(label="Défaillances", tab_id="defaillance"),
            ],
            id="tabs",
            active_tab="creation",
    ),
    dcc.Graph(
        id="tab-content"
    )         
,
])
