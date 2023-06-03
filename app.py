from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "HiHi"


@app.route('/gettest', methods=['GET'])
def get_test():
    string = request.args.get('string')
    return "您輸入的是：" + string
