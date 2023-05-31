# -*- coding: utf-8 -*-
"""
@author: Achilleas Karagiannidis
"""
# import needed libraries to create the map with the pointers
import matplotlib.pyplot as plt
import contextily as ctx
import pandas as pd


# Function to create the map, and appoint the pointers on it.
def poisOnMap(poiNum, x, y):
    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(10,10))

    # Set the limits to cover the POIs
    ax.set_xlim(min(x)-0.001, max(x)+0.001)
    ax.set_ylim(min(y)-0.001, max(y)+0.001)

    # Add the OpenStreetMap base map
    ctx.add_basemap(ax, crs='epsg:4326', source=ctx.providers.OpenStreetMap.Mapnik)

    # Add a marker for each POI
    for i in range(len(poiNum)):
        ax.plot(x[i], y[i], 'ro', markersize=10, label=f'POI {poiNum[i]}')
       
    ax.legend()
    plt.show()

# Read data from the XLSX file
data = pd.read_excel('TELIKO.xlsx')
#print(data)


# Extract columns from the data
poiNum = data['poinnum'].tolist()
x = data['x'].tolist()
y = data['y'].tolist()

# Call the function with the updated data
poisOnMap(poiNum, x, y)