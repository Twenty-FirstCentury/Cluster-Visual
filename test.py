#2022 Summer GTRI ELSYS Internship Project

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

    host = Custom("HOST", "./Images/computer-icon.png")
    web = Custom("The WEB", "./Images/web.png")

    for i in loadedjson:                                       
        
        if i["Mounts"] and 'Name' in (i["Mounts"][0]):                              #Docker Volume Names
            # print("Name: Exists")
            namevar = str(i["Mounts"][0]["Name"])
            namevar2 = (namevar[0:20] + "...")
        else:
            # print("Name: doesn't exist")
            namevar2 = "N/A"
        
        if i["Ports"] and 'IP' in i["Ports"][0]:                                      #Docker IP 
            # print("IP: Exists")
            ipvar = str(i["Ports"][0]["IP"])
        else:
            # print("IP: doesn't exist")
            ipvar = "N/A"

        if i["Ports"] and 'PublicPort' in i["Ports"][0]:                             #Docker Public Port
            # print("PublicPort: Exists")
            publicportvar = str(i["Ports"][0]["PublicPort"])
        else:
            # print("PublicPort: doesn't exist")
            publicportvar = "N/A"
        
        if i["Ports"] and 'PrivatePort' in i["Ports"][0]:                           #Docker Private Port
            # print("PrivatePort: Exists")
            privateportvar = str(i["Ports"][0]["PrivatePort"])
        else:
            # print("PublicPort: doesn't exist")
            privateportvar = "N/A"
        

        with Cluster("Name: " + i["Image"]):
            
            with Cluster("IP: " + ipvar + " | " + "Public Port: " + publicportvar + " | " + "Private Port: " + privateportvar):
                
                Subcontainer1 = [Custom("Command: \n" + str(i["Command"]) + "\n  " + "\n" + "Volume Name: " + "\n" + namevar2 + "...","./Images/docker.png")] 

                
