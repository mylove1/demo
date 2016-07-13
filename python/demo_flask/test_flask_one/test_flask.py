# coding:utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <body>
    <button type="button" onclick="alert('欢迎!')">点我!</button>
    </body>
    </html>

    """

app.run(debug=True)

