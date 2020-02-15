#!/bin/bash

df -ha > test.txt
tr -s ' ' ',' <test.txt >diskspace.txt
