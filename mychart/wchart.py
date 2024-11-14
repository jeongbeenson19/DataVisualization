from flask import Flask, render_template, url_for
import random
import folium


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