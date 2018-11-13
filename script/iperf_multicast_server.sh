#!/bin/sh

#####################
# Get 2 parameter
# 1. Log filename to save log
# 2. The iperf path, default in /usr/bin
# 3. multicast address
# 4. The listening port
#####################

#IPERF_PATH="/tmp/network_test/"
IPERF_PATH=$1
#MULTICAST_ADDRESS="239.255.255.252"
MULTICAST_ADDRESS=$2
#LISTEN_PORT=16666
LISTEN_PORT=$3
#ETHER=eth0
ETHER=$4

#ip_addr=$(ifconfig $ETHER | grep "inet " | awk '{ print $2}' | awk -F: '{print $2}')
ip_addr=$(ifconfig $ETHER | grep "inet " | awk 'NR==1 {print $2}')
LOG_FILE=$ip_addr"_udp_server.log"

echo "Save log to "$LOG_FILE

#listen for iperf
nohup $IPERF_PATH"/iperf" -s -u -B $MULTICAST_ADDRESS -i 1 -p $LISTEN_PORT | tee $LOG_FILE &
