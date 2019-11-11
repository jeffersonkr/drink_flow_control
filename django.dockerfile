FROM frankwolf/rpi-python3
MAINTAINER Jefferson Kwak <jeffersonkr@hotmail.com>
COPY . /home/pi/www
WORKDIR /home/pi/www
RUN apt-get update && apt-get install -y \
        libjpeg-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms1-dev \
        libopenjp2-7 \ 
        libtiff5 \
        mariadb-dev \ 
        mariadb-client \
        mariadb-libs \ 
        python3-dev \ 
        build-base
RUN pip3 install -r requirements.txt
EXPOSE 8000