FROM python:3

WORKDIR /usr/src/app/
COPY requirements.txt ./
COPY . /usr/src/


ENV https_proxy http://10.110.15.60:8080/
ENV http_proxy http://10.110.15.60:8080
RUN apt-get update -y && apt install -y default-libmysqlclient-dev
RUN apt-get install -y iputils-ping

RUN apt-get update \
    &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata 

RUN python3 -m pip install --upgrade pip --proxy=http://10.110.15.60:8080
RUN pip install --no-cache-dir -r requirements.txt --proxy=http://10.110.15.60:8080 --default-timeout=1000

CMD [ "python", "main.py" ]
