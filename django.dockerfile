FROM frankwolf/rpi-python3
MAINTAINER Jefferson Kwak <jeffersonkr@hotmail.com>
COPY . /home/pi/www
WORKDIR /home/pi/www
RUN sudo apt-get update
RUN sudo apt-get install libjpeg-dev -y
RUN sudo apt-get install zlib1g-dev -y
RUN sudo apt-get install libfreetype6-dev -y
RUN sudo apt-get install liblcms1-dev -y
RUN sudo apt-get install libopenjp2-7 -y
RUN sudo apt-get install libtiff5 -y
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD python3 manage.py migrate
CMD python3 manage.py makemigrations
CMD python3 manage.py migrate