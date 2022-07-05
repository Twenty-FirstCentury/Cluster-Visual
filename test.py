# Json parser
# variable name, network, ip, port
# docker container ls --format "{{json .}}"

from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
import docker
from docker import client
import json
import sys



client = docker.from_env()

jsondump = json.dumps(client.containers())
loadedjson = json.loads(jsondump)

graph_attr = {

}

with Diagram("Docker Diagram", show=False, direction="TB"):

    for i in loadedjson:

        with Cluster("Name: " + i["Image"]):
            
            with Cluster("IP: " + str(i["Ports"][0]["IP"]) + " | " + "Public Port: " + str(i["Ports"][0]["PublicPort"]) + " | " + "Private Port: " + str(i["Ports"][0]["PrivatePort"]), graph_attr=graph_attr):
                Subcontainer1 = [Custom("Command: \n" + str(i["Command"]) + "\n  " + "\n Mount Source:" + "\n", "./Images/docker.png")] 




            
#  + str(i["Mounts"][0]["Names"]), 







    
 










  

  
    



