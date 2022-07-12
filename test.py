from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
import docker
from docker import client
import json
import sys
import textwrap


client = docker.from_env()

jsondump = json.dumps(client.containers())
loadedjson = json.loads(jsondump)

with Diagram("Docker Diagram", show=False, direction="TB"):

    for i in loadedjson:                                           #Docker Volume Names
        
        if i["Mounts"] and 'Name' in (i["Mounts"][0]):
            print("Name: Exists")
            namevar = str(i["Mounts"][0]["Name"])
            namevar2 = (namevar[0:20] + "...")
        else:
            print("Name: Doesn't Exist")
            namevar2 = "N/A"

        if i["Ports"] and 'PublicPort' in (i["Ports"][0]):         #Docker IP
            print("IP: Exists")
            ipvar = (i["Ports"][0]["IP"])
        else: 
            print("IP: Doesn't Exist")
            ipvar = "ERROR"

        with Cluster("Name: " + i["Image"]):  
            with Cluster("IP: " + ipvar + " | " + "Public Port: " + str(i["Ports"][0]["PublicPort"]) + " | " + "Private Port: " + str(i["Ports"][0]["PrivatePort"])):
                Subcontainer1 = [Custom("Command: \n" + str(i["Command"]) + "\n  " + "\n" + "Volume Name: " + "\n" + namevar2 + "...","./Images/docker.png")] 


    
 










  

  
    



