import folium


map = folium.Map(location=[37.2261933, 127.1681805], zoom_start=16)
folium.Marker(location=[37.2261933, 127.1681805], popup=folium.Popup("용인대학교 AI융합대학", max_width=300)).add_to(map)

map.save("templates/map.html")

