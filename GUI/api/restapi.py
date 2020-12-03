from  flask import Flask, jsonify,request
from lexer import  get_token
from sintactico import get_production
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return "Lexer API 1.0"


@app.route('/lex')
def lex():
    string = request.args.get('s')
    return jsonify({'data':get_token(string)})

@app.route('/parse')
def parse():
    string = request.args.get('s')
    print(string)
    res = get_production(string)
    print(res)
    if(len(res)==0):
        return jsonify("Valid Syntax")
    else:
        return jsonify("Invalid Syntax")


if __name__ == '__main__':
    app.run(debug=True)