#! /bin/bash

# https://medium.com/reportbee/docker-image-for-machine-learning-and-data-science-44bbdb917d4a

docker run --name lamp-smart-farm -p 80:80 -v /mnt/center/yandex-disk/projects/old/smart-farm/:/var/www/html/ mattrayner/lamp:latest
