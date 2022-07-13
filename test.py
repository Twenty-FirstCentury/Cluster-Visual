from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
import docker
from docker import client
import json
import sys
import textwrap


client = docker.from_env()
network_list={}
for net in client.networks():
    network_list[net['Name']]=1

jsondump = json.dumps(client.containers())
loadedjson = json.loads(jsondump)
print(jsondump)

graph_attr = {

    "shape": "ellipse",

    "fontsize": "150",

    "splines": "spline",

    "nodesep": "5",
    "ranksep": "10",

    "dpi": "250",

}

for net in network_list.keys():


    with Diagram("\n \n \n \n \n \n" "Docker Container Diagram", show=False, direction="TB", graph_attr=graph_attr, outformat="jpg"):

        host = Custom("HOST", "./Images/computer-icon.png")
        web = Custom("WEB", "./Images/web.png")

        for i in loadedjson:                                       
            
            if i["Mounts"] and 'Name' in (i["Mounts"][0]):                              #Docker Volume Names
                # print("Name: Exists")
                namevar = str(i["Mounts"][0]["Name"])
                namevar2 = (namevar[0:40] + "...")
            else:
                # print("Name: doesn't exist")
                namevar2 = "                              N/A                              "
            
            if i["Ports"] and 'IP' in i["Ports"][0]:                                      #Docker IP 
                # print("IP: Exists")
                ipvar = str(i["Ports"][0]["IP"])
            else:
                # print("IP: doesn't exist")
                ipvar = "N/A"

            if i['HostConfig']['NetworkMode']:
                netvar = i["HostConfig"]["NetworkMode"]
                

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
                    # if ipvar == 'N/A':
                    if netvar == net:
                        Subcontainer0 = [Custom("IP: " + ipvar + netvar +  " \n " + "Public Port: " + publicportvar + "\n" + "Private Port: " + privateportvar, "./Images/docker.png")] 

                        Subcontainer0 - host

                    # else:
                    #     Subcontainer1 = [Custom("IP: " + ipvar + netvar +  " \n " + "Public Port: " + publicportvar + "\n" + "Private Port: " + privateportvar, "./Images/docker.png")] 
                        






    # "HostConfig": {
    #   "NetworkMode": "apache_default"
    # },
            



