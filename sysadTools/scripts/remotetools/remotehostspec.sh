#!/bin/bash

ssh $1@$2 -t "screenfetch -N > remotehostspec.txt"
scp $1@$2:remotehostspec.txt .
