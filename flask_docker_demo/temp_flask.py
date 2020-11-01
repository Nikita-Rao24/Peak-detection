# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:33:14 2020

@author: nikita.ramesh.rao
"""

from flask import Flask,request,jsonify
app=Flask(__name__)
app.config["DEBUG"]=True
@app.route('/detect/peak',methods=['POST'])
def detect_peak():
    content=request.json
    file_type=content['file_type']
    file_path=content['file_path']
    response={{'response':'dummy'}}
    return jsonify(response)
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
    
#from flask import Flask 
#app = Flask(__name__) 
#
#@app.route('/') 
#def hello(): 
#	return "welcome to the flask tutorials"
#
#
#if __name__ == "__main__": 
#	app.run(host ='127.0.0.1', port = 5000, debug = True) 
#
## Using flask to make an api 
## import necessary libraries and functions 
#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/')
#def hello_world():
#   return 'Hello World'
#
#if __name__ == '__main__':
#   app.run()


## A simple function to calculate the square of a number 
## the number to be squared is sent in the URL when we use GET 
## on the terminal type: curl http://127.0.0.1:5000 / home / 10 
## this returns 100 (square of 10) 
#@app.route('/home/<int:num>', methods = ['GET']) 
#def disp(num): 
#
#	return jsonify({'data': num**2}) 
#
#
## driver function 
#if __name__ == '__main__': 
#
#	app.run(debug = True) 
