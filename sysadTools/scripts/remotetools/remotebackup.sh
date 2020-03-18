#!/bin/bash

if [ $1 = "1" ]
then
	echo "Run backup"
	tar -czvf ~/backup.tgz ~
elif [ $1 = "2" ]
then
	echo "Extract backup"
	tar -xzvf ~/backup.tgz -C ~/backup
else
	echo "Delete backup"
	rm ~/backup.tgz
fi
