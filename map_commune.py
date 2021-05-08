import pandas as pd


us_cities = pd.read_csv("cas_communess.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="Nom_Commune", hover_data=["Nom_Commune", "Cas communautaires"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":1,"t":1,"l":0,"b":0})


# if __name__ == '__main__':
#     fig.run(host='0.0.0.0')

fig.show()
