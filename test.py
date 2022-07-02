# Json parser
# variable name, network, ip, port
# docker container ls --format "{{json .}}"
import json
import docker
from docker import client

#from flask import Flask, render_template

#app = Flask(__name__)

client = docker.from_env()

jsondump = json.dumps(client.containers())
y = json.loads(jsondump)

print(y[2])













# @app.route("/")
# def home():
#     return render_template('index.html' )
# if __name__ == '__main__':
#     app.run(debug=True)  




  

  
    



