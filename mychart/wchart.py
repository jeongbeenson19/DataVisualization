from flask import Flask, render_template, url_for
import random
import folium
from folium.plugins import MarkerCluster as MC
import pandas as pd
import json


def show_chart1():
    xval = ["{:02d}".format(i) for i in range(1, 11)]
    yval = ['a', 'b', 'c', 'd']
    my_list = []
    for i in range(len(yval)):
        for j in range(len(xval)):
            my_list.append([i, j, round(1000*random.random())])
    data = {"my_list": my_list, "x": xval, "y": yval}

    return render_template('chart1.html', data=data)


def show_map1():
    map = folium.Map(location=[37.2261933, 127.1681805], zoom_start=16)
    folium.Marker(location=[37.2261933, 127.1681805], popup=folium.Popup("용인대학교 AI융합대학", max_width=300)).add_to(map)

    return map.get_root().render()


def show_starbucks():
    sd = pd.read_csv('static/starbucks.csv', delimiter='|', encoding='utf-8')
    sido = json.load(open('static/sido.json', encoding='utf-8'))
    sd = pd.DataFrame(sd)
    map = folium.Map(location=[35.95, 128.25], zoom_start=7)
    folium.GeoJson(sido).add_to(map)
    mc = MC().add_to(map)
    for i, r in sd.iterrows():
        nm = r['Store_nm']
        ad = r['Address']
        te = r['Telephone']
        ca = str(r['Category'])
        lo = r['Ycoordinate']
        la = r['Xcoordinate']
        ps = f'<b>{nm}</b><br>주소:{ad}<br>전화:{te}<br><i>{"" if ca=="nan" else ca}</i>'
        mk = folium.Marker(location=[lo, la], popup=folium.Popup(f"{ps}", max_width=400))
        mk.add_to(mc)

    return map.get_root().render()
