# photolab_docker_template

# About
This is a docker template for the needs of the Photolab

# How to build and run docker

## Build
docker build -t app_name_here .

## Run
docker run -d -p 5000:5000 app_name_here

## Test connection
curl 127.0.0.1:5000/run

## List docker images
docker image ls

## List all containers (active and non-active)
docker ps -a

## Remove image
docker image rm image_id

## Remove container
docker rm container_id

