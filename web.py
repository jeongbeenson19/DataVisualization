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


if __name__ == '__main__':
    app.run(debug=True)
