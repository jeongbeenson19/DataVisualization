from flask import Flask, render_template
from mychart import wchart as wc

app = Flask(__name__)


@app.route('/')
def root_page():
    return 'Hello World!'


@app.route('/radar')
def radar_page():
    return render_template('radar.html')


@app.route('/chart1')
def chart1_page():
    return wc.show_chart1()


@app.route('/map')
def map_page():
    return render_template('map.html')


@app.route('/map1')
def map1_page():
    return wc.show_map1()

@app.route('/starbucks')
def starbucks_page():
    return wc.show_starbucks()


if __name__ == '__main__':
    app.run(debug=True)
