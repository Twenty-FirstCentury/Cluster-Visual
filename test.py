# Json parser
# variable name, network, ip, port
# docker container ls --format "{{json .}}"

from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
import docker
from docker import client
import json
from itertools import count
import sys



#from flask import Flask, render_template

#app = Flask(__name__)

client = docker.from_env()

jsondump = json.dumps(client.containers())
loadedjson = json.loads(jsondump)

ipa1 = loadedjson['Ports']
ipb1 = json.dumps(ipa1)
ipc1 = json.loads(ipb1)
ipd1 = ipc1[0]
ip1 = ipd1['IP']


with Diagram("Docker Diagram", show=False):

    for i in loadedjson:
        with Cluster("Name: " + i["Image"]):
            
            with Cluster("Subcontainer 1 (port: 3000)"):
                Subcontainer1 = [Custom("Node JS", "./Images/docker.png")] 
    
    print("done!")
            
  
print(ip1) 
        

        











# #defining containers
# container1 = loadedjson[0]
# container2 = loadedjson[1]
# container3 = loadedjson[2]


# #defining name
# name1 = container1["Image"]
# name2 = container2["Image"]
# name3 = container3["Image"]


# #defining ID
# id1 = container1["Id"]
# id2 = container2["Id"]
# id3 = container3["Id"]


# #defining network name





# #defining IP
# ipa1 = container1['Ports']
# ipb1 = json.dumps(ipa1)
# ipc1 = json.loads(ipb1)
# ipd1 = ipc1[0]
# ip1 = ipd1['IP']

# ipa2 = container2['Ports']
# ipb2 = json.dumps(ipa2)
# ipc2 = json.loads(ipb2)
# ipd2 = ipc2[0]
# ip2 = ipd2['IP']

# ipa3 = container3['Ports']
# ipb3 = json.dumps(ipa3)
# ipc3 = json.loads(ipb3)
# ipd3 = ipc3[0]
# ip3 = ipd3['IP']


# #defining public port




# #print space
# print("Container 1 Info:")
# print("                          ")
# print("Name: " + name1)
# print("ID: " + id1)
# print("Network Name: ")
# print("IP: " + ip1)

# print("                          ")
# print("                          ")
# print("Container 2 Info:")
# print("                          ")
# print("Name: " + name2)
# print("ID: " + id2)
# print("Network Name: ")
# print("IP: " + ip2)

# print("                          ")
# print("                          ")
# print("Container 3 Info:")
# print("                          ")
# print("Name: " + name3)
# print("ID: " + id3)
# print("Network Name: ")
# print("IP: " + ip3)

















# @app.route("/")
# def home():
#     return render_template('index.html' )
# if __name__ == '__main__':
#     app.run(debug=True)  














    
 










  

  
    



