#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
apt-get update && \
apt-get install -y nginx && \
mkdir -p -m=755 /data/web_static/{releases/test,shared} || exit 0
echo 'Holberton School for win!' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
insert='\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}'
