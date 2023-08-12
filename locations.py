import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd


volcano_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-12/volcano.csv"
eruptions_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-12/eruptions.csv"

volcano_df = pd.read_csv(volcano_url)
eruptions_df = pd.read_csv(eruptions_url)
merged_df = eruptions_df.merge(volcano_df, on='volcano_number', how='left')
# Count the number of eruptions for each volcano
volcano_frequency = merged_df['volcano_name'].value_counts()

# Filter the most active volcanoes with at least 5 eruptions since 1800
most_active_volcanoes = volcano_frequency[volcano_frequency >= 5].index.tolist(
)

# Create a new DataFrame with only the most active volcanoes
most_active_df = merged_df[merged_df['volcano_name'].isin(
    most_active_volcanoes)]

# The reference image URL you provided
reference_image_url = "https://pbs.twimg.com/media/EYI4hCuXkAA3CQg?format=jpg&name=medium"

# Load the reference image using matplotlib
img = mpimg.imread(reference_image_url)

# Create a geodataframe from the most_active_df
most_active_gdf = gpd.GeoDataFrame(most_active_df, geometry=gpd.points_from_xy(
    most_active_df['longitude'], most_active_df['latitude']))

# Plot the map
fig, ax = plt.subplots(figsize=(10, 6))

# Show the reference image as the background
ax.imshow(img, extent=[-180, 180, -90, 90])

# Plot the most active volcanoes on top of the reference image
most_active_gdf.plot(ax=ax, color='red', markersize=20,
                     marker='^', label='Most Active Volcanoes')

# Set the title and legend
ax.set_title('Locations of Most Active Volcanoes since 1800', fontsize=16)
ax.legend()

# Show the plot
plt.show()
