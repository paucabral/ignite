#!/bin/bash

id $1 > user.txt
echo "" >> user.txt
chage -l $1 >> user.txt
tr -s '\t' ' ' <user.txt >userinfo.txt
