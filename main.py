from werkzeug.wrappers import request,response
from flask import Flask,request,jsonify
from key import Keyword_Spotting_Service
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route('/api',methods=['GET'])
def Prediction():
     path = request.files['path']
     kss = Keyword_Spotting_Service()
     keyword1,keyword2= kss.prediction(path)
     return {'prediction':keyword1}
 
@app.route('/api1',methods=['GET'])
def Value():
     path = request.files['path']
     kss = Keyword_Spotting_Service()
     keyword1,keyword2= kss.prediction(path)
     return {'prediction':keyword2}


if __name__ == "__main__":
    app.run(debug=True,use_reloader = False)
    
    
    