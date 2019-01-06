FROM python:3.6

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./ /usr/src/app

RUN apt-get update -y
RUN apt-get install cmake -y
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000
CMD [ "python", "./run.py" ]