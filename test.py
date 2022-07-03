# Json parser
# variable name, network, ip, port
# docker container ls --format "{{json .}}"
import json
from stringprep import in_table_d1
import docker
from docker import client
#from flask import Flask, render_template

#app = Flask(__name__)

client = docker.from_env()

jsondump = json.dumps(client.containers())
loadedjson = json.loads(jsondump)

#defining containers
container1 = loadedjson[0]
container2 = loadedjson[1]
container3 = loadedjson[2]

#defining name
name1 = container1["Image"]
name2 = container2["Image"]
name3 = container3["Image"]

#defining ID
id1 = container1["Id"]
id2 = container2["Id"]
id3 = container3["Id"]


#defining network

#defining ports
fullport1 = container1['Ports']
portdump1 = json.dumps(fullport1)
portloaded1 = json.loads(portdump1)


#print space
print("Names:")
print(name1)
print(name2)
print(name3)
print("")
print("ID:")
print(id1)
print(id2)
print(id3)
















# @app.route("/")
# def home():
#     return render_template('index.html' )
# if __name__ == '__main__':
#     app.run(debug=True)  





  

  
    



