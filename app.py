country_name = input("Digite o nome do país que você deseja destacar no mapa: ")

# Create a new column to indicate the selected country
dataset['selected_country'] = dataset['nome'].apply(lambda x: 1 if x == country_name else 0)

fig = px.choropleth(dataset,
                     locations='iso3',
                     color='selected_country', # Use the new column for color
                     hover_name='nome',
                     color_continuous_scale="Viridis", # Choose a color scale
                     range_color=[0, 1]) # Set the range for the color scale

fig.update_layout(title=f'Mapa destacando {country_name}',
                  geo_scope='world')
fig.show()
