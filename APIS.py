from flask import Flask,request,jsonify,render_template

import json
with open("E:/python sql/json.json") as f:
    data = json.load(f)
app = Flask(__name__)
@app.route('/',methods=['GET'])
def GET ():
    return render_template("get.html",json=data)
@app.route('/post_json', methods=['POST'])
def post():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

if __name__=='__main__':
    app.run(debug=True,port=3000)

