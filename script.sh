
#!/bin/sh
sudo apt-get update
sudo apt-get install apache2 apache2-doc apache2-mpm-prefork apache2-utils libexpat1 ssl-cert -y

wget https://raw.githubusercontent.com/SerDigital/OpenStack/master/index.html

sudo cp index.html /var/www/html/index.html

#wget https://github.com/SerDigital/OpenStack/Pokemon/articuno.png
#sudo cp articuno.png /var/www/html/articuno.png

#wget https://github.com/SerDigital/OpenStack/Pokemon/ditto.png
#sudo cp ditto.png /var/www/html/ditto.png

#wget https://github.com/SerDigital/OpenStack/Pokemon/moltres.png
#sudo cp moltres.png /var/www/html/moltres.png
