from flask import Flask,request

app =Flask(__name__)

@app.route('/',methods=['get','post'])
def index():
    return "<h1>This is flask application </h1>"


if __name__ =="__main__":
    app.run()