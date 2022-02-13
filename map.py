# folium - interactive maps with python
# Choropleth Map
# 
import folium

# create a basemap
risk_map = folium.Map(location=[50, -95], zoom_start=4)

# show the map
risk_map.save("test_map.html")