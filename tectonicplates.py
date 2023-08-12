import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

volcano_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-12/volcano.csv"
eruptions_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-12/eruptions.csv"

volcano_df = pd.read_csv(volcano_url)
eruptions_df = pd.read_csv(eruptions_url)
tectonic_plates_url = "https://raw.githubusercontent.com/okothchristopher/tidy_tuesday_data_exploration/master/2020_week_20_volcano_erruptions/tectonic_plates_across_the_globe.shp"

tectonic_plates_gdf = gpd.read_file(tectonic_plates_url)

# Plot the tectonic plates
fig, ax = plt.subplots(figsize=(12, 8))
tectonic_plates_gdf.plot(ax=ax, color='gray', linewidth=0.5)

# Plot the volcanoes on top of the tectonic plates
ax.scatter(volcano_df['longitude'], volcano_df['latitude'],
           color='red', marker='^', label='Volcano')

# Plot the eruptions on top of the tectonic plates
ax.scatter(eruptions_df['longitude'], eruptions_df['latitude'],
           color='orange', marker='o', label='Eruption')

# Set the title and legend
ax.set_title('Tectonic Plates and Volcanoes', fontsize=16)
ax.legend()

# Show the plot
plt.show()
