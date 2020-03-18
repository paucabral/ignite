#!/bin/bash

shutdown -h $1
notify-send "$2" "$3"
