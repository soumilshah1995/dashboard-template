import os

# Step 1: Display
print(os.popen('echo -------------------------------------------------').read())
print(os.popen('echo Starting Build of Docker Images').read())
print(os.popen('echo \n').read())


# Step 2: Build Image
print(os.popen('echo -------------------------------------------------').read())
print(os.popen('docker build -t project_dashboardnew .   ').read())
print(os.popen('echo \n').read())




# Step 3: Print Message
print(os.popen('echo -------------------------------------------------').read())
print(os.popen('echo Docker Image Build complete').read())
print(os.popen('echo \n').read())




# Step 4: Print Message Service Deployment
print(os.popen('echo -------------------------------------------------').read())
print(os.popen('echo Creating deployment Services ').read())
print(os.popen('echo \n').read())



# Step 5: Deploy Image
print(os.popen('echo -------------------------------------------------').read())
print(os.popen('docker service create --name project_dashboardnew --publish 8080:80 project_dashboardnew ').read())
print(os.popen('echo \n').read())



# Step 6: Deploy Dash Board 8090 port
print(os.popen('echo -------------------------------------------------').read())
print(os.popen('echo Creating Dash Board').read())
print(os.popen('echo \n').read())
print(os.popen("""docker service create \
  --name=viz \
  --publish=8090:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  dockersamples/visualizer""").read())
print(os.popen('echo \n').read())


# Step 7: Print the IDS
print(os.popen('docker service ls').read())
print(os.popen('echo -------------------------------------------------').read())
print(os.popen('echo \n').read())

# To delete Service
# docker service rm test

# Scaling
# docker service scale test=2
# docker service update --replicas=3 test



"""

ARM 


docker service create \
  --name=viz \
  --publish=8080:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  alexellis2/visualizer-arm:latest
"""