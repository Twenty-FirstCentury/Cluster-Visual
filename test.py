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





#defining IP
ipa1 = container1['Ports']
ipb1 = json.dumps(ipa1)
ipc1 = json.loads(ipb1)
ipd1 = ipc1[0]
ip1 = ipd1['IP']

ipa2 = container2['Ports']
ipb2 = json.dumps(ipa2)
ipc2 = json.loads(ipb2)
ipd2 = ipc2[0]
ip2 = ipd2['IP']

ipa3 = container3['Ports']
ipb3 = json.dumps(ipa3)
ipc3 = json.loads(ipb3)
ipd3 = ipc3[0]
ip3 = ipd3['IP']


# #defining public port
# porta1 = container1['Ports']
# portb1 = json.dumps(porta1)
# port1 = portb1["PublicPort"]


#print space
print("Container1 Info:")
print("                          ")
print(container1)
print("                          ")
print("                          ")
print("Name: " + name1)
print("ID: " + id1)
print("Network Name: ")
print("IP: " + ip1)
# print("Public Port: " + port1)
















# @app.route("/")
# def home():
#     return render_template('index.html' )
# if __name__ == '__main__':
#     app.run(debug=True)  


















  

  
    



