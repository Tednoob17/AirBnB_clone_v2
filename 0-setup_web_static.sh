#!/usr/bin/env bash
# Setup web servers for the deployment of web_static

# Install Nginx if it not already installed
apt-get update -y
apt-get upgrade -y
apt-get install nginx -y

# Create the folders if they don’t already exist
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

echo "<h2>Basic HTML file</h2>" > /data/web_static/releases/test/index.html

# Create a symbolic link
ln -fs /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i '/^\tserver_name/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-available/default

# Restart Nginx after updating the configuration
service nginx restart
