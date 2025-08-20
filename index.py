#Putty gen
print("01. Authenticate type: SSH public Key, SSH public key source: Use existing public key ")
print("02. generate key -> pub.Key in azure -> save Prkey")
print("03. tick http and https")
print("03. open prkey in putty: SSH->Auth->credential->browse")

#Hosting
print("01. after update and upgrade : sudo apt install apache2")
print("02. cd /var/www/html")
print(" sudo mv index.html demo.html")
print("sudo touch index.html")

#Linux GUI
print("sudo DEBIAN_FRONTEND=noninteractive apt-get -y install xfce4 ")
print("sudo apt install xfce4-session")
print("sudo apt-get -y install xrdp")
print("sudo systemctl enable xrdp")
print("sudo adduser xrdp ssl-cert")
print("echo xfce4-session >~/.xsession")
print("sudo systemctl restart xrdp")
print("Add inbound port RDP.")

#docker
print("install docker: sudo apt install docker.io")
print(" check the Ubuntu OS: lsb_release -a")
print(" check if the docker service is running or not: sudo systemctl status docker")
print("check the Docker Client and Docker Server information: sudo docker version or sudo docker info")
print("Check the disk usage for different components : sudo docker system df")
print(" remove all unused objects: sudo docker system prune")
print(" check the real time resource usage of different containers: sudo docker stats")
print("show all image: sudo docker images")
print("show all container: sudo docker ps -a")
print("show running container: sudo docker ps")
print("pull image: sudo docker pull openjdk")
print("create sample container: sudo docker create --name sample openjdk")
print("run the container: sudo docker start sample")
print("Remove a container by its name: sudo docker rm [container_name]")
print("Stop a running container by its name: sudo docker stop [container_name]")
print("run the container in back: sudo docker run -d -it --name [container_name] [image_name]")
print("goto inside the image: sudo docker exec -it webpage1 /bin/bash"+"list bin commands: ls -lrt")
print("backup the image: sudo docker save [image_id / image_name] >sujah.tar")
print("load the backup tar file: sudo docker load -i sujah.tar")

#docker build image
print("create java file and implement the code")
print("create docker file: Dockerfile")
print("build docker image: sudo docker build -t my-java-app:release1 .")
print("stop all running container and run new container: sudo docker run -it my-java-app:release1")

#push into dockerhub
print("sudo docker login")
print("tag the image your username: sudo docker tag my-java-app:release1 dilax101/myjavaapp")
print("push the image to dockerhub: sudo docker push dilax101/myjavaapp")





