#!/bin/bash
app="oweek-ctf-rolld"
docker build -t ${app} .
docker run -d -p 420:80 \
  --name=${app} \
  -v $PWD:/app ${app}
