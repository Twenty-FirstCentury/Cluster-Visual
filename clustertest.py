import json
#from flask import Flask, render_template
import docker
from docker import client

#app = Flask(__name__)
client = docker.from_env()
for i in client.containers():
    #print(i)
    for key, value in i.items():
        print(key, '::::::::::::::::::::::::::::::', value)
        print(" ")
        
# for container_id in client.containers.list():
#     #print(container_id.attrs)
#     for x, y in container_id.items():
#         print(x, y)
#         #z=json.loads(container_id.attrs)
    
# l = '{"CreatedAt":"2022-06-29 11:33:55 -0400 EDT","ID":"urim","Image":"apache_php-apache-environment","LocalVolumes":"0","Names":"php-apache","Networks":"apache_default","Ports":"0.0.0.0:8000-\u003e80/tcp","RunningFor":"25 hours ago","Size":"2B (virtual 480MB)","State":"running","Status":"Up 4 hours"}'
# z = json.loads(l)

# a = '{"CreatedAt":"2022-06-29 11:33:55 -0400 EDT","ID":"testingid2","Image":"joe","LocalVolumes":"0","Names":"php-apache","Networks":"apache_default","Ports":"0.0.0.0:8000-\u003e80/tcp","RunningFor":"22 hours ago","Size":"2B (virtual 480MB)","State":"running","Status":"Up About an hour"}'
# b = json.loads(a)

# c = '{"CreatedAt":"2022-06-29 11:33:55 -0400 EDT","ID":"testing3","Image":"rye","LocalVolumes":"0","Names":"php-apache","Networks":"apache_default","Ports":"0.0.0.0:8000-\u003e80/tcp","RunningFor":"22 hours ago","Size":"2B (virtual 480MB)","State":"running","Status":"Up About an hour"}'
# d = json.loads(c)


#name1 = (z["Image"])
# name2 = (b["Image"])
# name3 = (d["Image"])

# network1 = (z["Networks"])
# network2 = (b["Networks"])
# network3 = (d["Networks"])

# id1 = (z["ID"])
# id2 = (b["ID"])
# id3 = (d["ID"])

# port1 = (z["Ports"])
# port2 = (b["Ports"])
# port3 = (d["Ports"])

# container1 = "Image: " + (z["Image"]), "Networks: " + (z["Networks"]), "ID: " + (z["ID"]), "Ports: " + (z["Ports"])
# container2 = "Image: " + (b["Image"]), "Networks: " + (b["Networks"]), "ID: " + (b["ID"]), "Ports: " + (b["Ports"])
# container3 = "Image: " + (d["Image"]), "Networks: " + (d["Networks"]), "ID: " + (d["ID"]), "Ports: " + (d["Ports"])

# Containers = [container1, container2, container3]


# @app.route("/")
# def home():
#     return render_template('index.html', name1=name1, name2=name2, name3=name3, network1=network1, network2=network2, network3=network3, id1=id1, id2=id2, id3=id3, port1=port1, port2=port2, port3=port3)
# if __name__ == '__main__':
#     app.run(debug=True)  



# Json parser
# variable name, network, ip, port
# docker container ls --format "{{json .}}"











    
 










  

  
    



