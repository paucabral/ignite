#!/bin/bash

ifconfig eth0 $1
ifconfig eth0 netmask $2
ifconfig eth0 broadcast $3
route add default gw $4 eth0
