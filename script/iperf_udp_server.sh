#!/bin/sh

#####################
# Get 2 parameter
# 1. Log filename to save log
# 2. The iperf path, default in /usr/bin
# 3. The listening port
#####################

#IPERF_PATH="/tmp/network_test/"
IPERF_PATH=$1
#LISTEN_PORT=16666
LISTEN_PORT=$2 
#ETHER=eth0
ETHER=$3

#ip_addr=$(ifconfig $ETHER | grep "inet " | awk '{ print $2}' | awk -F: '{print $2}')
ip_addr=$(ifconfig $ETHER | grep "inet " | awk 'NR==1 {print $2}')
LOG_FILE='/tmp/'$ip_addr"_udp_server.log"

echo "Save log to "$LOG_FILE

#listen for iperf
nohup $IPERF_PATH"/iperf" -s -i 1 -p $LISTEN_PORT -u > $LOG_FILE &

echo "iperf server running\n"


