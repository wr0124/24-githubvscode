import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots  

##################    Figure 5    #################################
filename5 = 'data_covid.csv'
df_covid = pd.read_csv(filename5)
fig5 = px.scatter(df_covid, y="tx_incid", x="date", title="Taux d'incidence du Covid en France")

# ##################    Figure 6    #################################
filename6 = 'data_creation.csv'
df_creation = pd.read_csv(filename6)
fig6 = make_subplots(specs=[[{"secondary_y": True}]])
for k in range(0,14):
    fig6.add_trace(
        go.Scatter(x=df_creation['Date'], y=df_creation[df_creation.columns[k]], name=df_creation.columns[k]),
        secondary_y=False,
    )
fig6.add_trace(
    go.Scatter(x=df_covid['date'], y=df_covid['tx_incid'], name="Taux incidence"),
    secondary_y=True,
)
fig6.update_xaxes(title_text="Année")
fig6.update_yaxes(title_text="Nombre de créations d'entreprises", secondary_y=False)
fig6.update_yaxes(title_text="Taux d'incidence", secondary_y=True)
fig6.update_layout(
    title_text="Taux d'incidence du Covid-19 & Créations d'entreprises en France entre 2015 et 2023"
)
# ##################    Figure 7    #################################
filename7 = 'data_defaillance.csv'
df_defaillance = pd.read_csv(filename7)
fig7 = make_subplots(specs=[[{"secondary_y": True}]])
for k in range(1,13):
    fig7.add_trace(
        go.Scatter(x=df_defaillance['Date'], y=df_defaillance[df_defaillance.columns[k]], name=df_defaillance.columns[k]),
        secondary_y=False,
    )
fig7.add_trace(
    go.Scatter(x=df_covid['date'], y=df_covid['tx_incid'], name="Taux incidence"),
    secondary_y=True,
)
fig7.update_xaxes(title_text="Année")
fig7.update_yaxes(title_text="Nombre de créations d'entreprises", secondary_y=False)
fig7.update_yaxes(title_text="Taux d'incidence", secondary_y=True)
fig7.update_layout(
    title_text="Taux d'incidence du Covid-19 & Défaillances d'entreprises en France entre 2015 et 2023"
)