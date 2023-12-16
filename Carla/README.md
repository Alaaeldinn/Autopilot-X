# Carla - Docker setup 

# Pull 

```bash
docker pull carlasim/carla:latest
```

# Run Container 

```bash
docker run \
 -p 2000-2002:2000-2002 \
 --runtime=nvidia \
 --gpus all \
 -e DISPLAY=$DISPLAY \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -it \
 carlasim/carla \
 bash
```


