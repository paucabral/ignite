#!/bin/bash

ifconfig $5 $1
ifconfig $5 netmask $2
ifconfig $5 broadcast $3
route add default gw $4 $5
