from dash import html
import plotly.graph_objects as go
from dash import dcc
import plotly.express as px
import pandas as pd
import dash


dt_worldwide = pd.read_csv("dt_world.csv")

affiche_map_1 = px.scatter_mapbox(
    dt_worldwide, lat="Lat", lon="Long", hover_name="Country",
    hover_data=["Country", "Date", "Confirmed", "Recovered", "Deaths", "Active"],
    color="Confirmed", size="Confirmed", zoom=2, height=800, color_continuous_scale=px.colors.sequential.Magma,
    title="Présence de cas confirmés de COVID-19 dans différentes parties du monde")

affiche_map_1.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {"below": 'traces', "sourcetype": "raster", "sourceattribution": "Présence de cas confirmés de COVID-19 dans différentes parties du monde",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ],
    title_x=0.5,
    title_y=0.95,
    titlefont={ "size": 35, "color": '#1C2840'}
      )
affiche_map_1.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 50})

# Deuxieme carte pour afficher les cas de mort dans le monde 
affiche_map_2 = px.scatter_mapbox(dt_worldwide, lat="Lat", lon="Long", hover_name="Country",
                        hover_data=["Country", "Date", "Deaths"],
                        color_discrete_sequence=["red"],
                        zoom=2,
                        height=800,
                        title="Nombre de décès dus au COVID-19 par région du monde")
affiche_map_2.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "Nombre de décès dus au COVID-19 par région du monde",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ],
    title_x=0.5,
    title_y=0.98,
    titlefont={ "size": 35, "color":'#1C2840' }

      )
affiche_map_2.update_layout(margin={"l": 0, "r": 0, "b": 0, "t": 50})

# Affichage des graphiques 
# On crée graphe en fromage

# Pour faire le % il est important d'avoir zero données nulles
confirm = dt_worldwide.loc[dt_worldwide['Confirmed'] > 0].count()[0]
dead = dt_worldwide.loc[dt_worldwide['Deaths'] > 0].count()[0]
recov = dt_worldwide.loc[dt_worldwide['Recovered'] > 0].count()[0]
active = dt_worldwide.loc[dt_worldwide['Active'] > 0].count()[0]

# On stock 3 cas qui nous interesse, colorée

labels = ['Décédé', 'Soigné', 'Actif']
values = [dead,recov,active]
colors = ['#E83845', '#CCFF33', '#FF9999']

#On affiche le graphique frommage

graph_fromage = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    textinfo='label+percent',
    marker_colors=colors,
    hole=.1,
    insidetextorientation='radial',textfont_size=25
    )])

#Ajout d'une couleur de fond au graphique, taille, titre
graph_fromage.layout.paper_bgcolor = '#FFFFCC'
graph_fromage.update_layout(title_text="Distribution des types de cas confirmés", titlefont={ "size": 35, "color":"#FFFFFF" },hoverlabel={"bgcolor":"white","font_size":30,"font_family":"Rockwell"})

#On affiche l'histogramme avec les cas confirmés en fonction de la date

graph1 = px.histogram(
    dt_worldwide,
    x="Date",
    y="Confirmed",
    color="Country",
    title='Analyse de la progression des cas confirmés au fil du temps',
    template='plotly_dark')
graph1.update_layout(titlefont={ "size": 25 })

#On affiche l'histogramme avec morts confirmés en fonction de la date

graph2 = px.histogram(
    dt_worldwide,
    x="Date",
    y="Deaths",
    color="Country",
    title='Analyse de la progression des cas décédés au fil du temps',
    template='plotly_dark')
graph2.update_layout(titlefont={ "size": 25 })

#On affiche du graphique représentant le nombre de cas confirmé par pays

graph3 = px.scatter(
    dt_worldwide,
    x="Country",
    y="Confirmed",
    color="Country",
    title="Nombre de cas confirmé par pays",
    template='plotly_dark')
graph3.update_layout(titlefont={ "size": 25 })

