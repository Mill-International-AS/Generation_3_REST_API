#!/bin/bash

HEATER_ADDRESS="10.0.0.102"

while :
do
    result=$(curl -s -X GET http://${HEATER_ADDRESS}/control-status)
    echo $result | grep -Po '"ambient_temperature": [.0-9]*'
    sleep 1
done

