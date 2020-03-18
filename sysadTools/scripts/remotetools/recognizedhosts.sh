#!/bin/bash

arp-scan --interface=$1 --localnet | tail -n +3 | head -n -3 | tr -s "\t" "," > recognized_hosts.txt
