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

with Diagram("Docker Diagram", show=False, direction="TB"):

    for i in loadedjson:
      
        
        if i["Mounts"] and 'Name' in (i["Mounts"][0]):
            print("Key (Name) exists in data")
            namevar = str(i["Mounts"][0]["Name"])
        else:
            print("Key (Name) doesn't exist in data")
            namevar = "N/A"

        with Cluster("Name: " + i["Image"]):
            
            with Cluster("IP: " + str(i["Ports"][0]["IP"]) + " | " + "Public Port: " + str(i["Ports"][0]["PublicPort"]) + " | " + "Private Port: " + str(i["Ports"][0]["PrivatePort"])):
                Subcontainer1 = [Custom("Command: \n" + str(i["Command"]) + "\n  " + "\n" + "Volume Name: " + "\n" + namevar,"./Images/docker.png")] 

                
        # print(i["Mounts"])



#  + str(i["Mounts"][0]["Names"]), 







    
 










  

  
    



