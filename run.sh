#!/bin/sh

printf "Run django app on\n\n1.Production mode [P]\n\n2.Production local simulation [S]\n\n3.Development mode [D]\n>> "
read params

Production = "p";

if [["$params" == "$Production"]]; then
    sudo docker-compose -f docker-compose-deploy.yml up

else 
    echo "fuck you bitch"
fi
