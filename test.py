# Json parser
# variable name, network, ip, port
# docker container ls --format "{{json .}}"

import json
import docker
from docker import client
#from flask import Flask, render_template

#app = Flask(__name__)

client = docker.from_env()

for container in client.containers():
    
    # for key, value in container.items():
    #     print(key, ':', value)
    #     print("")

    data = (container)
    final = json.dumps(data)
    
    # print(final)
    print("")

    y = json.loads(final)
    print(y["Image"])
 


    



 








# @app.route("/")
# def home():
#     return render_template('index.html' )
# if __name__ == '__main__':
#     app.run(debug=True)  
















    
 










  

  
    



