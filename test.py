#2022 Summer GTRI ELSYS Internship Project by Urim Suh && Kenan Orlovic


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


graph_attr = {

    "shape": "ellipse",

    "fontsize": "150",

    "splines": "spline",

    "nodesep": "4",
    "ranksep": "10",

    "fixedsize": "true",
    "width": "20in",

    "dpi": "250",

}


with Diagram("\n \n \n \n \n \n" "Docker Container Diagram", show=False, direction="TB", graph_attr=graph_attr, outformat="jpg"):

    host = Custom("Host", "./Images/computer-icon.png")
    web = Custom("WEB", "./Images/web.png")

    for i in loadedjson:                                       
        
        if i["Mounts"] and 'Name' in (i["Mounts"][0]):                              #Docker Volume Names
            # print("Name: Exists")
            namevar = str(i["Mounts"][0]["Name"])
            namevar2 = (namevar[0:30] + "...")
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
            
            with Cluster("Command: \n" + str(i["Command"]) + "\n" + "\n" + "Volume Name: " + "\n" + namevar2):
                
                Subcontainer1 = [Custom("IP: " + ipvar + " \n " + "Public Port: " + publicportvar + "\n" + "Private Port: " + privateportvar, "./Images/docker.png")] 

                web >> Subcontainer1 >> host

                host >> Subcontainer1 
                Subcontainer1 >> web


