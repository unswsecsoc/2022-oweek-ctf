FROM python:3.8-alpine
RUN apk update && apk add --no-cache socat
RUN apk add py3-pip
RUN pip3 install requests lxml
WORKDIR /srv/
COPY login.py .
ENV TIMEOUT=300
EXPOSE 9999
ENTRYPOINT socat TCP-LISTEN:9999,reuseaddr,fork EXEC:"timeout $TIMEOUT python login.py"
