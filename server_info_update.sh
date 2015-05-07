#!/bin/bash
workdir=$1
infofile="server_info.txt"

curl -sSfLk -m 10 -H 'Accept: text/plain'  http://10.27.17.46:8080/v2/tasks > /tmp/${infofile}

if ! [ -f  ${workdir}/${infofile} ]
then 
  touch  ${workdir}/${infofile}
fi

if ! diff -q /tmp/${infofile} ${workdir}/${infofile} > /dev/null
then
  cat /tmp/${infofile} > ${workdir}/${infofile}
fi
