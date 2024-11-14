from flask import Flask, render_template, url_for
import random


def show_chart1():
    xval = ["{:02d}".format(i) for i in range(1, 11)]
    yval = ['a', 'b', 'c', 'd']
    my_list = []
    for i in range(len(yval)):
        for j in range(len(xval)):
            my_list.append([i, j, round(1000*random.random())])
    data = {"my_list": my_list, "x": xval, "y": yval}

    return render_template('chart1.html', data=data)
