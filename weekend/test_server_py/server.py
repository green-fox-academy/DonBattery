from flask import Flask
import os

app = Flask(__name__, static_url_path='/static')

print('Instance Path :', app.instance_path)
print('Root Path :', app.root_path)
print('Static URL Path :', app.static_url_path)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/script.js')
def script():
    return app.send_static_file('script.js')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route("/jiff")
def foo():
    foo = "bar"
    return "foo = " + foo

if __name__ == "__main__":
    app.run(port=801)