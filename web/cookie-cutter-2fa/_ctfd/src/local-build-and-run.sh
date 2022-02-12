#!/bin/bash
app="oweek-ctf-cookie-cutter-2fa"
docker build -t ${app} .
docker run -d -p 420:80 \
  --name=${app} \
  -v $PWD:/app ${app}
