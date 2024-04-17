#!/bin/bash

DIR="/home/ec2-user/myapp"
if [-d "$DIR" ]; then
	echo "${DIR} exists"
else
   echo "Creating ${DIR} directory"
   mkdir ${DIR}
fi