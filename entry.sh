#!/bin/bash

if [ -z "$1" ]
then
    echo "No initial chapter number supplied"
    exit 1
fi

echo $1 > previous
crond -f
