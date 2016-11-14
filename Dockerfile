FROM python:2.7
MAINTAINER Gloria Palma "gloria@sentinel.la"
ADD . /app
WORKDIR /app/ 
RUN pip install -r requirements.txt
ENTRYPOINT ["./entrypoint.sh"]