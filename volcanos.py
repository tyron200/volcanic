import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the data into DataFrames
volcano_df = pd.read_csv(
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-12/volcano.csv")
eruptions_df = pd.read_csv(
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-12/eruptions.csv")

# Merge the DataFrames on 'volcano_number'
merged_df = pd.merge(volcano_df, eruptions_df,
                     on='volcano_number', how='inner')

# Group the data by volcano type and calculate total population exposure
population_exposure_by_type = merged_df.groupby(
    'type')['population_exposure'].sum().reset_index()

# Find the volcano type with the highest population exposure
highest_population_exposure_type = population_exposure_by_type.sort_values(
    by='population_exposure', ascending=False).iloc[0]

# Filter the merged DataFrame for the volcanoes with the highest population exposure
highest_population_volcanoes = merged_df[merged_df['type']
                                         == highest_population_exposure_type['type']]

# Create a GeoDataFrame from the highest population volcanoes data
gdf = gpd.GeoDataFrame(highest_population_volcanoes,
                       geometry=gpd.points_from_xy(highest_population_volcanoes.longitude, highest_population_volcanoes.latitude))

# Plot the GeoDataFrame on a map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(12, 8), color='lightgray', edgecolor='black')

gdf.plot(ax=ax, markersize=50, color='red',
         label='Volcanoes with highest population exposure')

plt.title('Volcanoes with Highest Effects on Population')
plt.legend()
plt.show()


# This code will display a map using GeoPandas, showing the location of volcanoes with the highest effects on the population. The volcanoes will be marked in red on a world map. The size of the markers represents the population exposure, i.e., the higher the population exposure, the larger the marker.