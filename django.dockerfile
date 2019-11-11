FROM frankwolf/rpi-python3
MAINTAINER Jefferson Kwak <jeffersonkr@hotmail.com>
COPY . /home/pi/www
WORKDIR /home/pi/www
RUN sudo apt-get update
RUN sudo apt install libjpeg-dev -y && sudo apt install zlib1g-dev -y \
        && sudo apt install libfreetype6-dev -y && sudo apt install liblcms1-dev -y \
        && sudo apt install libopenjp2-7 -y && sudo apt install libtiff5 -y
RUN pip3 install -r requirements.txt
EXPOSE 8000