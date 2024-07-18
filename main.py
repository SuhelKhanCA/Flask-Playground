from flask import Flask

app = Flask(__name__)


def gfg():
    return "Hello Geeks"

app.add_url_rule('/', 'g2g', gfg)


app.run(debug=True)