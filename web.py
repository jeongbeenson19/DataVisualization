from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root_page():
    return 'Hello World!'


@app.route('/radar')
def radar_page():
    return render_template('radar.html')


if __name__ == '__main__':
    app.run(debug=True)