#On affiche du graphique représentant le nombre de morts par pays

graph4 = px.scatter(
    dt_worldwide,
    x="Country",
    y="Deaths",
    title='Données sur les cas décès par pays',
    template='plotly_dark',
    color="Country")
graph4.update_layout(titlefont={ "size": 25 })

#On affiche du graphique représentant le nombre de cas confirmé par pays en fonction du temps

graph5 = px.scatter(
    dt_worldwide,
    x="Date",
    y="Confirmed",
    color="Country",
    title='Suivi de l\'évolution des cas confirmés par pays au fil du temps',template='plotly_dark')
graph5.update_layout(titlefont={ "size": 25 })

#On affiche du graphique représentant le nombre de morts par pays en fonction du temps

graph6 = px.scatter(
    dt_worldwide, 
    x="Date", y="Deaths",
    color="Country",
    title="Suivi de l\'évolution des cas décès par pays au fil du temps",template='plotly_dark')
graph6.update_layout(titlefont={ "size": 25 })

#On affiche du graphique représentant l'évolution du nombre de morts par pays dans le temps

graph7 = px.bar(
    dt_worldwide,
    x="Country",
    y="Confirmed",
    title='Suivi de l\'évolution des décès par pays au cours de la période considérée',
    animation_group="Country",
    animation_frame="Date",
    range_y=[0,14000000],
    height=800,template='plotly_dark')
graph7.update_layout(titlefont={ "size": 25 })

graph7.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 5
graph7.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

#On affiche du graphique représentant le nombre de morts en fonction des cas confirmés

graph8 = px.histogram(
    dt_worldwide,
    x="Confirmed",
    y="Deaths",
    color="Country",
    title='Corrélation entre le nombre de décès et de cas confirmés',
    template='plotly_dark')
graph8.update_layout(titlefont={ "size": 22 })



# Debut de Dashboard

app = dash.Dash(__name__) # Créer le dashboard
# Création d'une page HTML
app.layout = html.Div(style={'background-color':'#FFFF'},children=[
                        html.H1("Evolution de COVID-19 dans le monde",
                        style={'text-align': 'center', 'color':'black', 'padding-top':'2vh','padding-bottom':'2vh'}),
                        html.Br(),
                        #Affichage dans dashboard des traitements d'en haut
                        #On affiche graphique avec évolution du nombre de morts par pays dans le t
                        dcc.Graph(id='graph7', figure=graph7),
                        #On affiche la carte des cas confirmés dans le monde
                        dcc.Graph(id='affiche_map_1',figure=affiche_map_1),
                        #On affiche carte des cas morts dans le monde
                        dcc.Graph(id='affiche_map_2',figure=affiche_map_2),
                        #On affiche l'histogramme avec cas confirmés en fonction de la date
                        dcc.Graph(id='graph1',figure=graph1),


                        #On affiche le graphique avec le nombre de cas confirmé par pays
                        dcc.Graph(id='graph3',figure=graph3),
                        #On affiche graphique avec le nombre de morts par pays
                        dcc.Graph(id='graph4',figure=graph4),

                        #On affiche frommage
                        dcc.Graph(id='graph_fromage', figure=graph_fromage,style={'height': '90vh', 'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'}),

                        #On affiche de l'histogramme avec les morts avec covid confirmés en fonction de la date
                        dcc.Graph(id='graph2',figure=graph2),
                        #On affiche le graphique qui montre le nombre de cas confirmé par pays en fonction du temps
                        dcc.Graph(id='graph5',figure=graph5),
                        #On affiche le graphique avec nombre de morts par pays en fonction du t
                        dcc.Graph(id='graph6',figure=graph6),
                        #On affiche graphique avec le nombre de morts en fonction des cas confirmés
                        dcc.Graph(id='graph8',figure=graph8),
])


#########################################################################################################################################################################################################################################

# Lancement le Dashboard

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
