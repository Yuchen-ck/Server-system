sudo docker run --rm -it     -v /tmp/.X11-unix:/tmp/.X11-unix     -e DISPLAY=$DISPLAY     -u qtuser     server/system:latest python3.7 /home/qtuser/Server-system/system_main.py
